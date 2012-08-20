vm1_address=192.168.0.17
vm2_address=192.168.0.12
vm3_address=192.168.0.13
vm4_address=192.168.0.14
scp cal@${vm1_address}:/home/cal/Documents/Private-Sync/log/* ./logs/
scp cal@${vm2_address}:/home/cal/Documents/Private-Sync/log/* ./logs/
scp cal@${vm3_address}:/home/cal/Documents/Private-Sync/log/* ./logs/
scp cal@${vm4_address}:/home/cal/Documents/Private-Sync/log/* ./logs/
