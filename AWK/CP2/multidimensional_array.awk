BEGIN {FS = ","}
{for(i=1;i<=NF;i++)
    a[NR,i] = $i}
END {for (name in a) {
        split(name,k,SUBSEP)
        if(k[1] == "2")
            print a[name]}}
