vm1_name="Ubuntu-Hoon"
vm2_name="Ubuntu-Test2"
vm3_name="Ubuntu-Test4"
vm4_name="Ubuntu-Spheros"
intnet1="lion"
intnet2="tiger"
intnet3="cat"
intnet4="dog"
intnet5="fish"
intnet6="kiwi"
if [ $1 == "line" ]; then
    echo "Line"
    VBoxManage modifyvm $vm1_name --nic1 bridged
    VBoxManage modifyvm $vm1_name --nic2 intnet
    VBoxManage modifyvm $vm1_name --intnet2 $intnet1
    VBoxManage modifyvm $vm1_name --nic3 none
    VBoxManage modifyvm $vm1_name --nic4 none
    VBoxManage startvm $vm1_name
    VBoxManage modifyvm $vm2_name --nic1 bridged
    VBoxManage modifyvm $vm2_name --nic2 intnet
    VBoxManage modifyvm $vm2_name --intnet2 $intnet1
    VBoxManage modifyvm $vm2_name --nic3 intnet
    VBoxManage modifyvm $vm2_name --intnet3 $intnet2
    VBoxManage modifyvm $vm2_name --nic4 none
    VBoxManage startvm $vm2_name
    VBoxManage modifyvm $vm3_name --nic1 bridged
    VBoxManage modifyvm $vm3_name --nic2 intnet
    VBoxManage modifyvm $vm3_name --intnet2 $intnet2
    VBoxManage modifyvm $vm3_name --nic3 intnet
    VBoxManage modifyvm $vm3_name --intnet3 $intnet3
    VBoxManage modifyvm $vm3_name --nic4 none
    VBoxManage startvm $vm3_name
    VBoxManage modifyvm $vm4_name --nic1 bridged
    VBoxManage modifyvm $vm4_name --nic2 intnet
    VBoxManage modifyvm $vm4_name --intnet2 $intnet3
    VBoxManage modifyvm $vm4_name --nic3 none
    VBoxManage modifyvm $vm4_name --nic4 none
    VBoxManage startvm $vm4_name
elif [ $1 == "circle" ]; then
    echo "Circle"
    VBoxManage modifyvm $vm1_name --nic1 bridged
    VBoxManage modifyvm $vm1_name --nic2 intnet
    VBoxManage modifyvm $vm1_name --intnet2 $intnet1
    VBoxManage modifyvm $vm1_name --nic3 intnet
    VBoxManage modifyvm $vm1_name --intnet3 $intnet4
    VBoxManage modifyvm $vm1_name --nic4 none
    VBoxManage startvm $vm1_name
    VBoxManage modifyvm $vm2_name --nic1 bridged
    VBoxManage modifyvm $vm2_name --nic2 intnet
    VBoxManage modifyvm $vm2_name --intnet2 $intnet1
    VBoxManage modifyvm $vm2_name --nic3 intnet
    VBoxManage modifyvm $vm2_name --intnet3 $intnet2
    VBoxManage modifyvm $vm2_name --nic4 none
    VBoxManage startvm $vm2_name
    VBoxManage modifyvm $vm3_name --nic1 bridged
    VBoxManage modifyvm $vm3_name --nic2 intnet
    VBoxManage modifyvm $vm3_name --intnet2 $intnet2
    VBoxManage modifyvm $vm3_name --nic3 intnet
    VBoxManage modifyvm $vm3_name --intnet3 $intnet3
    VBoxManage modifyvm $vm3_name --nic4 none
    VBoxManage startvm $vm3_name
    VBoxManage modifyvm $vm4_name --nic1 bridged
    VBoxManage modifyvm $vm4_name --nic2 intnet
    VBoxManage modifyvm $vm4_name --intnet2 $intnet3
    VBoxManage modifyvm $vm4_name --nic3 intnet
    VBoxManage modifyvm $vm4_name --intnet3 $intnet4
    VBoxManage modifyvm $vm4_name --nic4 none
    VBoxManage startvm $vm4_name
