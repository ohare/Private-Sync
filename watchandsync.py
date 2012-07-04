import pyinotify

class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print "Create:",event.pathname
    def process_IN_DELETE(self, event):
        print "Delete:",event.pathname
    def process_IN_CREATE(self, event):
        print "Modify:",event.pathname

def main():
    wm = pyinotify.WatchManager()
    wm.add_watch('/home/cal/Documents/one',pyinotify.ALL_EVENTS, rec=True)

    eh = MyEventHandler()

    notifier = pyinotify.Notifier(wm,eh)
    notifier.loop()

if __name__ == '__main__':
    main()
