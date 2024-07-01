import numpy as np
import pandas as pd

movies=pd.read_csv("tmdb_5000_movies.csv")
credits=pd.read_csv("tmdb_5000_credits.csv")

# print(movies.head())

# merge based on title
new_df= movies.merge(credits,on='title')

# Data cleaning
#  we need genres, id, keywords, title, overview, cast, crew
new_df=new_df[['movie_id','title','overview','genres','keywords','cast','crew']]

# noiw we make a new dataframe with 3 columns movi id title and tags
# tags= overview, genres , keywordd ,cast and crew merge it to make tags


# missing data

# print(new_df.isnull().sum())
new_df.dropna(inplace=True)
print(new_df.duplicated().sum())