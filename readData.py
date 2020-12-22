import pandas as pd

rpath = './data.csv'
df = pd.read_csv(rpath)
print(df.columns)
print(df.index)
# 获取多列值
print(df[['age','desc']])
# 获取行值
print(df.loc[:])
print(type(df.loc[:]))

