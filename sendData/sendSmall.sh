vm_addr_arr=("192.168.0.28" "192.168.0.27" "192.168.0.19" "192.168.0.14")
path=/home/cal/Documents
name=t18
i=0
wait=3
echo "Starting one"
echo "ssh cal@${vm_addr_arr[$i]} \"date >> ${path}/${name}/smallchange\""
ssh cal@${vm_addr_arr[$i]} "date >> ${path}/${name}/smallchange"
sleep ${wait}
echo "Starting two"
echo "ssh cal@${vm_addr_arr[$i]} \"date >> ${path}/${name}/smallchange\""
ssh cal@${vm_addr_arr[$i]} "date >> ${path}/${name}/smallchange"
sleep ${wait}
echo "Starting three"
echo "ssh cal@${vm_addr_arr[$i]} \"date >> ${path}/${name}/smallchange\""
ssh cal@${vm_addr_arr[$i]} "date >> ${path}/${name}/smallchange"
sleep ${wait}
echo "Starting four"
echo "ssh cal@${vm_addr_arr[$i]} \"date >> ${path}/${name}/smallchange\""
ssh cal@${vm_addr_arr[$i]} "date >> ${path}/${name}/smallchange"
sleep ${wait}
echo "Starting five"
echo "ssh cal@${vm_addr_arr[$i]} \"date >> ${path}/${name}/smallchange\""
ssh cal@${vm_addr_arr[$i]} "date >> ${path}/${name}/smallchange"
#sleep ${wait}
#echo "Starting six"
#echo "ssh cal@${vm_addr_arr[$i]} \"date >> ${path}/${name}/smallchange\""
#ssh cal@${vm_addr_arr[$i]} "date >> ${path}/${name}/smallchange"
#sleep ${wait}
#echo "Starting seven"
#echo "ssh cal@${vm_addr_arr[$i]} \"date >> ${path}/${name}/smallchange\""
#ssh cal@${vm_addr_arr[$i]} "date >> ${path}/${name}/smallchange"
#sleep ${wait}
#echo "Starting eight"
#echo "ssh cal@${vm_addr_arr[$i]} \"date >> ${path}/${name}/smallchange\""
#ssh cal@${vm_addr_arr[$i]} "date >> ${path}/${name}/smallchange"
#sleep ${wait}
#echo "Starting nine"
#echo "ssh cal@${vm_addr_arr[$i]} \"date >> ${path}/${name}/smallchange\""
#ssh cal@${vm_addr_arr[$i]} "date >> ${path}/${name}/smallchange"
#sleep ${wait}
#echo "Starting ten"
#echo "ssh cal@${vm_addr_arr[$i]} \"date >> ${path}/${name}/smallchange\""
#ssh cal@${vm_addr_arr[$i]} "date >> ${path}/${name}/smallchange"
