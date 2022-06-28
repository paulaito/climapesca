import arcpy as ap
from arcpy import env
import os

# py27_32 enrivonment with python 2.7 32-bit

raster_data_dir = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/wind/Wind/raster_data/" #directory with subfolders contaning raster datasets
final_dir = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/wind/Wind/tabular_data/" #where .csv shall be created
XDimension = "lon"
YDimension = "lat"
bandDimmension = ""
dimensionValues = ""
valueSelectionMethod = ""
cellRegistration = ""
variable = "uwnd" # "wspd", "uwnd" or "vwnd"

# getting numerical data of wind raster data at fishing areas location

for root, dirs, files in os.walk(raster_data_dir):
    for file in files:
        current_year = root[-4:]
        inNetCDFFile = root + "/" + file
        
        current_YearAndMonth = current_year + "_" + file.split("_")[0][0:]
        
        ap.MakeNetCDFRasterLayer_md(inNetCDFFile, variable, XDimension, YDimension,
                           current_YearAndMonth, bandDimmension, dimensionValues, 
                           valueSelectionMethod, cellRegistration)
        env.workspace = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA"
        
        current_outputTable = final_dir + variable + "/" + current_YearAndMonth + "_" + variable + ".csv"
        
        ap.ExtractValuesToTable_ga("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/fishing-areas/fishing_areas.shp",
                         current_YearAndMonth, current_outputTable)

