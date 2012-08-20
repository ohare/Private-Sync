import glob, os, datetime, time

def main():
    first = True
    start_time = 0
    start_mb = 0

    os.chdir("./logs")
    for files in glob.glob("*"):
        print files
        f = open(files,"r");
        for line in f:
            print line
            l = line.split()
            if first:
                first = False
                start_time = date_to_i(l[1])
                start_mb = int(l[6])
            print str(date_to_i(l[1]) - start_time) + " " + str(int(l[6]) - start_mb)
        first = True

        f.close();

def date_to_i(date):
    date = date.split(".")[0]
    x = time.strptime(date.split(',')[0],'%H:%M:%S')
    t = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    return t

if __name__ == "__main__":
    main()
