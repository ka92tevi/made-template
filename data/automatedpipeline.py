import sqlite3
import pandas as pd


# Data_1 is Datasource 3 from project-plan.md

data_1 = pd.read_csv("D:/FAU/MADE/Bicycle_traffic_data_Cologne.csv") #datasource collect from https://offenedaten-koeln.de/sites/default/files/Radverkehr%20f%C3%BCr%20Offene%20Daten%20K%C3%B6ln%202013.csv

# Data_2 is Datasource 2 from project-plan.md

data_2 = pd.read_csv("D:/FAU/MADE/Accident_statistics_Cologne.csv") #datasource collect from https://offenedaten-koeln.de/dataset/unfallstatistik-k%C3%B6ln/resource/a32e0d4a-8a29-4b18-a49d-a9e1966c8c6f#{}

conn = sqlite3.connect("data/dbrituparna.sqlite")

data_1.to_sql("Bicycle", conn, if_exists="replace") 
data_2.to_sql("Accident", conn, if_exists="replace") 