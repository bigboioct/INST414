import pandas as pd
import requests

url = 'https://api.covidtracking.com/v1/us/daily.csv'

response = requests.get(url)

df = pd.read_csv(url)

cols_to_keep = ['date', 'hospitalizedCumulative']

for col in df.columns:
    if col not in cols_to_keep:
        df.drop(columns=col, inplace=True)

print(df)

first_hospitalizedCumulative = df.iloc[-1, 1]

last_hospitalizedCumulative = df.loc['hospitalizedCumulative',1]
print(last_hospitalizedCumulative - first_hospitalizedCumulative)