import pandas as pd
df = pd.read_csv('./data/beijing_tianqi_2018.csv')
#替换列值
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃","").astype("int32")
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃","").astype("int32")

#df[df["bWendu"]>5]["wen_cha"]=df["bWendu"]-df["yWendu"]
#df[df["bWendu"]>5]  无法确定是获取view 还是copy
print(df.head())
#解决方案
df.loc[df["bWendu"]>5, "wen_cha"] = df["bWendu"]-df["yWendu"]
print(df.loc[df["bWendu"]>5, :])
#2
# copyDf = df[df["bWendu"]>5].copy()
# copyDf["wen_cha"]=df["bWendu"]-df["yWendu"]
# print(copyDf.head())