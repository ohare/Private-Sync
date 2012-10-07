import subprocess, datetime, socket, argparse

#########################
#                       #
#   Read Network Data   #
#     Calum O'Hare      #
#         2012          #
#                       #
#########################

homepath = "/home/cal/Documents/Private-Sync/"
#homepath = "/Users/calum/Documents/Private-Sync/"

parser = argparse.ArgumentParser()
parser.add_argument('-i',action="store",dest='ip',help='IP address to record for')
parser.add_argument('-f',action="store",dest='fold',help='Folder to record for')

interfacenames = []

w = open(homepath + "whoami","r")
nodename = w.read()
nodename = nodename[0]
w.close()

#Get my ip corresponding to the interface with ipaddr
def getMyIP(ipaddr):
    route = subprocess.check_output("ip route get " + ipaddr,shell=True)
    words = route.split()
    interface = ""
    for word in words:
        if word.startswith("eth"):
            interface = word
            #print interface
            break
    ifconf = subprocess.check_output("ifconfig " + interface,shell=True)
    words = ifconf.split()
    now = False
    for word in words:
        if word == "inet":
            now = True
        elif now:
            word = word.split(":")
            #print word[1]
            return word[1]

#Log interface coresponding to ipaddr(*@\label{lst:log_ip}@*)
def logIPtraffic(ipaddr, folder):
    route = subprocess.check_output("ip route get " + ipaddr,shell=True)
    words = route.split()
    interface = ""
    for word in words:
        if word.startswith("eth"):
            interface = word
            #print interface
            break
    writeIface(interface, folder)

#Write the upload/download data for a given interface and folder
def writeIface(iface, folder):
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
                        f = open(homepath + "log/" \
                        + "node" + nodename.upper() + "-" \
                        + iface + ".log",'a')
                        f.write("#D " + folder + "\n")
                        f.write(str(datetime.datetime.now()) + " " + interfacename + " download: " + str(download) + " upload: " + str(upload) + "\n")
                        f.close()
                    count = 0
        elif(interface):
            if(split == "RX" or split == "TX"):
                nex = split

#Log all interfaces(*@\label{lst:log_all}@*)
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
                    f = open(homepath + "log/" \
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
        logIPtraffic(args.ip, args.fold)
        #getMyIP(args.ip)
    else:
        pass
        main()
