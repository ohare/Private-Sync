import pyinotify
import os
import subprocess

wm = pyinotify.WatchManager()
watchedfolders = []

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
        for folder in watchedfolders:
            if folder in event.pathname:
                subprocess.call(["ls","-l",folder])


#class watchfolders():
def main():

    f = open('./folderstowatch','r')

    for folder in f:
        wm.add_watch(folder.rstrip(),pyinotify.ALL_EVENTS, rec=True, auto_add=True)
        print "Watching: ", folder.rstrip()
        watchedfolders.append(folder.rstrip())


    eh = MyEventHandler()

    notifier = pyinotify.Notifier(wm,eh)
    notifier.loop()

if __name__ == '__main__':
    main()
