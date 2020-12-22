import pandas as pd
import warnings
warnings.filterwarnings("ignore")
df1 = pd.DataFrame(
    {
        "A":["A0","A1","A2","A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"]
    }
)
#print(df1.head())
df2 = pd.DataFrame(
    {
        "A":["A4","A5","A6","A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "F": ["F4", "F5", "F6", "F7"]
    }
)
#print(df2.head())

df3 = pd.concat([df1,df2],axis=0,ignore_index=True)
s1 = df3.apply(lambda x:x["A"]+"HH",axis=1)
s1.name = "K"
df4 = pd.concat([df3, s1], axis=1)
# print(df4.head())
#append
df8 = pd.DataFrame(columns=list("A"))
# print(df8.head())
#低性能
for i in range(5):
    #每次都在复制
    df8 = df8.append({"A":i},ignore_index=True)
print(df8.head())
#高性能
df9 = pd.concat([pd.DataFrame([i],columns=['A']) for i in range(5)],ignore_index=True)
print(df9)
