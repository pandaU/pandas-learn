import pandas as pd
import os

work_path = "./data/c15_excel_split_merge"
split_path = f"{work_path}/splits_new"
excel_names =[]
for excel_name in os.listdir(split_path):
    excel_names.append(excel_name)
df_list = [];
for excel_name in excel_names:
    # 读取每个excel到df
    excel_path = f"{split_path}/{excel_name}"
    df_split = pd.read_excel(excel_path, engine="openpyxl")
    # 得到username
    username = excel_name.replace("blog_articles_", "").replace(".xlsx", "")[2:]
    df_split["username"] = username
    df_list.append(df_split)
df = pd.concat(df_list,axis=0,ignore_index=True)
file_name = f"{work_path}/new_merge.xlsx"
df.to_excel(file_name,engine="openpyxl",index=False)