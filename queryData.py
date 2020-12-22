import pandas as pd

df = pd.read_csv('./data/beijing_tianqi_2018.csv')
print(df.head(5))
#替换索引
df.set_index('ymd',inplace=True)
print(df.head(5))
print(df.index)
#替换列值
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃","").astype("int32")
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃","").astype("int32")
#print(df.dtypes)
#查询
print(df.loc[["2018-12-27","2018-12-28"],["bWendu","yWendu"]])
# 区间查询
print(df.loc[df["yWendu"]<-5, :])
print(df["yWendu"]<-5)
#复杂条件
print(df.loc[(df["yWendu"]<-5) & (df["bWendu"]>3) & (df["aqiLevel"]==1), :])
# 函数
#print(df.loc[lambda df : (df["yWendu"]<-5) & (df["bWendu"]>3) & (df["aqiLevel"]==1), :])
def querydata(df):
    return df.index.str.startswith("2018-09") & df["aqiLevel"] ==1
print(df.loc[querydata, :])


