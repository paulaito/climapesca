import arcpy as ap
import os

# py27_32

directory = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/mar/asc"

for curr_file in os.listdir(directory):
    if curr_file.endswith(".asc"):
        curr_filename = curr_file[:-4]
        ap.RasterToNetCDF_md(in_raster = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/mar/asc/" + curr_file, out_netCDF_file = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/mar/nc/" + curr_filename + ".nc", variable_units="", x_dimension="lon", y_dimension="lat", band_dimension="", fields_to_dimensions="", compression_level="0")
        continue
    else :
        continue

