# Extracting values from raster object at vector data location
# Raster objects: environmental variables (sst, chl, wind)
# Vector data: fishing-areas (Portugal: North(1), Central(2) and South(3))

library (raster)
library (ncdf4)
library(stringr)

# Polygon as reference for extraction
fishing_areas<- shapefile("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/fishing-areas/fishing_areas.shp")

# Function for single-band files
extract_raster_poly <- function (dir, poly, var, pattern) {
  total_years <- list.files(dir)
  for (year in total_years) {
    curr_list <- list.files(paste0(dir, "/", year, "/data/"), pattern = pattern, full.names=TRUE)
    curr_stack <- raster::stack(curr_list)
    names(curr_stack) <- paste0(var, "_avg_", 1:12)
    current_data <- extract(curr_stack, poly, fun=mean, na.rm=TRUE, df=TRUE)
    write.csv(current_data, file=paste0(dir, "/", year, "/", year, "monthly_", var, ".csv"), row.names = FALSE)
  }
}

#Function for multiple-bands file
extract_multiple_raster_poly <- function(dir, raster, poly, var, varname) {
  if (missing(varname)) {
    dataset <- raster::brick(paste0(dir, "/", raster))
  }
  else {
    dataset <- raster::brick(paste0(dir, "/", raster), varname = varname)
  }
  names <- names(dataset)
  year <- str_sub(names, 2, 5)
  years <- as.list(year) %>% unique(years)
  for (year in years) {
    curr_year <- str_subset(names, pattern = year)
    curr_stack <- raster::subset(dataset, subset = curr_year)
    curr_data <- extract(curr_stack, poly, fun=mean, na.rm=TRUE, df=TRUE)
    write.csv(t(curr_data), file=paste0(dir, "/", year, "monthly_", var, ".csv"), row.names = FALSE)
  }
}

# RUNNING FUNCTION TO EXTRACT

#Chl Ocean Color (single-band files)
extract_raster_poly("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/chl/ocean-color_2002-2020/", fishing_areas, "chl", ".nc$")

#SST PODAAC (single-band files)
extract_raster_poly("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/sst/podaac_2003-2020/", fishing_areas, "sst", "MO.SST.sst.4km_..nc$|MO.SST.sst.4km_...nc$|MO.SST.sst.4km.nc$")

#Chl Copernicus (multiple-bands)
extract_multiple_raster_poly("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/chl/copernicus_1997-2001", "dataset-oc-glo-bio-multi-l4-chl_4km_monthly-rep_1635347399389.nc", fishing_areas, "chl")

#Wind Copernicus (multiple bands): wind speed
extract_multiple_raster_poly("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/wind/2007-2019_copernicus", "WIND.nc", fishing_areas, "wind_speed", "wind_speed")
 
##Wind Copernicus (multiple bands): eastward wind (uwnd)
extract_multiple_raster_poly("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/wind/2007-2019_copernicus", "WIND.nc", fishing_areas, "eastward_wind", "eastward_wind")

##Wind Copernicus (multiple bands): northward wind (vwnd)
extract_multiple_raster_poly("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/wind/2007-2019_copernicus", "WIND.nc", fishing_areas, "northward_wind", "northward_wind")


######
# Getting bathymetry for each region in each row of wind vector data
extract_bathy_poly <- function (raster, poly, final_dir) {
  curr_stack <- raster::stack(raster)
  names(curr_stack) <- "bathy"
  current_data <- extract(curr_stack, poly, fun=sd, na.rm=TRUE, df=TRUE)
  write.csv(current_data, file=paste0(final_dir, "bathy.csv"), row.names = FALSE)
}

fishing_areas1stRow <- shapefile("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/fishing-areas/fishing_areas-1stRow.shp")
fishing_areas2ndRow <- shapefile("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/fishing-areas/fishing_areas-2ndRowWind.shp")
fishing_areasBothRows <- shapefile("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/fishing-areas/fishing_areas-bothRows.shp")

#extract_bathy_poly("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/bathy/BO_bathymean_lonlat.tif", fishing_areasBothRows, "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/bathy/")

