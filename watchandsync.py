import pyinotify
import os
import subprocess

wm = pyinotify.WatchManager()
watchedfolders = {}

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
                #subprocess.call(["scp","-r",folder,watchedfolders[folder][0] + ":" + watchedfolders[folder][1]])
                #subprocess.call(["rsync","-r",folder,watchedfolders[folder][0] + ":" + watchedfolders[folder][1]])
                subprocess.call(["unison",folder,watchedfolders[folder][0] + watchedfolders[folder][1]])
                #print "scp","-r",folder,watchedfolders[folder][0] + ":" + watchedfolders[folder][1]
                subprocess.call(["python","/home/cal/Documents/Private-Sync/readnet.py"])

#class watchfolders():
def main():

    f = open('./folderstowatch','r')

    for folder in f:
        info = folder.split()
        wm.add_watch(info[0].rstrip(),pyinotify.ALL_EVENTS, rec=True, auto_add=True)
        print "Watching: ", info[0].rstrip()
        watchedfolders[info[0].rstrip()] = [info[1], info[2]]


    eh = MyEventHandler()

    notifier = pyinotify.Notifier(wm,eh)
    notifier.loop()

if __name__ == '__main__':
    main()
