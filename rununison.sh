iotop -aotqq >> ./log/iotop.log &
python readnet.py
ssh cal@192.168.3.2 '/home/cal/Documents/Private-Sync/monitor.sh'
#unison one two
rsync -rv ../one/ cal@192.168.3.2:/home/cal/Documents/one
ssh cal@192.168.3.2 '/home/cal/Documents/Private-Sync/stopmonitor.sh'
python readnet.py
pkill iotop
echo "\nEND\n" >> ./log/iotop.log
