import pandas as pd
import json
import numpy as np
from sklearn.metrics import DistanceMetric

data = []
with open('Data/imdb_movies_2000to2022.prolific.json') as f:
    for line in f:
        entry = json.loads(line)
        for actor in entry['actors']:
            row = {'actor': actor[0]}
            for genre in entry['genres']:
                if genre not in row:
                    row[genre] = 0
                row[genre] += 1
            data.append(row)
            
df = pd.DataFrame(data)
print(df.head())