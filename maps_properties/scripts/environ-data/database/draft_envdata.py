# python 3.8 64-bit
# Organizing database

from heapq import merge
from zlib import DEF_BUF_SIZE
import pandas as pd 
import os
from csv import writer

path_db = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/DATABASE/VARmonthlyavg.xlsx"

# SST PODAAC, CHL OCEAN COLOR 

# Read csv with tabular data, 
# Transpose to make columns=regions and rows=dates,
# Then delete first row, which is the ID.
# ID not needed, because we know 1st col = region 1 and so on.

dir = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/chl/2002-2020_OceanColor/monthly_avg/"
filename = "2003monthly_chl.csv"
data = pd.read_csv(dir + filename).T.drop('ID')

db = pd.DataFrame([])


#for column in data:
#    print(column)
#    for index, row in data.iterrows(): # Iterating through rows
#        month = index.split('_')[-1]
#        curr_dataReg1 = row[column] # Acess data for first column (region 1)
#
#        curr_reg = column + 1
#        # creating df with current data 
#        df = pd.DataFrame({'year': [year], 'month': [month], 'regionID': [curr_reg], 'sst_avg': [curr_dataReg1]}) 
#
#        # appending current data into database
#        db = db.append(df, ignore_index = True)
#
#    
#

#for file in os.listdir(dir):
#    current_data = pd.read_csv(dir + file).T.drop('ID')
#    year = file[:4]
#    for column in data:
#        for index, row in data.iterrows(): # Iterating through rows
#            month = index.split('_')[-1]
#            curr_dataReg1 = row[column] # Acess data for first column (region 1)
#
#            curr_reg = column + 1
#            # creating df with current data 
#            df = pd.DataFrame({'year': [year], 'month': [month], 'regionID': [curr_reg], 'sst_avg': [curr_dataReg1]}) 
#
#            # appending current data into database
#            db = db.append(df, ignore_index = True)
#


regions = {1: 'NOR', 2: 'CEN', 3: 'SOU'}

#print(data)

#year = filename[:4]        
#
#
#curr_df = pd.DataFrame([])
#
#for column in data:
#    curr_reg_avg = regions.get(column + 1) + "_avg"
#    
#    curr_reg_df = pd.DataFrame([])
#
#    for index, row in data.iterrows():
#        month = index.split('_')[-1]
#
#        df = pd.DataFrame({'year': [year], 'month': [month]}) # curr_reg_avg: row[column]})
#            
#        curr_reg_data = pd.DataFrame ({'year_month': [year + "_" + month], curr_reg_avg: row[column]})
#        
#        curr_reg_df = curr_reg_df.append(curr_reg_data, ignore_index = True)
#
        
datanew = data.rename(columns={0: "NOR_avg", 1: "CEN_avg", 2: "SOU_avg"})
year = filename[:4]
var = filename.split('_')[0]


for index, row in datanew.iterrows():
    month = index.split('_')[-1]
    

print(datanew)
