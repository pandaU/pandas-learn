import pandas as pd
df = pd.read_csv('./data/beijing_tianqi_2018.csv')
#替换列值
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃","").astype("int32")
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃","").astype("int32")

# print(df["aqi"].sort_values(ascending=False))
print(df.sort_values(by=["aqi","bWendu"],ascending=False))
print(df.sort_values(by=["aqi","bWendu"],ascending=[False,True]))
