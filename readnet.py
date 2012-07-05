import subprocess
import datetime

interfacename = "eth1"

def main():
    output = subprocess.check_output("ifconfig",shell=True)
    splitput = output.split()
    eth3 = False
    nex = ""
    count = 0
    upload = 0
    download = 0
    for split in splitput:
        if(split == interfacename):
            eth3 = True
        elif(nex != ""):
            sp = split.split(":")
            if(sp[0] == "bytes"):
                if(nex == "RX"):
                    download = int(sp[1])
                else:
                    upload = int(sp[1])
                nex = ""
                count += 1
                if(count == 2):
                    eth3 = False
        elif(eth3):
            if(split == "RX" or split == "TX"):
                nex = split

    f = open("/home/cal/Documents/Private-Sync/log/interface.log",'a')
    f.write(str(datetime.datetime.now()) + " " + interfacename + " download: " + str(download) + " upload: " + str(upload) + "\n")
    f.close()

if __name__ == "__main__":
    main()
