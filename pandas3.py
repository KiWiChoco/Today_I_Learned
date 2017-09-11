import pandas as pd

rng = pd.date_range('1/1/2017',periods=72,freq='H') #<-freq = D는 day S는 초로 72개 나타내줌
print(rng)

