{
        line[NR] = $0  #创建一个数组line，将每行用NR作为下标存储
    }
    END {
            for(i=NR; i>=1; i=i-1){
                        print line[i]
                        }
                    }
