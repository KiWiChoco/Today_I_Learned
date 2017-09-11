import pandas as pd
import random
import numpy as np
sales_states = {'Day' : [1,2,3,4,5,6],
                'visitors' : [43,45,56,67,65,54],
                'revenue' : [64,74,67,56,34,65]}

df = pd.DataFrame(sales_states).set_index('Day')
print(df)


df2 = pd.DataFrame({'A' : ['foo','bar','foo','bar','foo','bar','foo','foo'],
                    'B' : ['one','one','two','three','two','two','one','three'],
                    'C' : np.random.randn(8),
                    'D' : np.random.randn(8)})

print(df2)

grouped = df2.groupby('A')

print(grouped.mean())

print(df.head())