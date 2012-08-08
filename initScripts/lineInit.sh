vm1_name="Ubuntu-Test"
vm2_name="Ubuntu-Test2"
vm3_name="Ubuntu-Test4"
vm4_name="Ubuntu-Spheros"
intnet1="lion"
intnet2="tiger"
intnet3="cat"
VBoxManage modifyvm $vm1_name --nic1 none
VBoxManage modifyvm $vm1_name --nic1 bridged
VBoxManage modifyvm $vm1_name --nic2 none
VBoxManage modifyvm $vm1_name --nic2 intnet
VBoxManage modifyvm $vm1_name --intnet2 $intnet1
VBoxManage startvm $vm1_name
VBoxManage modifyvm $vm2_name --nic1 none
VBoxManage modifyvm $vm2_name --nic1 bridged
VBoxManage modifyvm $vm2_name --nic2 none
VBoxManage modifyvm $vm2_name --nic2 intnet
VBoxManage modifyvm $vm2_name --intnet2 $intnet1
VBoxManage modifyvm $vm2_name --nic3 none
VBoxManage modifyvm $vm2_name --nic3 intnet
VBoxManage modifyvm $vm2_name --intnet3 $intnet2
VBoxManage startvm $vm2_name
VBoxManage modifyvm $vm3_name --nic1 none
VBoxManage modifyvm $vm3_name --nic1 bridged
VBoxManage modifyvm $vm3_name --nic2 intnet
VBoxManage modifyvm $vm3_name --intnet2 $intnet2
VBoxManage modifyvm $vm3_name --nic3 intnet
VBoxManage modifyvm $vm3_name --intnet3 $intnet3
VBoxManage startvm $vm3_name
VBoxManage modifyvm $vm4_name --nic1 none
VBoxManage modifyvm $vm4_name --nic1 bridged
VBoxManage modifyvm $vm4_name --nic2 none
VBoxManage modifyvm $vm4_name --nic2 intnet
VBoxManage modifyvm $vm4_name --intnet2 $intnet3
#VBoxManage modifyvm $vm4_name --nic3 intnet
#VBoxManage modifyvm $vm4_name --intnet3 $intnet4
VBoxManage startvm $vm4_name
#VBoxManage dhcpserver add --netname intnet --ip 192.168.4.0 --netmask 255.255.255.0 --lowerip 192.168.4.1 --upperip 192.168.4.10
