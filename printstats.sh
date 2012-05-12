printf "Time\t\t Read\t\t Wrote\n"
cat ./iotop.log | awk '{if($13 == "unison") print $1," \t",$5 $6," \t",$7 $8; else if($1 == "END") print "\nEnd of Session\n"}'
