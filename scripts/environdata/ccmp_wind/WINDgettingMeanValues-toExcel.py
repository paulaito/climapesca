import pandas as pd
import openpyxl
import os
import re

# directory with wind tabular data
dir = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/wind/Wind/tabular_data/wspd/"

# creating dictionary with months' abbreviations and numbers for further use
months = {'J': 1, 'F': 2, 'MR': 3, 'AP': 4, 'M': 5, 'JN': 6, 'JL': 7, 'AG': 8, 'S': 9, 'O': 10, 'N': 11, 'D': 12}
years = ['1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
 '2004', '2005', '2006', '2007', '2008', '2009']

for root, dirs, files in os.walk(dir):

    curr_var = dir[-5:-1] # getting current variable: uwnd, vwnd or wspd 
    curr_year = root[-4:] # getting current year from file name
    
    if curr_year not in years:
        continue
    else:
        n = 0

        curr_excel_file = dir + curr_year + "_" + curr_var + "_avg.xlsx"
        writer = pd.ExcelWriter(curr_excel_file, engine='openpyxl')
        
        for file in files:

            if file.endswith(".csv"):
                n += 1

                curr_month_abbrev = re.search('_(.+?)_', file) # getting current month abbreviation from file name (characters between '_')

                if not curr_month_abbrev:
                    curr_month_abbrev = re.search('_(.+?).csv', file) # when nothing between '_' was found, search between '_' and '.csv', 
                    # because there are some files with this pattern.

                curr_month = str(months.get(curr_month_abbrev.group(1))) # getting number of current month

                curr_avg_list = [] # empty list to insert curr_avg later

                curr_data = pd.read_csv(root + "/" + file).loc[:, ['Value', "SrcID_Feat"]] # read csv and these two specific columns
                curr_data.columns = ['uwnd_values', 'RegionID'] # changing column names
                curr_data = curr_data[['RegionID', 'uwnd_values']] # changing columns order
                curr_data['RegionID'] = curr_data['RegionID'].apply(lambda x: x + 1) # adjusting region ID to match. (0,1,2) -> (1, 2, 3)

                for region in range(1,4):
                    curr_avg = (curr_data[curr_data['RegionID'] == region])['uwnd_values'].mean() # getting mean for region i
                    curr_avg_list.append([region, curr_avg]) # adding current region and average to list


                # converting list into dataframe whose index is 'RegionID'
                curr_column = "uwnd_avg_" + curr_month # creating object for first column value
                curr_avg_df = pd.DataFrame(curr_avg_list, columns = ['RegionID', curr_column]).set_index('RegionID').transpose()

                print(curr_avg_df)
                if n == 1:
                   curr_avg_df.to_excel(writer, sheet_name='Sheet1', index=True)
                   writer.save()

                else:
                   reader = pd.read_excel(curr_excel_file)
                   curr_avg_df.to_excel(writer,index=True,header=False, startrow=len(reader)+1)
                   writer.save()

            else:
                continue    

            curr_excel_workbook = openpyxl.load_workbook(curr_excel_file, read_only=False) 
            
            #to open the excel sheet and if it has macros
            
            sheetname = curr_excel_workbook['Sheet1']#get sheetname from the file
            sheetname['A1']= str('RegionID') #write something in B2 cell of the supplied she
            
            curr_excel_workbook.save(curr_excel_file)