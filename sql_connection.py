import pyodbc as odbc
import sys
import numpy as np
import time
import pandas as pd

conn = odbc.connect('Driver={SQL Server};'
                    'Server=DESKTOP-852RTG1;'
                    'Database=Takip;'
                    'Trusted_connection=yes;')


liste = []
def values(liste):
    sicaklik = np.random.randint(0,100,1)
    seviye = np.random.randint(0,100,1)
    kapak = np.random.randint(0,2,1)
    liste.append(([sicaklik,seviye,kapak]))

for i in range(30,0,-1):
    values(liste)
    time.sleep(1)
    print((liste[i]))

isimler = ["sicaklik","seviye","kapak"]
df = pd.DataFrame(liste)
df.columns = isimler


cursor = conn.cursor()
cursor.execute('select * from kontrol2')
for row in cursor:
    print(row)


insert_data = """ INSERT INTO kontrol2
                  VALUES (?,?,?)"""

liste1 = []
for i in range((len(df))):
    for j in range(1):
        liste1.append([str(df.iloc[i][j]), str(df.iloc[i][j+1]), str(df.iloc[i][j+2])])

for record in liste1:
    print(record)
    cursor.execute(insert_data, record)


df = pd.DataFrame(liste1)
df.to_csv("df_new.csv")