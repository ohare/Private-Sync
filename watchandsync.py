import pyinotify
import os

wm = pyinotify.WatchManager()

class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print "Create:",event.pathname
    def process_IN_DELETE(self, event):
        print "Delete:",event.pathname
    def process_IN_CREATE(self, event):
        print "Modify:",event.pathname
        if os.path.isdir(event.pathname):
            print "Watching: ",event.pathname

def main():

    f = open('./folderstowatch','r')

    for folder in f:
        wm.add_watch(folder.rstrip(),pyinotify.ALL_EVENTS, rec=True, auto_add=True)
        print "Watching: ", folder.rstrip()


    eh = MyEventHandler()

    notifier = pyinotify.Notifier(wm,eh)
    notifier.loop()

if __name__ == '__main__':
    main()
