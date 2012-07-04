VBoxManage modifyvm "Lubuntu-One" --nic2 intnet
VBoxManage modifyvm "Lubuntu-One" --intnet2 "intnet"
VBoxManage startvm "Lubuntu-One"
VBoxManage modifyvm "Lubuntu-Two" --nic1 intnet
VBoxManage modifyvm "Lubuntu-Two" --intnet1 "intnet"
VBoxManage modifyvm "Lubuntu-Two" --nic2 intnet
VBoxManage modifyvm "Lubuntu-Two" --intnet2 "intnet2"
VBoxManage startvm "Lubuntu-Two"
VBoxManage modifyvm "Lubuntu-Three" --nic1 intnet
VBoxManage modifyvm "Lubuntu-Three" --intnet1 "intnet2"
VBoxManage startvm "Lubuntu-Three"
