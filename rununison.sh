iotop -aotqq >> ./iotop.log &
unison one two
pkill iotop
echo "\nEND\n" >> ./iotop.log
