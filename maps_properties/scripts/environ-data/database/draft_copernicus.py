# python 3.8 64-bit
# Organizing database

import pandas as pd 
import os
from csv import writer

path_db = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/DATABASE/VARmonthlyavg.xlsx"

# CHL COPERNICUS DATA

# Read csv with tabular data, 
# Transpose to make columns=regions and rows=dates,
# Then delete first row, which is the ID.
# ID not needed, because we know 1st col = region 1 and so on.
chl = pd.read_csv("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/chl/1997-2001_Copernicus/monthly_avg/1997monthly_chl.csv").T.drop('ID')

for index, row in chl.iterrows(): # Iterating through rows
    year = index[1:].split('.')[0][0:]
    month = index[1:].split('.')[1][0:]
    
    curr_dataReg1 = row[0] # Acess data for first column
    print(year + " " + month)
    print(curr_dataReg1)
    

