import pandas as pd
df = pd.read_csv('./data/beijing_tianqi_2018.csv')
#替换列值
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃","").astype("int32")
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃","").astype("int32")
#print(df.head())
#赋值
df.loc[:,"wencha"]=df["bWendu"] - df["yWendu"]
#print(df.head())
def sub(df):
    if df["bWendu"]>20:
        return "高温"
    elif df["yWendu"]<-7:
        return "低温"
    else:
        return "常温"
df.loc[:,"wendu_type"] = df.apply(sub,axis=1)
print(df['wendu_type'].value_counts())
df = df.assign(
    yWendu_huashi = lambda x : x["yWendu"] * 9 /5 +32,
    bWendu_huashi = lambda x: x["yWendu"] * 9 / 5 + 32
)
#print(df.head())
#分组
df.loc[df["bWendu"] > 20, "wendu_t"] = "高温2"
df.loc[df["yWendu"] <= 20, "wendu_t"] = "低温2"
print(df.head())