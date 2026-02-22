import pandas as pd
import os
from sqlalchemy import create_engine
from kaggle.api.kaggle_api_extended import KaggleApi

DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
ENDPOINT = os.getenv('DB_HOST','pgdatabase')
PORT = os.getenv('DB_PORT','5432')
USER = os.getenv('DB_USER','admin')
PASSWORD = os.getenv('DB_PASSWORD','root')
DATABASE = os.getenv('DB_NAME', 'openAQ')

engine = create_engine(f'{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}')

def start_ingestion():
	print("Connecting to Kaggle API...")
	api = KaggleApi()
	api.authenticate()

	dataset = 'shivamshinde1904/weather-data2000-2023' # target dataset
	print(f"Downloading dataset: {dataset} >>>")
	api.dataset_download_files(dataset, path='.', unzip=True)

	csv_file = 'Argentina_weather_data.csv' # csv file name

	if os.path.exists(csv_file):
		print(f"Reading {csv_file}>>>")
		df = pd.read_csv(csv_file)

		print("Transforming data...")
		df.columns = [c.lower().replace(' ', '_') for c in df.columns] 
		df['ingested_at'] = pd.Timestamp.now()
		df = df.fillna(0)
		
		
		print(f"Loading {len(df)} rows into PostgresSQL...")
		df.to_sql('kaggle_weather', con=engine, if_exists='replace', index=False)

		print("Succeeded! Data is now in your Postgres database.")
	else:
		print(f"Error: Could not find {csv_file}. Currnt files: {os.listdir('.')}")
	
if __name__ == "__main__":
    start_ingestion()
