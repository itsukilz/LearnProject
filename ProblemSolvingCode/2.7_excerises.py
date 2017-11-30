import timeit
from timeit import Timer
import pandas as pd

list_index_time = []
list_index_k = []

index_time = Timer('x[10]',"from __main__ import x")

for i in range(1000,2000000,2000):
    x = list(range(i))
    pt = index_time.timeit(number=1000)

    #print '%10.5f' % pt

    list_index_k.append(i)
    list_index_time.append(pt)

list_index = pd.DataFrame()
list_index['time'] = list_index_time
list_index['k'] = list_index_k

list_index.plot()