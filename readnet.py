import subprocess, datetime, socket, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i',action="store",dest='ip',help='IP address to record for')

interfacenames = []

w = open("./whoami","r")
nodename = w.read()
nodename = nodename[0]
w.close()

#Log interface coresponding to ipaddr
def logIPtraffic(ipaddr):
    route = subprocess.check_output("ip route get " + ipaddr,shell=True)
    words = route.split()
    interface = ""
    for word in words:
        if word.startswith("eth"):
            interface = word
            #print interface
            break
    writeIface(interface)

def writeIface(iface):
    ifs = subprocess.check_output("ifconfig -s",shell=True)
    ilines = ifs.split("\n")
    for i in range(1,len(ilines)-1):
	interfacenames.append(ilines[i].split()[0])
    output = subprocess.check_output("ifconfig",shell=True)
    splitput = output.split()
    interface = False
    interfacename = ""
    nex = ""
    count = 0
    upload = 0
    download = 0
    for split in splitput:
        if split in interfacenames:
            interface = True
            interfacename = split
            #print interfacename
        if(nex != ""):
            sp = split.split(":")
            if(sp[0] == "bytes"):
                if(nex == "RX"):
                    download = int(sp[1])
                else:
                    upload = int(sp[1])
                nex = ""
                count += 1
                if(count == 2):
                    interface = False
                    if interfacename == iface:
                        f = open("/home/cal/Documents/Private-Sync/log/" \
                        + "node" + nodename.upper() + "-" \
                        + iface + ".log",'a')
                        f.write(str(datetime.datetime.now()) + " " + interfacename + " download: " + str(download) + " upload: " + str(upload) + "\n")
                        f.close()
                    count = 0
        elif(interface):
            if(split == "RX" or split == "TX"):
                nex = split

#Log all interfaces
def main():
    ifs = subprocess.check_output("ifconfig -s",shell=True)
    ilines = ifs.split("\n")
    for i in range(1,len(ilines)-1):
	interfacenames.append(ilines[i].split()[0])
    output = subprocess.check_output("ifconfig",shell=True)
    splitput = output.split()
    interface = False
    interfacename = ""
    nex = ""
    count = 0
    upload = 0
    download = 0
    for split in splitput:
        if split in interfacenames:
            interface = True
            interfacename = split
            #print interfacename
        if(nex != ""):
            sp = split.split(":")
            if(sp[0] == "bytes"):
                if(nex == "RX"):
                    download = int(sp[1])
                else:
                    upload = int(sp[1])
                nex = ""
                count += 1
                if(count == 2):
                    interface = False
                    f = open("/home/cal/Documents/Private-Sync/log/" \
                    + str(socket.gethostname()) + "-" \
                    + interfacename + ".log",'a')
                    f.write(str(datetime.datetime.now()) + " " + interfacename + " download: " + str(download) + " upload: " + str(upload) + "\n")
                    f.close()
                    count = 0
        elif(interface):
            if(split == "RX" or split == "TX"):
                nex = split

if __name__ == "__main__":
    args = parser.parse_args()
    if args.ip != None:
        logIPtraffic(args.ip)
    else:
        pass
        main()
