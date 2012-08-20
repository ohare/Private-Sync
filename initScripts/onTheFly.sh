vm_name_arr=("Ubuntu-Cyan" "Ubuntu-Test2" "Ubuntu-Test4" "Ubuntu-Spheros" "Ubuntu-Hoon")
intnetarr=("lion" "tiger" "cat" "dog" "fish" "kiwi")
letterarr=("a" "b" "c" "d" "e" "f" "g")
ifcountarr=(2 2 2 2 2 2 2 2 2)
incount=1

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
    #VBoxManage modifyvm $1 --nic$3 intnet
    echo "VBoxManage modifyvm $1 --nic$3 intnet"
    #VBoxManage modifyvm $1 --intnet$3 $2
    echo "VBoxManage modifyvm $1 --intnet$3 $2"
}

while read line         
do         
    first=$(echo "$line" | awk '{print $1}')
    last=$(echo "$line" | awk '{print $(NF)}' | sed 's/[;]//g')
    #echo "$first and $last"
    index=$(search_letters $first)
    if [ "$index" = "None" ]; then
        #echo "NPT"
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

