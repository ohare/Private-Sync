import glob, os, time, sys, argparse
from datetime import datetime
from operator import attrgetter

parser = argparse.ArgumentParser()
parser.add_argument("-d","--dir",action="store_true",help="Generate data based on directories")
parser.add_argument("-a","--all",action="store_true",help="Generate data for all traffic on nodes")
args = parser.parse_args()

divide_by = 1024 * 1024
#divide_by = 1

class dataPoint:
    def __init__(self, time, data, path):
        self.time = time
        self.data = data
        self.path = path
    def __repr__(self):
        return repr((self.time, self.data, self.path))
    def getTime(self):
        return self.time
    def getData(self):
        return self.data
    def getPath(self):
        return self.path

def outputData(dataPoints_list, lastNode, namedirs, outputType):
    total = 0
    dataList = sorted(dataPoints_list, key=lambda dataPoint: dataPoint.time)
    for data in dataList:
        if outputType == "individual":
            x = open("../graphs/" + lastNode + "-data-" + str(namedirs[data.getPath()]),"a");
        elif outputType == "combined":
            x = open("../graphs/nodeCombDir-data-" + str(namedirs[data.getPath()]),"a");
        total += data.getData()
        x.write(str(data.getTime()) + " " + str(total/divide_by) + "\n")
        x.close()

def dataPerDirNode():
    first = True
    start_time = 0
    start_mb = 0
    max_mb = 0
    max_name = ""

    dircount = 1
    namedirs = {}
    curDir = ""

    count = 1
    bytes_field = 4
    date_field = 1
    fin = {'nodeA':[0,0],'nodeB':[0,0],'nodeC':[0,0],'nodeD':[0,0]}
    lastNode = ""
    num_mb_dict = {}
    beginning_time = -1
    firstRun = True
    dataPoints_list = []
    allDataPoints_list = []
    for files in glob.glob("*"):
        #print files
        #if files == max_name:
        names = files.split("-")
        f = open(files,"r");
        if names[0] == lastNode:
            pass
        else:
            if not firstRun:
                #print lastNode
                #total = 0
                outputData(dataPoints_list,lastNode,namedirs,"individual")

                num_mb_dict = {}
                dataPoints_list = []
            else:
                firstRun = False
        prev = 0
        num_mb_dict = {}
        for line in f:
            l = line.split()
            if l[0] == '#D':
                if l[1] not in namedirs.keys():
                    print str(l[1]) + " not in namedir keys dircount = " + str(dircount)
                    namedirs[l[1]] = dircount
                    dircount += 1
                curDir = l[1]
            elif l[0] != '#':
                #print line
                if first:
                    first = False
                    start_time = l[date_field]
                    start_mb = long(l[bytes_field])
                    prev = start_mb
                    if beginning_time == -1:
                        beginning_time = l[date_field]
                    elif int(secondsDiff(beginning_time,l[date_field])) > 0:
                        beginning_time = l[date_field]
                #elapsed = int(secondsDiff(l[date_field],start_time))
                elapsed = int(secondsDiff(l[date_field],beginning_time))
                #print elapsed

                if elapsed in num_mb_dict:
                    num_mb_dict[elapsed] += (long(l[bytes_field]) - prev)
                else:
                    num_mb_dict[elapsed] = long(l[bytes_field]) - prev
                
                dataPoints_list.append(dataPoint(elapsed,long(l[bytes_field]) - prev, curDir))
                allDataPoints_list.append(dataPoint(elapsed,long(l[bytes_field]) - prev, curDir))
                prev = long(l[bytes_field])

                if(fin[names[0]][0] == 0):
                    fin[names[0]][0] = l[date_field]
                    fin[names[0]][1] = float(l[bytes_field])
                elif((int(secondsDiff(fin[names[0]][0],l[date_field])) < 0) and fin[names[0]][1] < float(l[bytes_field])):
                    fin[names[0]][0] = l[date_field]
                    fin[names[0]][1] = float(l[bytes_field])
        lastNode = names[0]
        start_mb = 0.0
        start_time = 0

        first = True
        f.close();
        count += 1

    outputData(dataPoints_list,lastNode,namedirs,"individual")

    outputData(allDataPoints_list,lastNode,namedirs,"combined")

    timesort = []
    #print beginning_time
    for node in fin:
        #print fin[node][0]
        timesort.append(int(secondsDiff(fin[node][0],beginning_time)))

    timesort.sort()
    count = 1
    x = open("../graphs/node-comp-time","a")
    x.write("0 0\n")
    start_time = 0
    for time in timesort:
        if count == 1:
            start_time = time
        #x.write(str(time - start_time) + " " + str(count) + "\n")
        x.write(str(time) + " " + str(count) + "\n")
        count += 1
    x.close()

    print "Dir data success"

def dataPerNode():
    first = True
    start_time = 0
    start_mb = 0
    max_mb = 0
    max_name = ""

    divide_by = 1024 * 1024
    #print divide_by
    #divide_by = 1

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

    beginning_time = -1

    #os.chdir("./logs")
    count = 1
    bytes_field = 4
    date_field = 1
    fin = {'nodeA':[0,0],'nodeB':[0,0],'nodeC':[0,0],'nodeD':[0,0]}
    lastNode = ""
    num_mb_dict = {}
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
            l = line.split()
            #print line
            if l[0][0] != '#':
                if first:
                    first = False
                    start_time = l[date_field]
                    start_mb = long(l[bytes_field])
                    prev = start_mb
                    if beginning_time == -1:
                        beginning_time = l[date_field]
                    elif int(secondsDiff(beginning_time,l[date_field])) > 0:
                        beginning_time = l[date_field]
                    #print beginning_time
                #elapsed = int(secondsDiff(l[date_field],start_time))
                elapsed = int(secondsDiff(l[date_field],beginning_time))
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
    x = open("../graphs/node-comp-time","a")
    x.write("0 0\n")
    start_time = 0
    for time in timesort:
        if count == 1:
            start_time = time
        #x.write(str(time - start_time) + " " + str(count) + "\n")
        x.write(str(time) + " " + str(count) + "\n")
        count += 1
    x.close()

    print "Node data success"

def main():
    pass

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
    os.chdir("./logs")
    if args.dir:
        dataPerDirNode() 
        dataPerNode()
    elif args.all:
        dataPerNode()
    else:
        print "You forgot the flag"
