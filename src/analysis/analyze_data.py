import pandas as pd
import matplotlib.pyplot as plt
import os

Clean_Location = os.path.join("data","processed","books_clean.csv")
Output_Location = os.path.join("outputs","figures")

def analyze_data():
   try:
      #Loading cleaned data
      df = pd.read_csv(Clean_Location)
      print(f"Data loaded successfully! Total rows: {len(df)}\n")
      #Basic stats
      print("Basic Statistics:")
      print(df.describe(include='all').transpose().head(10))
      print("\n")
      #Top 10 authors by number of books
      top_authors = df['authors'].value_counts().head(10)
      print("Top 10 Authors by Number of Books:")
      print(top_authors)
      print("\n")
      #Top 10 books by average rating (if existing)
      if 'average_rating' in df.columns:
         top_books=df.sort_values(by='average_rating',ascending=False).head(10)
         print("Top 10 Books By Rating:")
         print(top_books[['title','authors','average_rating']])
      else:
         print(" No 'average_rating' column found - skipping rating analysis")
      #Making sure the corresponding folder exists
      os.makedirs(Output_Location, exist_ok=True)
      #Time to visualize: Top authors
      plt.figure(figsize=(10,5))
      top_authors.plot(kind='bar', color='orange')
      plt.title("Top 10 Authors by Number of Books")
      plt.ylabel("Number of Books")
      plt.xticks(rotation=45,ha="right")
      plt.tight_layout()
      plt.savefig(os.path.join(Output_Location, "top_authorss.png"))
      plt.close()
      print("Charts saved in outputs/figures/")
   except Exception as e:
      print(f"Error during analyseis: {e}")

if __name__ == "__main__":
   analyze_data()
