'''napi oldalmegtekinések száma  a codecamp orgon 2016-19 között. 
 Ezen adatok idősoros megtekintése diagramon'''
 
import pandas as pd
import matplotlib as plt
import seaborn as sns 
 
 
df = pd.read_csv("fcc-forum-pageviews.csv")
print(df.head())




