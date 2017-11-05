/Asia/ {pop["Asia"] += $3}
/Europe/ {pop["Europe"] += $3}
END {print "Asia population is ",pop["Asia"],"million."
     print "Europe population is ",pop["Europe"],"million."
     }
