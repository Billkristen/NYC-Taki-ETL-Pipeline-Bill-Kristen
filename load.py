import sqlite3

def load_to_sqlite(df, db_path='warehouse/nyc_taxi.db'):
    conn = sqlite3.connect(db_path)
    df.to_sql("yellow_tripdata_2023", conn, if_exists="replace", index=False)
    conn.close()
