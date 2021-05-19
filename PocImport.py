import pandas as pd
import pymysql
import numpy as np
#需要修改的变量
# num = 2
# img_id = 5
#####
if num == 0:
    board_id = 5
elif num == 1:
    board_id = 9
elif num == 2:
    board_id = 10
df1 = pd.read_excel('./poc/20210518.xlsx', engine="openpyxl",header = None,sheet_name=num)
df1.dropna(axis=1,how="all",inplace=True)
df1.fillna(method="ffill")
print(df1)
list1 =[]
length = len(df1)/2
map1 = {}
start = int(length)
for i in range(0,int(len(df1))):
    if i % 2 != 0:
        map1[i] = start
        start = start-1
updates=[]
for index, row in df1.iterrows():
    col = 1
    if index%2 != 0 :
        r = map1[index]
        for v in row:
            if np.isnan(v):
                v=0
            tp = (img_id,board_id, r, col,v)
            col = col+1
            updates.append(tp)
print(updates)
# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", passwd="123456", database="hntobacco",port=8066)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
for tuples in updates:
    sql ='insert into board_plan_position_imgs (img_id,board_id,row,col,tobacco_id) ' \
     'values (%s, %s,  %s,  %s,  %s)' % tuples
    print(sql)
    cursor.execute(sql)
db.commit()
print("数据操作完成")
# 关闭数据库连接
db.close()

