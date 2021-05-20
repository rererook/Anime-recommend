import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv(r'C:\Users\ASUS.LAPTOP-ND8SPQRT\Documents\Year 3\Data vis\Anime file/AnimeList.csv')
columns =  [ 'title','studio' , 'genre' , 'producer']
df1 =df[columns]
df1['C'] = np.arange(df1.shape[0])

def get_important_features(df1):
    important_features = []
    for i in range (0,df.shape[0]):
          important_features.append(str(df1['title'][i])+' '+str(df1['studio'][i])+' '+str(df1['genre'][i])+' '+str(df1['producer'][i]))
   
    return important_features

df1['important_features'] = get_important_features(df1)

cm = CountVectorizer().fit_transform(df1['important_features'])
cs = cosine_similarity(cm)

Title = 'Bleach'

anime_id = df1[df1.title == Title]['C'].values[0]
scores = list(enumerate(cs[anime_id]))

sorted_scores = sorted(scores, key = lambda x:x[1] , reverse = True)
sorted_scores = sorted_scores[1:]

j = 0 
print(
      
      'The 7 most recommend  animes  to ' , Title , 'are:\n')
for item in sorted_scores :
    anime_title = df1[df1.C == item[0]]['title'].values[0]
    print (j+1 , anime_title)
    j = j+1
    if j>9 :
        break