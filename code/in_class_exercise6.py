import json
import pandas as pd

data = pd.read_json('\Data\imdb_movies_2000to2022.prolific.json')

df = pd.DataFrame(data)

df.head()