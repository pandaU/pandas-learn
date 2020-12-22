import pandas as pd

#字符串操作只用于  series  只能在字符串类型字段上操作  str是series 属性

df = pd.read_csv('./data/beijing_tianqi_2018.csv')
# print(df.dtypes)
# print(df["bWendu"].str.isnumeric())
# print(df["bWendu"].str.len())
#链式
df.set_index('ymd',inplace=True,drop=False)
print(df["ymd"].str.replace("-","").str[0:6])
# print(df["ymd"].str.replace("-",""))

def  getData(df):
    y,M,d = df["ymd"].split("-")
    return f"{y}年{M}月{d}日"
df.loc[: , "中文日期"]=df.apply(getData,axis=1)
print(df["中文日期"])
print(df["中文日期"].str.replace("[年月日]",""))
