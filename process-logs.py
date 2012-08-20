import glob, os, datetime, time

def main():
    first = True
    start_time = 0
    start_mb = 0
    max_mb = 0
    max_name = ""

    os.chdir("./logs")
    for files in glob.glob("*"):
        f = open(files,"r");
        for line in f:
            l = line.split()
            if float(l[6]) > max_mb:
                max_mb = float(l[6])
                max_name = files
        f.close()

    for files in glob.glob("*"):
        #print files
        if files == max_name:
            f = open(files,"r");
            x = open("../graphs/data","a");
            for line in f:
                #print line
                l = line.split()
                if first:
                    first = False
                    start_time = date_to_i(l[1])
                    start_mb = float(l[6])
                x.write(str(date_to_i(l[1]) - start_time) + \
                " " + str(((float(l[6]) - start_mb)/1024)/1024) + "\n")
            x.close()
            first = True
            f.close();

    print "Success"

def date_to_i(date):
    date = date.split(".")[0]
    x = time.strptime(date.split(',')[0],'%H:%M:%S')
    t = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    return t

if __name__ == "__main__":
    main()
