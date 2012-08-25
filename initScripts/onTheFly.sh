vm_name_arr=("Ubuntu-Cyan" "Ubuntu-Test2" "Ubuntu-Hoon" "Ubuntu-Spheros" "Ubuntu-Wild")
vm_addr_arr=("192.168.0.17" "192.168.0.12" "192.168.0.15" "192.168.0.14")
intnetarr=("lion" "tiger" "cat" "dog" "fish" "kiwi")
letterarr=("a" "b" "c" "d" "e" "f" "g")
ifcountarr=(2 2 2 2 2 2 2 2 2)
ethcountarr=(1 1 1 1 1 1 1 1 1)
incount=1
bigncount=2
littlencount=1
foldername="ready"

function clear_ifaces() {
    i=0
    while [ "$i" -lt "${#vm_name_arr[@]}" ]; do
        VBoxManage modifyvm ${vm_name_arr[$i]} --nic2 none
        echo "VBoxManage modifyvm ${vm_name_arr[$i]} --nic2 none"
        VBoxManage modifyvm ${vm_name_arr[$i]} --nic3 none
        echo "VBoxManage modifyvm ${vm_name_arr[$i]} --nic3 none"
        VBoxManage modifyvm ${vm_name_arr[$i]} --nic4 none
        echo "VBoxManage modifyvm ${vm_name_arr[$i]} --nic4 none"
        let "i++"
    done
}

function clear_watched_folders() {
    i=0
    while [ "$i" -lt "${#vm_addr_arr[@]}" ]; do
        ssh cal@${vm_addr_arr[$i]} "echo \"#Local folder path to watch, host to copy to, remote dir to copy to\" > /home/cal/Documents/Private-Sync/folderstowatch; echo ${letterarr[$i]} > /home/cal/Documents/Private-Sync/whoami"
        let "i++"
    done
}

function search_letters() {
    index=0
    while [ "$index" -lt "${#letterarr[@]}" ]; do
        if [ "${letterarr[$index]}" = "$1" ]; then
            echo $index
            return
        fi
        let "index++"
    done
    echo "None"
}

function vbmMOD {
    VBoxManage modifyvm $1 --nic$3 intnet
    echo "VBoxManage modifyvm $1 --nic$3 intnet"
    VBoxManage modifyvm $1 --intnet$3 $2
    echo "VBoxManage modifyvm $1 --intnet$3 $2"
}

function ifconf {
    ssh cal@$1 "sudo /sbin/ifconfig eth$2 192.168.$3.$4 netmask 255.255.255.0 up; echo \"/home/cal/Documents/$foldername 192.168.$3.$5 /home/cal/Documents/\" >> /home/cal/Documents/Private-Sync/folderstowatch" < /dev/null
    echo "ssh cal@$1 'sudo /sbin/ifconfig eth$2 192.168.$3.$4 netmask 255.255.255.0 up; echo "/home/cal/Documents/$foldername 192.168.$3.$5 /home/cal/Documents/" >> /home/cal/Documents/Private-Sync/folderstowatch'"
}

if [ $2 == "vm" ]; then
    clear_ifaces

    while read line         
    do         
        first=$(echo "$line" | awk '{print $1}')
        last=$(echo "$line" | awk '{print $(NF)}' | sed 's/[;]//g')
        #echo "$first and $last"
        index=$(search_letters $first)
        if [ "$index" = "None" ]; then
            #echo "None"
            :
        else
            vbmMOD ${vm_name_arr[$index]} ${intnetarr[$incount]} ${ifcountarr[$index]} 
            #echo "in: $index"
            (( ifcountarr[$index]++ ))
            index=$(search_letters $last)
            vbmMOD ${vm_name_arr[$index]} ${intnetarr[$incount]} ${ifcountarr[$index]} 
            #echo "in: $index"
            (( ifcountarr[$index]++ ))
            incount=$incount+1
        fi
    done <graphs/$1
elif [ $2 == "if" ]; then
    clear_watched_folders

    while read line         
    do         
        first=$(echo "$line" | awk '{print $1}')
        last=$(echo "$line" | awk '{print $(NF)}' | sed 's/[;]//g')
        echo "$first and $last"
        index=$(search_letters $first)
        if [ "$index" = "None" ]; then
            #echo "None"
            :
        else
            ifconf ${vm_addr_arr[$index]} ${ethcountarr[$index]} $bigncount $littlencount $(( $littlencount+1 ))
            #echo "in: $index"
            (( ethcountarr[$index]++ ))
            (( littlencount++ ))
            index=$(search_letters $last)
            ifconf ${vm_addr_arr[$index]} ${ethcountarr[$index]} $bigncount $littlencount $(( $littlencount-1 ))
            #echo "in: $index"
            (( ethcountarr[$index]++ ))
            incount=$incount+1
            (( bigncount++ ))
            (( littlencount-- ))
        fi
    done <graphs/$1
fi

neato -Tpng graphs/$1 > graphs/$1-graph.png
