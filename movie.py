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
# print(new_df.duplicated().sum())
# print(movies.iloc[0].genres)
# we need the genresd in a list
import ast
def convert_to_list(x):
    L=[]
    for i in ast.literal_eval(x):
        L.append(i['name'])
    return L

new_df['genres']=new_df['genres'].apply(convert_to_list)
# print(movies.head())

new_df['keywords']=new_df['keywords'].apply(convert_to_list)

def convert_3(x):
    L=[]
    counter=0
    for i in ast.literal_eval(x):
        if counter!=3:
            L.append(i['name'])
        else:
            break
    return L
new_df['cast']=new_df['cast'].apply(convert_3)



# print(new_df.iloc[0].keywords)

# we need the names from crew from only thjose who have jobs as director

def get_director(x):
    L=[]
    for i in ast.literal_eval(x):
        if i['job']=='Director':
            L.append(i['name'])
            break
    return L

new_df['crew']=new_df['crew'].apply(get_director)

new_df['overview']=new_df['overview'].apply(lambda x:x.split())

new_df['genres']=new_df['genres'].apply(lambda x:[i.replace(" ","")for i in x])
new_df['keywords']=new_df['keywords'].apply(lambda x:[i.replace(" ","")for i in x])
new_df['cast']=new_df['cast'].apply(lambda x:[i.replace(" ","")for i in x])
new_df['crew']=new_df['crew'].apply(lambda x:[i.replace(" ","")for i in x])
# print(new_df.head())

new_df['tags']=new_df['tags']=new_df['overview']+new_df['genres']+new_df['keywords']+new_df['cast']+new_df['crew']
final_df=new_df[['movie_id','title','tags']]
# print(final_df.head())
# convert tags to strings
final_df['tags']=final_df['tags'].apply(lambda x:" ".join(x))

final_df['tags']=final_df['tags'].apply(lambda x:x.lower())