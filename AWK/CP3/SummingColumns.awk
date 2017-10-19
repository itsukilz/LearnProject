#sum1- print sum of each column
    {
        for(i=1; i<=NF; i++){
                sum[i] += $i
            }
        if(NF > maxf)
            maxf = NF
    }

    END { for(j=1; j<=maxf; j++){
            printf("%d\t",sum[j])
          }
    }
