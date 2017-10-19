# sum3 - print sums of numberic columns
NR == 1 {nfone = NF
         for(i=1; i<=nfone; i++){
             numcol[i] = isnum($i)}}

        {for(j=1;j<=nfone;j++){
                 if(numcol[j])
                     sum[j] += $j
             }
        }

END {for(i=1;i<=nfone; i++){
        if(numcol[i])
            printf("%d",sum[i])
        else
            printf("--")
        printf(i < nfone ? "\t":"\n")}
    }
function isnum(n) {return n ~  /^[+-]?[0-9]+([\.][0-9]+)?$/}
