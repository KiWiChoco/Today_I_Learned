import pandas as pd

sales_states = {'Day' : [1,2,3,4,5,6],
                'visitors' : [43,45,56,67,65,54],
                'revenue' : [64,74,67,56,34,65]}

df = pd.DataFrame(sales_states).set_index('Day')
print(df)


