# raster calculator: calculating differences for specialization and marginality mapstar
import os

dir_present = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/mar/nc/present/"
dir_future = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/mar/nc/rcp85/"
final_dir = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/mar/nc/diff85/"

type = "mar_diff85"

n = 0

for current_present in os.listdir(dir_present):
    current_sp_present = (current_present.split('_')[0])[0:] # getting current species for present map
    n += 1
    for current_future in os.listdir(dir_future):
        current_sp_future = (current_future.split('_')[0])[0:] # getting current species for future map
        
        if current_sp_present == current_sp_future: # conditional for further raster calculation only when it is the same species
            
            # creating raster layer objects from both maps
            current_presentPath = dir_present + current_present
            current_presentLayer = QgsRasterLayer(current_presentPath, current_present)
            
            current_futurePath = dir_future + current_future
            current_futureLayer = QgsRasterLayer(current_futurePath, current_future)
            
            # creating Raster Calculator Entry for further use in the calculation
            entries = []
            mapPresent = QgsRasterCalculatorEntry()
            mapPresent.ref = 'mapPresent@1'
            mapPresent.bandNumber = 1
            mapPresent.raster = current_presentLayer
            entries.append(mapPresent)
            
            mapFuture = QgsRasterCalculatorEntry()
            mapFuture.ref = 'mapFuture@1'
            mapFuture.bandNumber = 1
            mapFuture.raster = current_futureLayer
            entries.append(mapFuture)
            
            output = final_dir + current_sp_present + "_" + type + ".nc"
            print("({})".format(n), output)
            calc = QgsRasterCalculator('mapFuture@1 - mapPresent@1', output, 'NetCDF', current_presentLayer.extent(), current_presentLayer.width(), current_presentLayer.height(), entries)
            calc.processCalculation()
            break # break loop and start working with next species
            
        else:
            continue


