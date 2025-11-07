import pandas as pd
import os
# Define the location of te raw data
Data_Location = os.path.join("data","raw","books.csv")

def Load_Data(Loc = Data_Location):
   try:
      df = pd.read_csv(Loc, encoding='utf-8', on_bad_lines='skip')
      print(f"Data loaded successfully! Shape: {df.shape}")
      return df
   except FileNotFoundError:
      print("File not found :( .Please check the csv file's location")
   except Exception as e:
      print(f"An error occurred! {e}")

if __name__ == "__main__":
   Load_Data()