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
VBoxManage modifyvm "Lubuntu-Three" --nic2 intnet
VBoxManage modifyvm "Lubuntu-Three" --intnet2 "intnet3"
VBoxManage startvm "Lubuntu-Three"
VBoxManage modifyvm "Lubuntu-Four" --nic1 intnet
VBoxManage modifyvm "Lubuntu-Four" --intnet1 "intnet3"
VBoxManage modifyvm "Lubuntu-Four" --nic2 intnet
VBoxManage modifyvm "Lubuntu-Four" --intnet2 "intnet4"
VBoxManage startvm "Lubuntu-Four"
VBoxManage modifyvm "Lubuntu-Five" --nic1 intnet
VBoxManage modifyvm "Lubuntu-Five" --intnet1 "intnet4"
VBoxManage startvm "Lubuntu-Five"
