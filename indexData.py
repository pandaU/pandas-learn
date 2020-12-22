import pandas as pd
from sklearn.utils import shuffle
df = pd.read_csv("./data/ratings.csv")
print(df.count())
#drop 代表是否丢弃原先colum
df.set_index("userId",inplace=True,drop=False)
print(df.head())

df_shuffle = shuffle(df)
print(df_shuffle.head())