import pyinotify, os, subprocess, argparse, socket, time, glob
import readnet

wm = pyinotify.WatchManager()
watchedfolders = {}

parser = argparse.ArgumentParser()
parser.add_argument("-c","--scp",action="store_true",help="Copy using scp")
parser.add_argument("-r","--rsync",action="store_true",help="Copy using rsync")
args = parser.parse_args()

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

    #Check for IP not to copy too
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
        for files in glob.glob("Stop-*"):
            f = open(files,"r");
            for line in f:
                l = line.split()
                if l[0] == ip and l[1] == path and modTime <= l[2:]:
                    stop = True
                else:
                    stopIPs[l[0]] = l[1]

            if stop:
                f.close()
                f = open(files,"w")
                for k in stopIPs.keys():
                    f.write(k + " " + stopIPs[k])
                f.close()
                stopIPs.clear()
                return True

            f.close()
            stopIPs.clear()


        return False

    #Set flag on other server telling it not to immediately try and copy data here
    
    def setStopFileUniq(self,ip,myIP,path):
        w = open("/home/cal/Documents/Private-Sync/whoami","r")
        nodename = w.read()
        nodename = nodename[0].upper()
        w.close()
        subprocess.call(["ssh",ip,"echo " + myIP + " " + path + " " + self.getModTime(path) + " >> /home/cal/Documents/Private-Sync/Stop-" + nodename])
        print "ssh",ip,"echo " + myIP + " " + path  + " " + self.getModTime(path) + " >> /home/cal/Documents/Private-Sync/Stop-" + nodename

    def setStopFile(self,ip,myIP,path):
        subprocess.call(["ssh",ip,"echo " + myIP + " " + path + "> /home/cal/Documents/Private-Sync/stop"])
        print "ssh",ip,"echo " + myIP + "> /home/cal/Documents/Private-Sync/stop"

    def rmTree(self,path):
        subprocess.call(["ssh",ip,"rm -r '" + path + "'"])
        print "ssh",ip,"rm -r '" + path + "'"

    def fileSync(self,event):
        if os.path.isdir(event.pathname):
            print "Watching: ",event.pathname
        for folder in watchedfolders.keys():
            if folder in event.pathname:
                for i in range(0, len(watchedfolders[folder]),2):
                    ip = watchedfolders[folder][i]
                    path = watchedfolders[folder][i+1]
                    #print ip + " " + path
                    readnet.logIPtraffic(ip)
                    myIP = readnet.getMyIP(ip)
                    subprocess.call(["ssh",ip,"/usr/bin/python /home/cal/Documents/Private-Sync/readnet.py -i " + myIP])
                    print "ssh",ip,"'/usr/bin/python /home/cal/Documents/Private-Sync/readnet.py -i " + myIP + "'"
                    #stopIP = self.getStopInfo()
                    #print "STOP: " + stopIP[0] + " " + stopIP[1]
                    #if stopIP[0] == ip and stopIP[1] == event.pathname:
                    if self.inStopFile(ip,event.pathname):
                        print "STOPPED"
                        #os.remove("./stop");
                    else:
                        print "CONTINUE"
                        if args.scp:
                            subprocess.call(["scp","-rp",folder,ip + ":" + path])
                            print "scp","-rp",folder,ip + ":" + path
                        elif args.rsync:
                                subprocess.call(["rsync","-rt",folder,ip + ":" + path])
                                print "rsync","-rt",folder,ip + ":" + path
                        else:
                                time.sleep(5)
                                fparts = folder.split("/")
                                fname = fparts[len(fparts)-1]
                                print fname
                                subprocess.call(["unison","-batch","-confirmbigdel=false",folder,"ssh://" + ip + "/" + path + fname])
                                print "unison","-batch","-confirmbigdel=false",folder,"ssh://" + ip + "/" + path + fname
                        self.setStopFileUniq(ip,myIP,event.pathname)
                    subprocess.call(["ssh",ip,"/usr/bin/python /home/cal/Documents/Private-Sync/readnet.py -i " + myIP])
                    readnet.logIPtraffic(ip)

    #def process_IN_CREATE(self, event):
    #    print "Create:",event.pathname
    def process_IN_DELETE(self, event):
        print "Delete:",event.pathname
        self.fileSync(event)
    def process_IN_CREATE(self, event):
        print "Modify:",event.pathname
        self.fileSync(event)


def main():

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

    #print watchedfolders
    eh = MyEventHandler()

    notifier = pyinotify.Notifier(wm,eh)
    notifier.loop()

if __name__ == '__main__':
    main()
