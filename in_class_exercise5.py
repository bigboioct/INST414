import pandas as pd
from sklearn.metrics import DistanceMetric, pairwise_distances
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_json('data/imdb_movies_2000to2022.prolific.json', lines=True)

genre_counts = {}

# Iterate through the DataFrame
for index, row in df.iterrows():
    actors = row['actors']
    genres = row['genres']
    
    for actor in actors:
        actor_key, actor_name = actor
        if actor_key not in genre_counts:
            genre_counts[actor_key] = {
                'ActorKey': actor_key,
                'ActorName': actor_name
            }
        
        for genre in genres:
            if genre in genre_counts[actor_key]:
                genre_counts[actor_key][genre] += 1
            else:
                genre_counts[actor_key][genre] = 1

# Convert the dictionary to a list of dictionaries
result_data = list(genre_counts.values())

# Create the final DataFrame
result_df = pd.DataFrame(result_data).fillna(0)

print(result_df)

query_actor_index = 1
query_actor = result_df.iloc[query_actor_index]

actors_data = result_df.drop(['ActorName'], axis=1)

distance_metric = DistanceMetric.get_metric('cosine')
distances = pairwise_distances([query_actor[2:]], actors_data.iloc[:, 2:], metric=distance_metric)

distance_df = pd.DataFrame({'ActorKey': result_df['ActorKey'], 'ActorName': result_df['ActorName'], 'CosineDistance': distances[0]})

similar_actors = distance_df.sort_values(by='CosineDistance').head(11)

print("Top 10 most similar actors to:", query_actor['ActorKey'], query_actor['ActorName'])
print(similar_actors.iloc[1:][['ActorKey', 'ActorName']])  # Exclude the query actor itself