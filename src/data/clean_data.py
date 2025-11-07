import pandas as pd
import os
Raw_Location = os.path.join("data","raw","books.csv")
Clean_Location = os.path.join("data","processed","books_clean.csv")

def Clean_Data():
   try:
      #Load the raw dataset
      df=pd.read_csv(Raw_Location, encoding="utf-8",on_bad_lines="skip")
      #Remove duplicates
      df=df.drop_duplicates()
      #Remove rows with missing titles or authors
      df=df.dropna(subset=["title","authors"])
      #Verifying the existence of the processed folder
      os.makedirs(os.path.join("data","processed"),exist_ok=True)
      #Saving clean dataset
      df.to_csv(Clean_Location, index=False)
      print(f"Data cleaned successfuly! Data saved to {Clean_Location} (rows: {len(df)})")
   except Exception as e:
      print(f"An error occurred! {e}")

if __name__=="__main__":
   Clean_Data() 