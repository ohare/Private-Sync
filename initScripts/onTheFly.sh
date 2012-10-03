vm_name_arr=("Ubuntu-Pool" "Ubuntu-Silence" "Ubuntu-Black" "Ubuntu-Spheros" "Ubuntu-Wild")
vm_addr_arr=("192.168.0.28" "192.168.0.27" "192.168.0.30" "192.168.0.14")
#Wild = 19
intnetarr=("lion" "tiger" "cat" "dog" "fish" "kiwi" "swish" "boom" "roar")
#These should all be in one big dictionary apart from inet names
letterarr=("a" "b" "c" "d" "e" "f" "g" "h" "i" "j")
ifcountarr=(2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2)
ethcountarr=(1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1)
incount=1
bigncount=2
littlencount=1
folderpath="/home/cal/Documents/t14"
folderpath2="/home/cal/Documents/t02"
homepath="/home/cal/Documents/Private-Sync/"
waitTime=10

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
        ssh cal@${vm_addr_arr[$i]} "echo \"#Local folder path to watch, host to copy to, remote dir to copy to, min time between syncs\" > /home/cal/Documents/Private-Sync/folderstowatch; echo ${letterarr[$i]} > /home/cal/Documents/Private-Sync/whoami"
        let "i++"
    done
}

function git_pull() {
    i=0
    while [ "$i" -lt "${#vm_addr_arr[@]}" ]; do
        echo "ssh cal@${vm_addr_arr[$i]} \"cd /home/cal/Documents/Private-Sync; git pull origin master\""
        ssh cal@${vm_addr_arr[$i]} "cd /home/cal/Documents/Private-Sync; git pull origin master"
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
    echo "VBoxManage modifyvm $1 --nic$3 intnet"
    VBoxManage modifyvm $1 --nic$3 intnet
    echo "VBoxManage modifyvm $1 --intnet$3 $2"
    VBoxManage modifyvm $1 --intnet$3 $2
}

function gatherLogs {
    index=0
    while [ "$index" -lt "${#vm_addr_arr[@]}" ]; do
        echo "scp cal@${vm_addr_arr[$index]}:/home/cal/Documents/Private-Sync/log/* ../logs/"
        scp cal@${vm_addr_arr[$index]}:/home/cal/Documents/Private-Sync/log/* ../logs/
        let "index++"
    done
}

function clean {
    index=0
    while [ "$index" -lt "${#vm_addr_arr[@]}" ]; do
        echo "ssh cal@${vm_addr_arr[$index]} \"rm ${homepath}log/*; rm ${homepath}Stop-*; rm ${homepath}folders.dat\""
        ssh cal@${vm_addr_arr[$index]} "rm ${homepath}log/*; rm ${homepath}Stop-*; rm ${homepath}folders.dat"
        let "index++"
    done
}

function cleanFold {
    index=0
    while [ "$index" -lt "${#vm_addr_arr[@]}" ]; do
        echo "ssh cal@${vm_addr_arr[$index]} \"rm -rf ${folderpath}/*;\""
        ssh cal@${vm_addr_arr[$index]} "rm -rf ${folderpath}/*;"
        let "index++"
    done
}

function sendKeys {
    index=0
    while [ "$index" -lt "${#vm_addr_arr[@]}" ]; do
        #ssh cal@${vm_addr_arr[$index]} "rm /home/cal/.ssh/authorized_keys"
        for file in /Users/calum/.ssh/*.pub; do
            #echo "$file"
            echo "cat $file | ssh cal@${vm_addr_arr[$index]} \"cat >> /home/cal/.ssh/authorized_keys\""
            cat $file | ssh cal@${vm_addr_arr[$index]} "cat >> /home/cal/.ssh/authorized_keys"
        done
        let "index++"
    done
    #for file in /Users/calum/.ssh/*.pub; do
    #    echo "$file"
    #    cat $file | ssh cal@192.168.0.17 "cat >> /home/cal/.ssh/testfile"
    #    echo "cat $file | ssh cal@192.168.0.17 \"cat >> /home/cal/.ssh/testfile\""
    #done
}

function ifconf {
    echo "ssh cal@$1 'sudo /sbin/ifconfig eth$2 192.168.$3.$4 netmask 255.255.255.0 up; echo \"$folderpath 192.168.$3.$5 /home/cal/Documents/ $waitTime\" >> /home/cal/Documents/Private-Sync/folderstowatch'"
    ssh cal@$1 "sudo /sbin/ifconfig eth$2 192.168.$3.$4 netmask 255.255.255.0 up; echo \"$folderpath 192.168.$3.$5 /home/cal/Documents/ $waitTime\" >> /home/cal/Documents/Private-Sync/folderstowatch" < /dev/null
}

function ifconf2 {
    echo "ssh cal@$1 \"sudo /sbin/ifconfig eth$2 192.168.$3.$4 netmask 255.255.255.0 up; echo \"$folderpath 192.168.$3.$5 /home/cal/Documents/ *\" >> /home/cal/Documents/Private-Sync/folderstowatch; echo \"$folderpath2 192.168.$3.$5 /home/cal/Documents/ *\" >> /home/cal/Documents/Private-Sync/folderstowatch\" < /dev/null"
    ssh cal@$1 "sudo /sbin/ifconfig eth$2 192.168.$3.$4 netmask 255.255.255.0 up; echo \"$folderpath 192.168.$3.$5 /home/cal/Documents/ *\" >> /home/cal/Documents/Private-Sync/folderstowatch; echo \"$folderpath2 192.168.$3.$5 /home/cal/Documents/ *\" >> /home/cal/Documents/Private-Sync/folderstowatch" < /dev/null
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
elif [ $2 == "if2" ]; then
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
            ifconf2 ${vm_addr_arr[$index]} ${ethcountarr[$index]} $bigncount $littlencount $(( $littlencount+1 ))
            #echo "in: $index"
            (( ethcountarr[$index]++ ))
            (( littlencount++ ))
            index=$(search_letters $last)
            ifconf2 ${vm_addr_arr[$index]} ${ethcountarr[$index]} $bigncount $littlencount $(( $littlencount-1 ))
            #echo "in: $index"
            (( ethcountarr[$index]++ ))
            incount=$incount+1
            (( bigncount++ ))
            (( littlencount-- ))
        fi
    done <graphs/$1
elif [ $2 == "key" ]; then
    sendKeys
elif [ $2 == "gather" ]; then
    gatherLogs
elif [ $2 == "clean" ]; then
    clean
elif [ $2 == "pull" ]; then
    git_pull
elif [ $2 == "clean-fold" ]; then
    cleanFold
elif [ $2 == "help" ]; then
    echo "vm          - setup vm networking"
    echo "if          - setup network addresses etc for each vm"
    echo "if2         - setup network addresses etc for each vm for two folders"
    echo "gather      - gather the logs in"
    echo "clean       - clean out the logs/config files"
    echo "clean-fold  - clean out the files folder"
    echo "pull        - pull the latest code from the repository to each vm"
    echo "help        - display this help message"
else
    echo "Oops try again"
fi

neato -Teps graphs/$1 > graphs/$1-graph.eps
