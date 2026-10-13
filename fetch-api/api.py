import requests
import pandas as pd
import csv

response = requests.get("https://api.mfapi.in/mf/119598")

if response.status_code == 200:
  # Converts the json data into python json object so that we can access the value as well.
  data = response.json()

  # DataFrame creates a datatable
  df = pd.DataFrame(data['data'])
  df.to_csv("mutual_funds_data.csv", index=False)
  
  # Returns top 5 or 10 rows output as a check to preview everything worked or not.
  print(df.head())
