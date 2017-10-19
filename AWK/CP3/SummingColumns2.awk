# sum2 - check that each line has the same fields as line one
NR == 1 {nfone = NF}
        { if(NF != nfone)
            printf("#%d does not has the same number of fields as line one\n",NR)
          for(i=1; i<=NF; i++){
              sum[i] += $i}}
END { for(j=1; j<=nfone; j++){
        printf("%g%s",sum[j], j < nfone ? "\t":"\n")}}
