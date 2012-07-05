import pyinotify
import os

wm = pyinotify.WatchManager()

class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print "Create:",event.pathname
    def process_IN_DELETE(self, event):
        print "Delete:",event.pathname
        #Can be done with flags...
        """
        i = 0
        rw = open('./folderstowatch','r+')
        for folder in rw:
            print folder
            print i
            if(folder == event.pathname):
                #rw.seek(-1 * len(folder),1)
                rw.seek(i)
                rw.write("!#!")
                wm.del_watch(event.pathname)
                break
            i += len(folder)
        rw.close()
        """

    def process_IN_CREATE(self, event):
        print "Modify:",event.pathname
        if os.path.isdir(event.pathname):
            print "Watching: ",event.pathname
            #wm.add_watch(event.pathname,pyinotify.ALL_EVENTS, rec=True)
            #w = open('./folderstowatch','a')
            #w.write(event.pathname)
            #w.close()

def main():

    f = open('./folderstowatch','r+')

    for folder in f:
        wm.add_watch(folder.rstrip(),pyinotify.ALL_EVENTS, rec=True, auto_add=True)
        print "Watching: ", folder.rstrip()


    eh = MyEventHandler()

    notifier = pyinotify.Notifier(wm,eh)
    notifier.loop()

if __name__ == '__main__':
    main()
