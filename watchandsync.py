import pyinotify, os, subprocess, argparse

wm = pyinotify.WatchManager()
watchedfolders = {}

parser = argparse.ArgumentParser()
parser.add_argument("-c","--scp",action="store_true",help="Copy using scp")
parser.add_argument("-r","--rsync",action="store_true",help="Copy using rsync")
args = parser.parse_args()

#TODO stats and service and run command

class MyEventHandler(pyinotify.ProcessEvent):
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
                subprocess.call(["python","/home/cal/Documents/Private-Sync/readnet.py"])
                if args.scp:
			subprocess.call(["scp","-r",folder,watchedfolders[folder][0] + ":" + watchedfolders[folder][1]])
                        print "scp","-r",folder,watchedfolders[folder][0] + ":" + watchedfolders[folder][1]
                elif args.rsync:
			subprocess.call(["rsync","-r",folder,watchedfolders[folder][0] + ":" + watchedfolders[folder][1]])
                        print "rsync","-r",folder,watchedfolders[folder][0] + ":" + watchedfolders[folder][1]
                else:
                        fparts = folder.split("/")
                        fname = fparts[len(fparts)-1]
                        print fname
			subprocess.call(["unison","-batch","-confirmbigdel=false",folder,"ssh://" + watchedfolders[folder][0] + "/" + watchedfolders[folder][1] + fname])
                        print "unison","-batch","-confirmbigdel=false",folder,"ssh://" + watchedfolders[folder][0] + "/" + watchedfolders[folder][1] + fname
                subprocess.call(["python","/home/cal/Documents/Private-Sync/readnet.py"])

#class watchfolders():
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
