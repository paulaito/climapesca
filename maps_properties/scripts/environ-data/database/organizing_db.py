# python 3.8 64-bit
# Organizing database: getting mean values (previously extracted) from each month, region and variable, then add into database.

from asyncio.windows_events import NULL
import pandas as pd 
import os

## BEFORE RUNNING FUNCTION FOR THE FIRST TIME!!!
# Create empty df: DATABASE (where data will be inserted)
db = pd.DataFrame([])

## SST PODAAC, CHL OCEAN COLOR: they all have same column names to indicate date. ex: sst_avg_1 (avg of sst on 1st month)
## PODAAC provider_id: 103; OCEAN COLOR provider_id: 100

## FOR ALL FILES IN DIRECTORY

# Loop for Chl Ocean Color
dir_oceancolor = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/chl/2002-2020_OceanColor/monthly_avg/"
provider_id_oceancolor = 100

for file in os.listdir(dir_oceancolor):
    current_data = pd.read_csv(dir_oceancolor + file).T.drop('ID').rename(columns={0: "NOR_avg", 1: "CEN_avg", 2: "SOU_avg"})
    
    year = file[:4]
    var = file.split('_')[1].split('.')[0]
    years = [year] * len(current_data)
    vars = [var] * len(current_data)
    provider = [provider_id_oceancolor] * len(current_data)
    current_data.insert(0, 'var_id', vars)
    current_data.insert(1, 'year', years)
    months = []
    for index, row in current_data.iterrows():
        month = int(index.split('_')[-1])
        months.append(month)
    current_data.insert(2, 'month', months)
    current_data.insert(6, 'provider_id', provider)
    db = db.append(current_data, ignore_index = True)

# Loop for SST PODAAC
dir_podaac = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/sst/2003-2020_PODAAC/monthly_avg/"
provider_id_podaac = 103

for file in os.listdir(dir_podaac):
    current_data = pd.read_csv(dir_podaac + file).T.drop('ID').rename(columns={0: "NOR_avg", 1: "CEN_avg", 2: "SOU_avg"})
    
    year = file[:4]
    var = file.split('_')[1].split('.')[0]
    years = [year] * len(current_data)
    vars = [var] * len(current_data)
    provider = [provider_id_podaac] * len(current_data)
    current_data.insert(0, 'var_id', vars)
    current_data.insert(1, 'year', years)
    months = []
    for index, row in current_data.iterrows():
        month = int(index.split('_')[-1])
        months.append(month)
    current_data.insert(2, 'month', months)
    current_data.insert(6, 'provider_id', provider)
    db = db.append(current_data, ignore_index = True)


# Loop for wspd, uwnd and vwnd (FL)
dir_wind_FL = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/wind/Wind/tabular_data/monthly_avg/"
provider_wind_FL = "104"

for file in os.listdir(dir_wind_FL):
    current_data = pd.read_excel(dir_wind_FL + file).rename(columns={1: "NOR_avg", 2: "CEN_avg", 3: "SOU_avg"}).set_index("RegionID")

    year = file[:4]
    var = file.split('_')[1]

    years = [year] * len(current_data)
    vars = [var] * len(current_data)
    provider = [provider_wind_FL] * len(current_data)
    current_data.insert(0, 'var_id', vars)
    current_data.insert(1, 'year', years)
    months = []
    for index, row in current_data.iterrows():
        month = int(index.split('_')[-1])
        months.append(month)
    current_data.insert(2, 'month', months)
    current_data.insert(6, 'provider_id', provider)
    db = db.append(current_data, ignore_index = True)



### COPERNICUS DATA: they all have same row names to indicate date. ex: X2002.04.01.12 to indicate april 2002

dir_copernicus_wind = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/wind/2007-2019_copernicus/monthly_avg/"
provider_id_copernicus_wind = 102

# Loop for Copernicus wind data
for file in os.listdir(dir_copernicus_wind):
    current_data = pd.read_csv(dir_copernicus_wind + file).T.drop('ID').rename(columns={0: "NOR_avg", 1: "CEN_avg", 2: "SOU_avg"})

    year = file[:4]
    var = file.split('_')[1].split('.')[0]

    years = [year] * len(current_data)
    vars = [var] * len(current_data)
    provider = [provider_id_copernicus_wind] * len(current_data)
    current_data.insert(0, 'var_id', vars)
    current_data.insert(1, 'year', years)
    months = []
    for index, row in current_data.iterrows():
        month = int(index.split('.')[1])
        months.append(month)
    current_data.insert(2, 'month', months)
    current_data.insert(6, 'provider_id', provider)
    db = db.append(current_data, ignore_index = True)


## Loop for Copernicus Chl data
dir_copernicus_chl = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/chl/1997-2001_Copernicus/monthly_avg/"
provider_id_copernicus_chl = 101


for file in os.listdir(dir_copernicus_chl):
    current_data = pd.read_csv(dir_copernicus_chl + file).T.drop('ID').rename(columns={0: "NOR_avg", 1: "CEN_avg", 2: "SOU_avg"})

    year = file[:4]
    var = file.split('_')[1].split('.')[0]

    years = [year] * len(current_data)
    vars = [var] * len(current_data)
    provider = [provider_id_copernicus_chl] * len(current_data)
    current_data.insert(0, 'var_id', vars)
    current_data.insert(1, 'year', years)
    months = []
    for index, row in current_data.iterrows():
        month = int(index.split('.')[1])
        months.append(month)
    
    current_data.insert(2, 'month', months)
    current_data.insert(6, 'provider_id', provider)
    db = db.append(current_data, ignore_index = True)


## EXPORTING DATABASE TO EXCEL FILE

db.to_excel("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/DATABASE/DATABASE.xlsx", index = False)
