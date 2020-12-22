import pandas as pd

reate_df = pd.read_csv("./data/movie/ratings.dat",sep="::",engine="python",names="UserID,MovieID,Rating,Timestamp".split(","))
reate_df.set_index("UserID")
user_df = pd.read_csv("./data/movie/users.dat",sep="::",engine="python",names="UserID,Gender,Age,Occupation,Zip-code".split(","))
user_df.set_index("UserID")
movie_df = pd.read_csv("./data/movie/movies.dat",sep="::",engine="python",names="MovieID,Title,Genres".split(","))
result1= reate_df.merge(right=user_df,left_on="UserID",right_on="UserID")
print(result1.head())
result2 = result1.merge(right=movie_df,left_on="MovieID",right_on="MovieID")
print(result2.head())