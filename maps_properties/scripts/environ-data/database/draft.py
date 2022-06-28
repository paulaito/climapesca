# python 3.8 64-bit
# Organizing database

from heapq import merge
from zlib import DEF_BUF_SIZE
import pandas as pd 
import os
from csv import writer

path_db = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/DATABASE/VARmonthlyavg.xlsx"

# SST PODAAC, CHL OCEAN COLOR 

## FOR ONE FILE:
dir = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/chl/2002-2020_OceanColor/monthly_avg/"

filename = "2003monthly_chl.csv"

# Read csv with tabular data, 
# Transpose to make columns=regions and rows=dates,
# Then delete first row, which is the region ID.
# ID not needed, because we know 1st col = region 1 and so on.

data = pd.read_csv(dir + filename).T.drop('ID').rename(columns={0: "NOR_avg", 1: "CEN_avg", 2: "SOU_avg"})

# get year and variable from filename
year = filename[:4]
var = filename.split('_')[1].split('.')[0]

# create list with year and var in the length of dataframe rows
years = [year] * len(data)
vars = [var] * len(data)

# insert column var_id and year in the df
data.insert(0, 'var_id', vars)
data.insert(1, 'year', years)

months = []

# get each month and add to list 'months'
for index, row in data.iterrows():
    month = int(index.split('_')[-1]) # get month from index
    months.append(month)

# insert column month in the df
data.insert(2, 'month', months)

# export to excel
data.to_excel("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/hehe.xlsx", index = False)



## FOR ALL FILES IN DIRECTORY

# specify directory containing all files
dir = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/chl/2002-2020_OceanColor/monthly_avg/"

db = pd.DataFrame([])

# loop for each file

for file in os.listdir(dir):
    current_data = pd.read_csv(dir + file).T.drop('ID').rename(columns={0: "NOR_avg", 1: "CEN_avg", 2: "SOU_avg"})
    
    year = file[:4]
    var = file.split('_')[1].split('.')[0]

    years = [year] * len(current_data)
    vars = [var] * len(current_data)
    provider = [101] * len(current_data)

    current_data.insert(0, 'var_id', vars)
    current_data.insert(1, 'year', years)

    months = []

    for index, row in current_data.iterrows():
        month = int(index.split('_')[-1])
        months.append(month)

    current_data.insert(2, 'month', months)
    current_data.insert(6, 'provider_id', provider)

    db = db.append(current_data, ignore_index = True)

    
print(db)