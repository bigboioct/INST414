import json
import pandas as pd

data = pd.read_json('Data/imdb_movies_2000to2022.prolific.json', lines=True)

df = pd.DataFrame(data)

actor_genre_df = df[['genres']].explode('actors')
print(actor_genre_df.head())