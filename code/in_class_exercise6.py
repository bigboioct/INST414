import pandas as pd
import json
from sklearn.metrics import DistanceMetric

data = []
with open('C:/Users/octav/Documents/GitHub/INST414/Data/imdb_movies_2000to2022.prolific.json') as f:
    for line in f:
        movie = json.loads(line)
        for actor in movie['actors']:
            row = {'actor': actor[0]}
            for genre in movie['genres']:
                if genre not in row:
                    row[genre] = 0
                row[genre] += 1
            data.append(row)
            
df = pd.DataFrame(data)
print(df.head())