import sqlite3
import pandas as pd


# Data_1 is Datasource 1 from project-plan.md

data_1 = pd.read_csv(r"D:/FAU/MADE/GDP_per_capita_table.csv") #datasource collect from https://www.kaggle.com/datasets/samuelcortinhas/gdp-of-european-countries?select=GDP_per_capita_table.csv

# Data_2 is Datasource 2 from project-plan.md

data_2 = pd.read_excel(r"D:/FAU/MADE/unemployment_rate.xlsx") #datasource collect from https://ec.europa.eu/eurostat/databrowser/view/une_rt_a__custom_9447392/default/table?lang=en

conn = sqlite3.connect(r"D:\FAU\MADE\made-template\data\db_rituparna.sqlite")

data_1.to_sql("GDP Count", conn, if_exists="replace") 
data_2.to_sql("Unemployment Rate", conn, if_exists="replace") 