VBoxManage modifyvm "Ubuntu-Test" --nic2 intnet
VBoxManage modifyvm "Ubuntu-Test" --intnet2 "intnet"
VBoxManage startvm "Ubuntu-Test"
VBoxManage modifyvm "Ubuntu-Test2" --nic1 intnet
VBoxManage modifyvm "Ubuntu-Test2" --intnet1 "intnet"
VBoxManage modifyvm "Ubuntu-Test2" --nic2 intnet
VBoxManage modifyvm "Ubuntu-Test2" --intnet2 "intnet2"
VBoxManage startvm "Ubuntu-Test2"
VBoxManage modifyvm "Ubuntu-Test3" --nic1 intnet
VBoxManage modifyvm "Ubuntu-Test3" --intnet1 "intnet2"
VBoxManage modifyvm "Ubuntu-Test3" --nic2 intnet
VBoxManage modifyvm "Ubuntu-Test3" --intnet2 "intnet3"
VBoxManage startvm "Ubuntu-Test3"
VBoxManage modifyvm "Ubuntu-Test4" --nic1 intnet
VBoxManage modifyvm "Ubuntu-Test4" --intnet1 "intnet3"
VBoxManage modifyvm "Ubuntu-Test4" --nic2 intnet
VBoxManage modifyvm "Ubuntu-Test4" --intnet2 "intnet4"
VBoxManage startvm "Ubuntu-Test4"
#VBoxManage modifyvm "Ubuntu-Test5" --nic1 intnet
#VBoxManage modifyvm "Ubuntu-Test5" --intnet1 "intnet4"
#VBoxManage startvm "Ubuntu-Test5"
#VBoxManage dhcpserver add --netname intnet --ip 192.168.4.0 --netmask 255.255.255.0 --lowerip 192.168.4.1 --upperip 192.168.4.10
