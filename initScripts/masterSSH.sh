vm1_address=192.168.0.17
vm2_address=192.168.0.12
vm3_address=192.168.0.13
vm4_address=192.168.0.14
if [ $1 == "line" ]; then
    echo "Line"
    ssh cal@${vm1_address} 'sudo /sbin/ifconfig eth1 192.168.2.1 netmask 255.255.255.0 up'
    ssh cal@${vm2_address} 'sudo /sbin/ifconfig eth1 192.168.2.2 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth2 192.168.3.1 netmask 255.255.255.0 up'
    ssh cal@${vm3_address} 'sudo /sbin/ifconfig eth1 192.168.3.2 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth2 192.168.4.1 netmask 255.255.255.0 up'
    ssh cal@${vm4_address} 'sudo /sbin/ifconfig eth1 192.168.4.2 netmask 255.255.255.0 up'
    scp folderopts/line1 cal@${vm1_address}:/home/cal/Documents/Private-Sync/folderstowatch
    scp folderopts/line2 cal@${vm2_address}:/home/cal/Documents/Private-Sync/folderstowatch
    scp folderopts/line3 cal@${vm3_address}:/home/cal/Documents/Private-Sync/folderstowatch
    scp folderopts/line4 cal@${vm4_address}:/home/cal/Documents/Private-Sync/folderstowatch
    neato -Tpng graphs/line > graphs/line-graph.png
elif [ $1 == "circle" ]; then
    echo "Circle"
    ssh cal@${vm1_address} 'sudo /sbin/ifconfig eth1 192.168.2.1 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth2 192.168.5.2 netmask 255.255.255.0 up'
    ssh cal@${vm2_address} 'sudo /sbin/ifconfig eth1 192.168.2.2 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth2 192.168.3.1 netmask 255.255.255.0 up'
    ssh cal@${vm3_address} 'sudo /sbin/ifconfig eth1 192.168.3.2 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth2 192.168.4.1 netmask 255.255.255.0 up'
    ssh cal@${vm4_address} 'sudo /sbin/ifconfig eth1 192.168.4.2 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth2 192.168.5.1 netmask 255.255.255.0 up'
    scp folderopts/circ1 cal@${vm1_address}:/home/cal/Documents/Private-Sync/folderstowatch
    scp folderopts/circ2 cal@${vm2_address}:/home/cal/Documents/Private-Sync/folderstowatch
    scp folderopts/circ3 cal@${vm3_address}:/home/cal/Documents/Private-Sync/folderstowatch
    scp folderopts/circ4 cal@${vm4_address}:/home/cal/Documents/Private-Sync/folderstowatch
    neato -Tpng graphs/circ > graphs/circ-graph.png
elif [ $1 == "mesh" ]; then
    echo "Connected Mesh"
    ssh cal@${vm1_address} 'sudo /sbin/ifconfig eth1 192.168.2.1 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth2 192.168.5.2 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth3 192.168.6.1 netmask 255.255.255.0 up'
    ssh cal@${vm2_address} 'sudo /sbin/ifconfig eth1 192.168.2.2 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth2 192.168.3.1 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth3 192.168.7.1 netmask 255.255.255.0 up'
    ssh cal@${vm3_address} 'sudo /sbin/ifconfig eth1 192.168.3.2 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth2 192.168.4.1 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth3 192.168.6.2 netmask 255.255.255.0 up'
    ssh cal@${vm4_address} 'sudo /sbin/ifconfig eth1 192.168.4.2 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth2 192.168.5.1 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth3 192.168.7.2 netmask 255.255.255.0 up'
    scp folderopts/mesh1 cal@${vm1_address}:/home/cal/Documents/Private-Sync/folderstowatch
    scp folderopts/mesh2 cal@${vm2_address}:/home/cal/Documents/Private-Sync/folderstowatch
    scp folderopts/mesh3 cal@${vm3_address}:/home/cal/Documents/Private-Sync/folderstowatch
    scp folderopts/mesh4 cal@${vm4_address}:/home/cal/Documents/Private-Sync/folderstowatch
    neato -Tpng graphs/mesh > graphs/mesh-graph.png
elif [ $1 == "odd" ]; then
    echo "Odd"
    ssh cal@${vm1_address} 'sudo /sbin/ifconfig eth1 192.168.2.1 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth2 192.168.5.2 netmask 255.255.255.0 up'
    ssh cal@${vm2_address} 'sudo /sbin/ifconfig eth1 192.168.2.2 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth2 192.168.3.1 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth3 192.168.7.1 netmask 255.255.255.0 up'
    ssh cal@${vm3_address} 'sudo /sbin/ifconfig eth1 192.168.3.2 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth2 192.168.4.1 netmask 255.255.255.0 up'
    ssh cal@${vm4_address} 'sudo /sbin/ifconfig eth1 192.168.4.2 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth2 192.168.5.1 netmask 255.255.255.0 up; sudo /sbin/ifconfig eth3 192.168.7.2 netmask 255.255.255.0 up'
    scp folderopts/odd1 cal@${vm1_address}:/home/cal/Documents/Private-Sync/folderstowatch
    scp folderopts/odd2 cal@${vm2_address}:/home/cal/Documents/Private-Sync/folderstowatch
    scp folderopts/odd3 cal@${vm3_address}:/home/cal/Documents/Private-Sync/folderstowatch
    scp folderopts/odd4 cal@${vm4_address}:/home/cal/Documents/Private-Sync/folderstowatch
    neato -Tpng graphs/odd > graphs/odd-graph.png
fi
