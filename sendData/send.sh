vm_addr_arr=("192.168.0.28" "192.168.0.27" "192.168.0.30" "192.168.0.14")
path=/home/cal/Documents
name=t23
i=0
echo "ssh cal@${vm_addr_arr[$i]} \"mkdir /tmp/${name}\""
ssh cal@${vm_addr_arr[$i]} "mkdir /tmp/${name}"
echo "Starting one"
echo "scp rten /tmp/${name}/"
scp rten cal@${vm_addr_arr[$i]}:/tmp/${name}/
ssh cal@${vm_addr_arr[$i]} "mv /tmp/${name}/rten ${path}/${name}/"
sleep 10
echo "Starting two"
scp rten2 cal@${vm_addr_arr[$i]}:/tmp/${name}/
ssh cal@${vm_addr_arr[$i]} "mv /tmp/${name}/rten2 ${path}/${name}/"
sleep 10
echo "Starting three"
scp rten3 cal@${vm_addr_arr[$i]}:/tmp/${name}/
ssh cal@${vm_addr_arr[$i]} "mv /tmp/${name}/rten3 ${path}/${name}/"
ssh cal@${vm_addr_arr[$i]} "rmdir /tmp/${name}"
