import pandas as pd ,numpy as np

df =pd.DataFrame(
    np.arange(12).reshape(3,4),
    columns=["A","B","C","D"]
)
print(df.head())
#删除A列
# df.drop("A",axis=1,inplace=True)
# print(df.head())
# df.drop(1,axis=0,inplace=True)
# print(df.head())
#聚合  axis =0 代表列的聚合操作  =1 代表行的聚合
print(df.mean(axis=1))

def getdata(df):
    return df["A"]+df["B"]+df["C"]+df["D"]
df.loc[:, "SUM"] = df.apply(getdata,axis=1)
print(df.head())
