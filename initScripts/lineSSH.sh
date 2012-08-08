vm1_address=192.168.0.15
vm2_address=192.168.0.12
vm3_address=192.168.0.13
vm4_address=192.168.0.14
#ssh cal@${vm1_address} 'sudo /sbin/ifconfig eth1 192.168.2.1 netmask 255.255.255.0 up'
ssh cal@${vm2_address} 'sudo /sbin/ifconfig eth1 192.168.2.2 netmask 255.255.255.0 up'
ssh cal@${vm2_address} 'sudo /sbin/ifconfig eth2 192.168.3.1 netmask 255.255.255.0 up'
ssh cal@${vm3_address} 'sudo /sbin/ifconfig eth1 192.168.3.2 netmask 255.255.255.0 up'
ssh cal@${vm3_address} 'sudo /sbin/ifconfig eth2 192.168.4.1 netmask 255.255.255.0 up'
ssh cal@${vm4_address} 'sudo /sbin/ifconfig eth1 192.168.4.2 netmask 255.255.255.0 up'
#scp folderopts/linesimp1 ${vm1_address}:/home/cal/Documents/Private-Sync/
scp folderopts/linesimp2 cal@${vm2_address}:/home/cal/Documents/Private-Sync/folderstowatch
scp folderopts/linesimp3 cal@${vm3_address}:/home/cal/Documents/Private-Sync/folderstowatch
scp folderopts/linesimp4 cal@${vm4_address}:/home/cal/Documents/Private-Sync/folderstowatch
