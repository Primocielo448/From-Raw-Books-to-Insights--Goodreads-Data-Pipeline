import pandas as pd
import os
# Define the location of te raw data
Data_Location = os.path.join("data","raw",'books.csv")

def Load_Data(Loc = Data_location):
   try:
      df = pd.read_csv(path,encoding='utf-8')
      print(f"Data loaded successfully! :)")
      return df
   except FileNotFoundError:
      print("File not found :( .Please check the csv file's location")
   except Exception as e:
      print(f"An error occurred! :(")

if __name__ == "__main__":
   load_data()