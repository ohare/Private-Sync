vm_addr_arr=("192.168.0.26" "192.168.0.22" "192.168.0.19" "192.168.0.14")
path=/home/cal/Documents
name=t01
i=1
echo "Starting one"
ssh ${vm_name_arr[$i]} "mkdir /tmp/${name}"
scp rten /tmp/${name}/
ssh ${vm_name_arr[$i]} "mv /tmp/${name}/* ${path}/${name}/"
sleep 10
echo "Starting two"
ssh ${vm_name_arr[$i]} "mkdir /tmp/${name}"
scp rten2 /tmp/${name}/
ssh ${vm_name_arr[$i]} "mv /tmp/${name}/* ${path}/${name}/"
sleep 10
echo "Starting three"
ssh ${vm_name_arr[$i]} "mkdir /tmp/${name}"
scp rten3 /tmp/${name}/
ssh ${vm_name_arr[$i]} "mv /tmp/${name}/* ${path}/${name}/"
