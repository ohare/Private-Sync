import pyinotify, os, subprocess, argparse, socket, time, glob, datetime
import readnet

wm = pyinotify.WatchManager()
watchedfolders = {}
homepath = "/home/cal/Documents/Private-Sync/"
#homepath = "/Users/calum/Documents/Private-Sync/"

parser = argparse.ArgumentParser()
parser.add_argument("-c","--scp",action="store_true",help="Copy using scp")
parser.add_argument("-r","--rsync",action="store_true",help="Copy using rsync")
args = parser.parse_args()

class Tools():
    def updateFolderInfo(self, wfolds):
        f = open('./folders.dat','w')
        for fold in wfolds:
            f.write(fold + " ")
            for i in range(0,len(wfolds[fold])-1):
                f.write(wfolds[fold][i] + " ")
            f.write(wfolds[fold][len(wfolds[fold])-1] + "\n")
        f.close()

    def timeElapsed(self, dtstamp, diff):
        if diff == "*":
            print "Sync ASAP"
            return
        diff = int(diff)
        FMT = '%Y-%m-%d %H:%M:%S.%f'
        #FMT = '%Y-%m-%d %H:%M:%S'
        tdelta = datetime.datetime.now() - datetime.datetime.strptime(dtstamp, FMT)
        print  tdelta.total_seconds()
        timeDiff = tdelta.total_seconds()
        if (timeDiff >= diff):
            print "Time period reached"
        else:
            print "Time not elapsed, sleeping for " + str(diff - timeDiff + 1)
            time.sleep(int(diff - timeDiff + 1))

