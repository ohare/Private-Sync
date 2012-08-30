import glob, os, time, sys
from datetime import datetime

def main():
    first = True
    start_time = 0
    start_mb = 0
    max_mb = 0
    max_name = ""

    #divide_by = 1024/1024
    divide_by = 1

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
    lastNode = ""
    num_mb_dict = {}
    beginning_time = -1
    for files in glob.glob("*"):
        #print files
        #if files == max_name:
        names = files.split("-")
        f = open(files,"r");
        if names[0] == lastNode:
            pass
        else:
            #print lastNode
            total = 0
            x = open("../graphs/" + lastNode + "-data","a");
            #print num_mb_dict
            for key in sorted(num_mb_dict.iterkeys()):
                total += num_mb_dict[key]
                #print num_mb_dict[key]
                #print str(key) + " " + str(total/divide_by)
                x.write(str(key) + " " + str(total/divide_by) + "\n")
            num_mb_dict = {}
            x.close()
        prev = 0
        for line in f:
            #print line
            l = line.split()
            if first:
                first = False
                start_time = l[date_field]
                start_mb = long(l[bytes_field])
                prev = start_mb
                if beginning_time == -1:
                    beginning_time = l[date_field]
                elif int(secondsDiff(beginning_time,l[date_field])) > 0:
                    beginning_time = l[date_field]
            elapsed = int(secondsDiff(l[date_field],start_time))
            #print elapsed
            if elapsed in num_mb_dict:
                num_mb_dict[elapsed] += (long(l[bytes_field]) - prev)
            else:
                num_mb_dict[elapsed] = (long(l[bytes_field]) - prev)
            #print str(elapsed) + " " + str(num_mb_dict[elapsed])
            prev = long(l[bytes_field])
            #x.write(str(date_to_i(l[date_field]) - start_time) + \
            #" " + str(((float(l[bytes_field]) - start_mb)/1024)/1024) + "\n")
            #if(fin[names[0]][0] < date_to_i(l[date_field]) and fin[names[0]][1] < float(l[bytes_field])):
            if(fin[names[0]][0] == 0):
                fin[names[0]][0] = l[date_field]
                fin[names[0]][1] = float(l[bytes_field])
            elif((int(secondsDiff(fin[names[0]][0],l[date_field])) < 0) and fin[names[0]][1] < float(l[bytes_field])):
            #if(fin[names[0]][0] < elapsed and fin[names[0]][1] < float(l[bytes_field])):
                fin[names[0]][0] = l[date_field]
                fin[names[0]][1] = float(l[bytes_field])
        lastNode = names[0]
        start_mb = 0.0
        start_time = 0

        first = True
        f.close();
        count += 1

    x = open("../graphs/" + lastNode + "-data","a");
    total = 0
    #print num_mb_dict
    #print lastNode
    for key in sorted(num_mb_dict.iterkeys()):
        total += num_mb_dict[key]
        #print str(key) + " " + str(total/divide_by)
        x.write(str(key) + " " + str(total/divide_by) + "\n")
    x.close()

    #sys.exit()

    timesort = []
    #print beginning_time
    for node in fin:
        #print fin[node][0]
        timesort.append(int(secondsDiff(fin[node][0],beginning_time)))

    timesort.sort()
    count = 1
    x = open("../graphs/comp-time","a")
    x.write("0 0\n")
    start_time = 0
    for time in timesort:
        if count == 1:
            start_time = time
        #x.write(str(time - start_time) + " " + str(count) + "\n")
        x.write(str(time) + " " + str(count) + "\n")
        count += 1
    x.close()

    print "Success"

def secondsDiff(date1, date2):
    FMT = '%H:%M:%S.%f'
    tdelta = datetime.strptime(date1, FMT) - datetime.strptime(date2, FMT)
    return tdelta.total_seconds()

def date_to_i(date):
    date = date.split(".")[0]
    x = time.strptime(date.split(',')[0],'%H:%M:%S')
    t = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    return t

if __name__ == "__main__":
    main()
