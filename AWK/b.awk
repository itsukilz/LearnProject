ARGIND==1 	{accid[$1]} 
END {for (i in accid) print i}