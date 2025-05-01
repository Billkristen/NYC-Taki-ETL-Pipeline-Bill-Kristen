from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_to_sqlite

def main():
    raw_df = extract_data()
    clean_df = transform_data(raw_df)
    load_to_sqlite(clean_df)

if __name__ == "__main__":
    main()
