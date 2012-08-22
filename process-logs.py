import glob, os, datetime, time

def main():
    first = True
    start_time = 0
    start_mb = 0
    max_mb = 0
    max_name = ""

    """
    os.chdir("./logs")
    for files in glob.glob("*"):
        f = open(files,"r");
        for line in f:
            l = line.split()
            if float(l[6]) > max_mb:
                max_mb = float(l[6])
                max_name = files
        f.close()
    """

    os.chdir("./logs")
    count = 1
    bytes_field = 4
    date_field = 1
    fin = {'nodeA':[0,0],'nodeB':[0,0],'nodeC':[0,0],'nodeD':[0,0]}
    for files in glob.glob("*"):
        #print files
        #if files == max_name:
        names = files.split("-")
        #print names
        f = open(files,"r");
        x = open("../graphs/" + names[0] + "-data","a");
        for line in f:
            #print line
            l = line.split()
            if first:
                first = False
                start_time = date_to_i(l[date_field])
                start_mb = float(l[bytes_field])
            x.write(str(date_to_i(l[date_field]) - start_time) + \
            " " + str(((float(l[bytes_field]) - start_mb)/1024)/1024) + "\n")
            if(fin[names[0]][0] < date_to_i(l[date_field]) and fin[names[0]][1] < float(l[bytes_field])):
                fin[names[0]][0] = date_to_i(l[date_field])
                fin[names[0]][1] = float(l[bytes_field])

        x.close()
        first = True
        f.close();
        count += 1

    timesort = []
    for node in fin:
        #print node
        timesort.append(fin[node][0])

    timesort.sort()
    count = 1
    x = open("../graphs/comp-time","a")
    x.write("0 0\n")
    for time in timesort:
        x.write(str(time) + " " + str(count) + "\n")
        count += 1
    x.close()

    print "Success"

def date_to_i(date):
    date = date.split(".")[0]
    x = time.strptime(date.split(',')[0],'%H:%M:%S')
    t = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    return t

if __name__ == "__main__":
    main()
