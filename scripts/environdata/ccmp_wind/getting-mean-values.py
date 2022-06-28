import pandas as pd
from openpyxl import load_workbook

# DRAFT

### Getting mean values of a single wind dataset for each fishing areas region 

# reading only the columns we are interested in: wind values and region
uwnd_mr87 = pd.read_csv("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/wind/Wind/tabular_data/uwnd/2002_MR_uwnd.csv").loc[:, ['Value', "SrcID_Feat"]]
uwnd_mr87.columns = ['Uwnd_values', 'RegionID'] # changing column names
uwnd_mr87 = uwnd_mr87[['RegionID', 'Uwnd_values']] # changing columns order
uwnd_mr87['RegionID'] = uwnd_mr87['RegionID'].apply(lambda x: x + 1) # adjusting region ID to match. (0,1,2) -> (1, 2, 3)

data = [] # creating empty list

for i in range(1,4):
    curr_avg = (uwnd_mr87[uwnd_mr87['RegionID'] == i])['Uwnd_values'].mean() # getting mean for region i
    data.append([i, curr_avg]) # adding current region and average to list

uwnd_mr87_avg = pd.DataFrame(data, columns = ['RegionID', 'Uwnd_avg_MR']).set_index('RegionID').transpose() # converting list into dataframe whose index is 'RegionID'

#print(uwnd_mr87_avg)

# creating dictionary with months' abbreviations and numbers for further use
months = {'J': 1, 'F': 2, 'MR': 3, 'AP': 4, 'M': 5, 'JN': 6, 'JL': 7, 'AG': 8, 'S': 9, 'O': 10, 'N': 11, 'D': 12}

######### other df
# reading only the columns we are interested in: wind values and region
uwnd_f87 = pd.read_csv("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/wind/Wind/tabular_data/uwnd/2002_F_uwnd.csv").loc[:, ['Value', "SrcID_Feat"]]
uwnd_f87.columns = ['Uwnd_values', 'RegionID'] # changing column names
uwnd_f87 = uwnd_f87[['RegionID', 'Uwnd_values']] # changing columns order
uwnd_f87['RegionID'] = uwnd_f87['RegionID'].apply(lambda x: x + 1) # adjusting region ID to match. (0,1,2) -> (1, 2, 3)

data = [] # creating empty list

for i in range(1,4):
    curr_avg = (uwnd_f87[uwnd_f87['RegionID'] == i])['Uwnd_values'].mean() # getting mean for region i
    data.append([i, curr_avg]) # adding current region and average to list

uwnd_f87_avg = pd.DataFrame(data, columns = ['RegionID', 'Uwnd_avg_f']).set_index('RegionID').transpose() # converting list into dataframe whose index is 'RegionID'

#print(uwnd_f87_avg)
#########

### EXPORTING TO EXCEL FILE

writer = pd.ExcelWriter('C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/scripts/environ-data/excel-draft/demo.xlsx', engine='openpyxl')
uwnd_mr87_avg.to_excel(writer, sheet_name='Sheet1', index=True)

writer.save()

reader = pd.read_excel(r'C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/scripts/environ-data/excel-draft/demo.xlsx')

uwnd_f87_avg.to_excel(writer,index=True,header=False, startrow=len(reader)+1)
writer.save()

reader = pd.read_excel(r'C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/scripts/environ-data/excel-draft/demo.xlsx')
writer.save()
print(reader)
