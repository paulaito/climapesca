import arcpy
from arcpy.sa import *
from arcpy import env
raster = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/hsm/hsm//Aantennatus_present_hsm.nc"
env.cellSize = raster
env.extent = raster
arcpy.CalculateStatistics_management(raster)
maximum = arcpy.GetRasterProperties_management(raster, "MAXIMUM")
whereCondition = "VALUE <> " + maximum.getOutput(0)
where = SetNull(raster, 1, whereCondition )