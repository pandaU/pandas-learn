import pandas as pd
df = pd.read_excel('./data/student_excel.xlsx',engine='openpyxl',skiprows=2)
print(df.head())
# isnull 和 notnull 检测空值
#print(df.isnull())
#print(df.loc[df["分数"].notnull(), :])
#dropna 丢弃 列
df.dropna(axis=1,how="all",inplace=True)
print(df.head())
#dropna 丢弃 行
df.dropna(axis=0,how="all",inplace=True)
print(df.head())
#fillna 填充
#df = df.fillna({"分数":0,"姓名":"xxx"})
#2
df.loc[:,"分数"] = df["分数"].fillna(0)
df.loc[:,"姓名"] = df["姓名"].fillna(method="ffill")
print(df.head())
df.to_excel('./data/student_excel_openpyxl.xlsx',engine='openpyxl',index=False)
