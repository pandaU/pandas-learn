import pandas as pd

df = pd.read_csv('./data/beijing_tianqi_2018.csv')
#替换列值
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃","").astype("int32")
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃","").astype("int32")
print(df.head())
#数值
#print(df.describe())
#字符串 枚举 去重
#print(df['fengxiang'].unique())
#print(df['fengxiang'].value_counts())
#print(df['tianqi'].unique())

#协方差矩阵
print(df.cov())
#相关系数矩阵
print(df["aqi"].corr(df["bWendu"]))
print(df["aqi"].corr(df["bWendu"]-df["yWendu"]))