elif [ $1 == "mesh" ]; then
    echo "Connected Mesh"
    VBoxManage modifyvm $vm1_name --nic1 bridged
    VBoxManage modifyvm $vm1_name --nic2 intnet
    VBoxManage modifyvm $vm1_name --intnet2 $intnet1
    VBoxManage modifyvm $vm1_name --nic3 intnet
    VBoxManage modifyvm $vm1_name --intnet3 $intnet4
    VBoxManage modifyvm $vm1_name --nic4 intnet
    VBoxManage modifyvm $vm1_name --intnet4 $intnet5
    VBoxManage startvm $vm1_name
    VBoxManage modifyvm $vm2_name --nic1 bridged
    VBoxManage modifyvm $vm2_name --nic2 intnet
    VBoxManage modifyvm $vm2_name --intnet2 $intnet1
    VBoxManage modifyvm $vm2_name --nic3 intnet
    VBoxManage modifyvm $vm2_name --intnet3 $intnet2
    VBoxManage modifyvm $vm2_name --nic4 intnet
    VBoxManage modifyvm $vm2_name --intnet4 $intnet6
    VBoxManage startvm $vm2_name
    VBoxManage modifyvm $vm3_name --nic1 bridged
    VBoxManage modifyvm $vm3_name --nic2 intnet
    VBoxManage modifyvm $vm3_name --intnet2 $intnet2
    VBoxManage modifyvm $vm3_name --nic3 intnet
    VBoxManage modifyvm $vm3_name --intnet3 $intnet3
    VBoxManage modifyvm $vm3_name --nic4 intnet
    VBoxManage modifyvm $vm3_name --intnet4 $intnet5
    VBoxManage startvm $vm3_name
    VBoxManage modifyvm $vm4_name --nic1 bridged
    VBoxManage modifyvm $vm4_name --nic2 none
    VBoxManage modifyvm $vm4_name --intnet2 $intnet3
    VBoxManage modifyvm $vm4_name --nic3 intnet
    VBoxManage modifyvm $vm4_name --intnet3 $intnet4
    VBoxManage modifyvm $vm4_name --nic4 intnet
    VBoxManage modifyvm $vm4_name --intnet4 $intnet6
    VBoxManage startvm $vm4_name
elif [ $1 == "odd" ]; then
    echo "Odd"
    VBoxManage modifyvm $vm1_name --nic1 bridged
    VBoxManage modifyvm $vm1_name --nic2 intnet
    VBoxManage modifyvm $vm1_name --intnet2 $intnet1
    VBoxManage modifyvm $vm1_name --nic3 intnet
    VBoxManage modifyvm $vm1_name --intnet3 $intnet4
    VBoxManage modifyvm $vm1_name --nic4 none
    VBoxManage startvm $vm1_name
    VBoxManage modifyvm $vm2_name --nic1 bridged
    VBoxManage modifyvm $vm2_name --nic2 intnet
    VBoxManage modifyvm $vm2_name --intnet2 $intnet1
    VBoxManage modifyvm $vm2_name --nic3 intnet
    VBoxManage modifyvm $vm2_name --intnet3 $intnet2
    VBoxManage modifyvm $vm2_name --nic4 intnet
    VBoxManage modifyvm $vm2_name --intnet4 $intnet6
    VBoxManage startvm $vm2_name
    VBoxManage modifyvm $vm3_name --nic1 bridged
    VBoxManage modifyvm $vm3_name --nic2 intnet
    VBoxManage modifyvm $vm3_name --intnet2 $intnet2
    VBoxManage modifyvm $vm3_name --nic3 intnet
    VBoxManage modifyvm $vm3_name --intnet3 $intnet3
    VBoxManage modifyvm $vm3_name --nic4 none
    VBoxManage startvm $vm3_name
    VBoxManage modifyvm $vm4_name --nic1 bridged
    VBoxManage modifyvm $vm4_name --nic2 none
    VBoxManage modifyvm $vm4_name --intnet2 $intnet3
    VBoxManage modifyvm $vm4_name --nic3 intnet
    VBoxManage modifyvm $vm4_name --intnet3 $intnet4
    VBoxManage modifyvm $vm4_name --nic4 intnet
    VBoxManage modifyvm $vm4_name --intnet4 $intnet6
    VBoxManage startvm $vm4_name
fi
