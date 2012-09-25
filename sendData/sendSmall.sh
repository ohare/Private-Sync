vm_addr_arr=("192.168.0.28" "192.168.0.27" "192.168.0.19" "192.168.0.14")
path=/home/cal/Documents
name=t01
i=0
echo "Starting one"
echo "ssh cal@${vm_addr_arr[$i]} \"date >> ${path}/${name}/smallChange.txt\""
ssh cal@${vm_addr_arr[$i]} "date >> ${path}/${name}/smallChange.txt"
sleep 5
echo "Starting two"
echo "ssh cal@${vm_addr_arr[$i]} \"date >> ${path}/${name}/smallChange.txt\""
ssh cal@${vm_addr_arr[$i]} "date >> ${path}/${name}/smallChange.txt"
sleep 5
echo "Starting three"
echo "ssh cal@${vm_addr_arr[$i]} \"date >> ${path}/${name}/smallChange.txt\""
ssh cal@${vm_addr_arr[$i]} "date >> ${path}/${name}/smallChange.txt"
