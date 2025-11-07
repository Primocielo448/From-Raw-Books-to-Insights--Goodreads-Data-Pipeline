# 📚 From Raw Books to Insights — Goodreads Data Pipeline & Analysis

**Author:** Athanasios-Marios Marougkas  
**Technologies:** Python, Pandas, Matplotlib, Jupyter Notebook, Git

---

## 🧠 Overview

This project demonstrates a complete **data engineering and analytics workflow** using a dataset of books from Goodreads (source: Jeffrey Allen).  
The goal is to showcase both **data pipeline automation** and **exploratory data analysis (EDA)** through clean, reproducible code and clear visual insights.

---

## 🧩 Project Architecture

project/
│
├── data/
│ ├── raw/ # Raw CSV from Goodreads
│ ├── processed/ # Cleaned CSV ready for analysis
│
├── notebooks/
│ └── Book_Data_Analysis.ipynb # Exploratory data analysis and charts
│
├── src/
│ └── data/
│ ├── load_data.py # Loads raw dataset
│ └── clean_data.py # Cleans and preprocesses data
│
├── outputs/
│ └── figures/ # Generated visualizations
│
├── main.py # Runs the entire pipeline
├── requirements.txt # Dependencies
└── README.md # Documentation

yaml
Αντιγραφή κώδικα

---

## ⚙️ Pipeline Steps

1. **Load raw data** → from `/data/raw/books.csv`
2. **Clean data** → removes duplicates, missing titles/authors, fixes formatting  
3. **Analyze & visualize** → interactive EDA in Jupyter Notebook  

Run the full pipeline with:
```bash
python main.py
Open the analysis notebook with:

bash
Αντιγραφή κώδικα
jupyter notebook notebooks/Book_Data_Analysis.ipynb
📊 Example Insights
Metric	Description
⭐ Rating Distribution	Most books rated between 3.5 and 4.5
👑 Top Authors	Frequent authors in the dataset
📘 Pages vs Ratings	Correlation between book length and reader satisfaction
🕒 Publication Trends	How ratings evolve across years

Sample chart:


🧩 Tech Stack
Python 3.12+

Pandas for data manipulation

Matplotlib / Seaborn for visualization

Jupyter Notebook for EDA

Git & GitHub for version control

🚀 Next Steps / Extensions
Add genre classification or sentiment analysis

Build a small recommendation system

Deploy a Streamlit dashboard for interactive exploration

🏁 Credits
Dataset by Jeffrey Allen on Kaggle
Project developed by Athanasios-Marios Marougkas as part of a personal data engineering & analytics portfolio.