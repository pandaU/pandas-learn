import pandas as pd
import os
work_path = "./data/c15_excel_split_merge"
split_path = f"{work_path}/splits_new"
if not os.path.exists(split_path):
    os.mkdir(split_path)
df_source = pd.read_excel(f"{work_path}/crazyant_blog_articles_source.xlsx",engine="openpyxl")
count = df_source.shape[0]

user_names = ["xiao_xiong","xiao_shuai","xiao_wang","xiao_hong","xiao_ming","xiao_zhu"]

size = count // len(user_names)
if count % len(user_names) != 0:
    size += 1
subs=[]
for idx,user_name in enumerate(user_names):
    start = idx * size
    end =start +size
    sub =df_source.iloc[start:end]
    subs.append((idx,user_name,sub))
for idx,user_name,sub in subs:
    file_name = f"{split_path}/blog_articles_{idx}_{user_name}.xlsx";
    sub.to_excel(file_name,engine="openpyxl",index=False)
