#iotop -aotqq >> /home/cal/Documents/Private-Sync/log/iotop.log &
python /home/cal/Documents/Private-Sync/readnet.py
ssh cal@192.168.3.2 '/home/cal/Documents/Private-Sync/monitor.sh'
#unison one two
rsync -rv /home/cal/Documents/one/ cal@192.168.3.2:/home/cal/Documents/one
ssh cal@192.168.3.2 '/home/cal/Documents/Private-Sync/stopmonitor.sh'
python /home/cal/Documents/Private-Sync/readnet.py
#pkill iotop
echo "\nEND\n" >> /home/cal/Documents/Private-Sync/log/iotop.log
