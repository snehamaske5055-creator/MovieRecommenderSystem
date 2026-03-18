import idlelib.replace
import numpy as np
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

movies = pd.read_csv("D:\\Aditya's Notes\\All Projects\\Movie Recommender System\\tmdb_5000_movies.csv")
credits = pd.read_csv("D:\\Aditya's Notes\\All Projects\\Movie Recommender System\\tmdb_5000_credits.csv")

movies = movies.merge(credits,on='title')
#print(movies.head(1))
#print(movies.shape)
#print(movies['original_language'].value_counts())
#print(movies.info())
'''
Following columns we have to keep. 
genres,movie_id.keywords,title,overview,cast,crew.
'''

movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]
#print(movies.info())
#print(movies.head(1))

#Checking for Null Values and Dropping if any
#print(movies.isnull().sum())
movies.dropna(inplace=True)
#print(movies.isnull().sum())

#Checking for Duplicate Values
#print(movies.duplicated().sum())

#print(movies.iloc[0].genres)
#[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"},
# {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]
#Convert above data in following format
#['Action','Adventure','Fantasy','SciFi']

def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

movies['genres'] = movies['genres'].apply(convert)
#print(movies['genres'])
#print(movies.head())

movies['keywords'] = movies['keywords'].apply(convert)
#print(movies['keywords'])
#print(movies.head())

#For getting name of actor/actress
def convert3(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter+=1
        else:
            break
    return L

movies['cast'] = movies['cast'].apply(convert3)
#print(movies['cast'])
#print(movies.head())

#for getting name of director
#print(movies['crew'][0])

def fetch_director(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director' :
            L.append(i['name'])
            break
    return L

movies['crew'] = movies['crew'].apply(fetch_director)
#print(movies['crew'])

#print(movies.head())

#converting overview column string to list
#print(movies['overview'][0])

movies['overview'] = movies['overview'].apply(lambda x:x.split())
#print(movies['overview'])
#print(movies.head())

#for removing extra spaces between the words

movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])

'''
print(movies['genres'])
print(movies['keywords'])
print(movies['cast'])
print(movies['crew'])
'''

movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

#print(movies['tags'])
#print(movies.head())

#creating new dataframe
new_df = movies[['movie_id','title','tags']]
#print(new_df)

#converting list to string
new_df.loc[:, 'tags'] = new_df['tags'].apply(lambda x: " ".join(x))
#print(new_df['tags'][0])
#print(new_df)
#print(new_df.head())

#converting to lower case
new_df.loc[:, 'tags'] = new_df['tags'].apply(lambda x:x.lower())
#print(new_df['tags'][0])
#print(new_df)
print(new_df.head())
#print(new_df['tags'][0])
#print(new_df['tags'][1])

#stemming process (eg. love loving loved == love,action,actions == aciton)
ps = PorterStemmer()
def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

new_df.loc[:, 'tags'] = new_df['tags'].apply(stem)


#Model Building Starts from here:
cv = CountVectorizer(max_features=5000,stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()
#print(vectors)
#print(vectors[0])

#to know the feature names
#print(cv.get_feature_names_out())

#finding similarity angle of movies to eachother
similarity = cosine_similarity(vectors)

#print(similarity)
#print(similarity.shape)
#print(similarity[0])

#to find the index of movie in the dataframe
#print(new_df[new_df['title'] == 'Batman Begins'].index[0])
#for sorting accourding to distances
#sorted(list(enumerate(similarity[0])), key=lambda x: x[1], reverse=True)[1:6]

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    for i in movies_list:
        print(new_df.iloc[i[0]].title)

recommend('Batman Begins')

#recomender system created successfuly

#creating pickle file
#pickle.dump(new_df,open('movies.pkl','wb'))

#pickle.dump(new_df.to_dict(),open('movie_dict.pkl','wb'))

#pickle.dump(similarity,open('similarity.pkl','wb'))











