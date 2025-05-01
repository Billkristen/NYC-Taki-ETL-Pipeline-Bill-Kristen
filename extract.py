import pandas as pd

def extract_data(nrows=100000):
    url = "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2023-01.csv"
    df = pd.read_csv(url, nrows=nrows)
    return df