class MyEventHandler(pyinotify.ProcessEvent):
    def flipIP(self,ip):
        octets = ip.split(".")
        if(octets[3] == "1"):
            octets[3] = "2"
        elif(octets[3] == "2"):
            octets[3] = "1"
        else:
            octets[3] = "1"
        return ".".join(octets)

    #Get the last modified time of a file
    def getModTime(self,path):
        try:
            return time.ctime(os.path.getmtime(path))
        except Exception, e:
            return ""

    #Deprecated - Check for IP not to copy too
    def getStopInfo(self):
        stopIP = ["",""]
        try:
            o = open("./stop",'r')
            stopIP = o.read().split()
            o.close()
        except IOError, e:
            pass
        return stopIP

    def inStopFile(self,ip,path):
        stopIPs = {}
        stop = False
        modTime = self.getModTime(path)
        while True:
            tmpcount = 0
            print "Files found: " + str(glob.glob("Stop-*"))
            for files in glob.glob("Stop-*"):
                #print "File: " + str(files)
                if ".tmp" in files:
                    tmpcount += 1
                    time.sleep(5)
                    break
                f = open(files,"r");
                for line in f:
                    l = line.split()
                    print "local " + str(path) + " modtime: " + modTime
                    print "Stop " + l[1] + " modtime: " + str(l[2:])
                    ts1 = time.strptime(modTime,"%a %b %d %H:%M:%S %Y")
                    ts2 = time.strptime(" ".join(l[2:]),"%a %b %d %H:%M:%S %Y")
                    print "local <= stop: " + str(ts1 <= ts2)
                    #if l[0] == ip and l[1] == path and ts1 <= ts2:
                    #If IP sending to has sent data more recently don't send back
                    if l[0] == ip and ts1 <= ts2:
                        print "Stop = True, file: " + l[0]
                        stop = True
                    else:
                        stopIPs[l[0]] = [l[1]," ".join(l[2:])]

                if stop:
                    f.close()
                    #f = open(files,"w")
                    #for k in stopIPs.keys():
                    #    f.write(k + " " + stopIPs[k][0] + " " + stopIPs[k][1] + "\n")
                    #f.close()
                    #stopIPs.clear()
                    return True

                f.close()
                #stopIPs.clear()
            if tmpcount == 0:
                break

        return False

    #Set flag on other server telling it not to immediately try and copy data here
    def setStopFileUniq(self,ip,myIP,path,folder):
        nodename = self.getNodeName()
        #print "ssh",ip,"echo " + myIP + " " + path + " " + self.getModTime(path) + " >> " + homepath + "Stop-" + nodename + ".tmp;"
        #subprocess.call(["ssh",ip,"echo " + myIP + " " + path + " " + self.getModTime(path) + " >> " + homepath + "Stop-" + nodename + ".tmp;"])
        subprocess.call(["ssh",ip,"rm " + homepath + "Stop-" + nodename + ".tmp;"])
        for cpFile in glob.glob(folder + "/*"): 
            subprocess.call(["ssh",ip,"echo " + myIP + " " + cpFile + " " + self.getModTime(cpFile) + " >> " + homepath + "Stop-" + nodename + ".tmp;"])

    #Sets the config files on the remote node
    def beginCopy(self, ip):
        nodename = self.getNodeName()
        print "ssh",ip,"touch " + homepath + "Stop-" + nodename + ".tmp; mv " + homepath + "Stop-" + nodename + " " + homepath + "Stop-" + nodename + ".tmp;"
        subprocess.call(["ssh",ip,"touch " + homepath + "Stop-" + nodename + ".tmp; mv " + homepath + "Stop-" + nodename + " " + homepath + "Stop-" + nodename + ".tmp;"])

    #Moves the Stop files back into place
    def endCopy(self, ip):
        nodename = self.getNodeName()
        print "ssh",ip,"mv " + homepath + "Stop-" + nodename + ".tmp " + homepath + "Stop-" + nodename
        subprocess.call(["ssh",ip,"mv " + homepath + "Stop-" + nodename + ".tmp " + homepath + "Stop-" + nodename])

    #Get node name from whoami file
    def getNodeName(self):
        w = open(homepath + "whoami","r")
        nodename = w.read()
        nodename = nodename[0].upper()
        w.close()
        return nodename

    #Deprecated stop file
    def setStopFile(self,ip,myIP,path):
        subprocess.call(["ssh",ip,"echo " + myIP + " " + path + "> " + homepath + "stop"])
        print "ssh",ip,"echo " + myIP + "> " + homepath + "stop"

    def rmTree(self,path):
        subprocess.call(["ssh",ip,"rm -r '" + path + "'"])
        print "ssh",ip,"rm -r '" + path + "'"

    #Exclude files matching patterns in the ignore file
    def exclusions(self, path):
        try:
            f = open("./ignore",'r')
            for line in f:
                if line.rstrip() in path:
                    #print "Ignoring: " + path
                    return True
            f.close()
        except error, e:
            print e
        return False

    #Sync files
    def fileSync(self,event):
        t = Tools()
        if os.path.isdir(event.pathname):
            print "Watching: ",event.pathname
        if self.exclusions(event.pathname):
            return
        for folder in watchedfolders.keys():
            print "For each folder: " + str(folder) + " in watchedfolder keys"
            if folder in event.pathname:
                for i in range(0, len(watchedfolders[folder]),4):
                    ip = watchedfolders[folder][i]
                    path = watchedfolders[folder][i+1]
                    waitTime = watchedfolders[folder][i+2]
                    lastTime = watchedfolders[folder][i+3]
                    print "Wait: " + str(waitTime) + " Last: " + str(lastTime) 
                    print "Current ip and path: " + ip + " " + path
                    readnet.logIPtraffic(ip, event.pathname)
                    myIP = readnet.getMyIP(ip)
                    subprocess.call(["ssh",ip,"/usr/bin/python " + homepath + "readnet.py -i " + myIP + " -f " + event.pathname])
                    print "ssh",ip,"'/usr/bin/python " + homepath + "readnet.py -i " + myIP + " -f " + event.pathname + "'"
                    fparts = folder.split("/")
                    fname = fparts[len(fparts)-1]
                    #stopIP = self.getStopInfo()
                    #print "STOP: " + stopIP[0] + " " + stopIP[1]
                    #if stopIP[0] == ip and stopIP[1] == event.pathname:
                    if self.inStopFile(ip,event.pathname):
                        print "STOPPED to " + ip + " " + path
                        #os.remove("./stop");
                    else:
                        print "CONTINUE"
                        t.timeElapsed(lastTime, waitTime)
                        watchedfolders[folder][i+3] = str(datetime.datetime.now())
                        t.updateFolderInfo(watchedfolders)
                        self.beginCopy(ip)
                        if args.scp:
                            #print "SCP: For cpFile in " + folder
                            for cpFile in glob.glob(folder + "/*"): 
                                #print "SCP GLOB:" + cpFile
                                print "scp","-rp",cpFile,ip + ":" + cpFile + ".tmp"
                                subprocess.call(["scp","-rp",cpFile,ip + ":" + cpFile + ".tmp"])
                                #subprocess.call(["ssh",ip,"yes y | find /tmp/" + fname + " -type f -exec cp -p {} " + path + fname + "/ \; rm /tmp/" + fname])
                                print "ssh",ip,"mv " + cpFile + ".tmp " + cpFile
                                subprocess.call(["ssh",ip,"mv " + cpFile + ".tmp " + cpFile])
                                print "END SCP GLOB"
                        elif args.rsync:
                            print "rsync","-rt",folder,ip + ":" + path
                            subprocess.call(["rsync","-rt",folder,ip + ":" + path])
                        else:
                            time.sleep(5)
                            print "unison","-batch","-confirmbigdel=false","-times",folder,"ssh://" + ip + "/" + path + fname
                            subprocess.call(["unison","-batch","-confirmbigdel=false","-times",folder,"ssh://" + ip + "/" + path + fname])
                        self.setStopFileUniq(ip,myIP,event.pathname,folder)
                        self.endCopy(ip)
                    subprocess.call(["ssh",ip,"/usr/bin/python " + homepath + "readnet.py -i " + myIP + " -f " + event.pathname])
                    readnet.logIPtraffic(ip, event.pathname)

    #def process_IN_CREATE(self, event):
    #    print "Create:",event.pathname
    def process_IN_DELETE(self, event):
        print "Delete: ",event.pathname
        #self.fileSync(event)
    def process_IN_CREATE(self, event):
        print "CREATE: ",event.pathname
        self.fileSync(event)
    def process_IN_MOVED_FROM(self, event):
        print "Move from: ",event.pathname
    #    self.fileSync(event)
    def process_IN_MODIFY(self, event):
        #print "Modify: ",event.pathname
        self.fileSync(event)
    def process_IN_MOVED_TO(self, event):
        print "Move to: ",event.pathname
        self.fileSync(event)


