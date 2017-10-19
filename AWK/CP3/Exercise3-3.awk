# remove the test of numcol in the second 'for' statement 
# no effect  
NR == 1 {nfone = NF
         for(i=1; i<=nfone; i++){
             numcol[i] = isnum($i)}}

NF != 0 {for(j=1;j<=nfone;j++){
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
