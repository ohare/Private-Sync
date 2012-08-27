import pyinotify, os, subprocess, argparse, socket
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

    def process_IN_CREATE(self, event):
        print "Create:",event.pathname
    def process_IN_DELETE(self, event):
        print "Delete:",event.pathname
    def process_IN_CREATE(self, event):
        print "Modify:",event.pathname
        if os.path.isdir(event.pathname):
            print "Watching: ",event.pathname
        for folder in watchedfolders.keys():
            if folder in event.pathname:
                ip = watchedfolders[folder][0]
                path = watchedfolders[folder][1]
                readnet.logIPtraffic(ip)
                subprocess.call(["ssh",ip,"/usr/bin/python /home/cal/Documents/Private-Sync/readnet.py -i " + self.flipIP(ip)])
                print "ssh",ip,"'/usr/bin/python /home/cal/Documents/Private-Sync/readnet.py -i " + self.flipIP(ip) + "'"
                myIP = readnet.getMyIP(ip)
                if args.scp:
                    if not os.path.exists("./stop"):
                        subprocess.call(["ssh",ip,"echo " + myIP + "> /home/cal/Documents/Private-Sync/stop"])
                        print "ssh",ip,"touch /home/cal/Documents/Private-Sync/stop"
			subprocess.call(["scp","-r",folder,ip + ":" + path])
                        print "scp","-r",folder,ip + ":" + path
                    else:
                        os.remove("./stop");
                elif args.rsync:
			subprocess.call(["rsync","-r",folder,ip + ":" + path])
                        print "rsync","-r",folder,ip + ":" + path
                else:
                        fparts = folder.split("/")
                        fname = fparts[len(fparts)-1]
                        print fname
			subprocess.call(["unison","-batch","-confirmbigdel=false",folder,"ssh://" + ip + "/" + path + fname])
                        print "unison","-batch","-confirmbigdel=false",folder,"ssh://" + ip + "/" + path + fname
                subprocess.call(["ssh",ip,"/usr/bin/python /home/cal/Documents/Private-Sync/readnet.py -i " + self.flipIP(ip)])
                readnet.logIPtraffic(ip)


def main():

    f = open('./folderstowatch','r')

    for folder in f:
        if(folder[0] == '#'):
            pass
        else:
            info = folder.split()
            wm.add_watch(info[0].rstrip(),pyinotify.ALL_EVENTS, rec=True, auto_add=True)
            print "Watching: ", info[0].rstrip()
            watchedfolders[info[0].rstrip()] = [info[1],info[2]]


    eh = MyEventHandler()

    notifier = pyinotify.Notifier(wm,eh)
    notifier.loop()

if __name__ == '__main__':
    main()