def main():
    t = Tools()
    f = open('./folderstowatch','r')

    for folder in f:
        if(folder[0] == '#'):
            pass
        else:
            info = folder.split()
            wm.add_watch(info[0].rstrip(),pyinotify.ALL_EVENTS, rec=True, auto_add=True)
            print "Watching: ", info[0].rstrip()
            if info[0] not in watchedfolders.keys():
                watchedfolders[info[0].rstrip()] = []
            watchedfolders[info[0].rstrip()].append(info[1])
            watchedfolders[info[0].rstrip()].append(info[2])
            watchedfolders[info[0].rstrip()].append(info[3])
            watchedfolders[info[0].rstrip()].append(str(datetime.datetime.now()))
    f.close()

    try:
        f = open('./folders.dat','r')
        for folder in f:
            if(folder[0] == '#'):
                pass
            else:
                info = folder.split()
                if info[0] in watchedfolders.keys():
                    del watchedfolders[info[0].rstrip()]
                    #wm.add_watch(info[0].rstrip(),pyinotify.ALL_EVENTS, rec=True, auto_add=True)
                    #print "Watching: ", info[0].rstrip()
                    if info[0] not in watchedfolders.keys():
                        watchedfolders[info[0].rstrip()] = []
                    watchedfolders[info[0].rstrip()].append(info[1])
                    watchedfolders[info[0].rstrip()].append(info[2])
                    watchedfolders[info[0].rstrip()].append(info[3])
                    watchedfolders[info[0].rstrip()].append(str(datetime.datetime.now()))
                else:
                    print "Removing: " + info[0]
        f.close()
    except IOError, e:
        print "Folders.dat does not exist, skipping"

    t.updateFolderInfo(watchedfolders)

    #print watchedfolders
    eh = MyEventHandler()

    notifier = pyinotify.Notifier(wm,eh)
    notifier.loop()

if __name__ == '__main__':
    main()
