from src.data.load_data import Load_Data
from src.data.clean_data import Clean_Data
import os

def run_pipeline():
   print("Loading raw data...")
   Load_Data()
   print("\n Cleaning and processing data...")
   Clean_Data()
   print("\n Pipeline executed successfully!")
   print("Cleaned dataset is available at: data/processed/books_clean.csv")

if __name__ == "__main__":
   run_pipeline()