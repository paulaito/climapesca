# Extracting values from raster object at vector data location
# Raster objects: environmental variables (sst, chl, wind)
# Vector data: fishing-areas (Portugal: North(1), Central(2) and South(3))

library (raster)
library (ncdf4)
library(stringr)

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

# Polygon as reference for extraction
fishing_areas<- shapefile("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/fishing-areas/fishing_areas.shp")

variables <- c("wspd", "vwnd", "uwnd")

for (var in variables) {
  dataset <- raster::brick("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/wind/Wind/1988/AG_1988.nc", varname = var)
  year <- str_sub(names(dataset), 2, 5)
  curr_data <- extract(dataset, fishing_areas, fun=mean, na.rm=TRUE, df=TRUE)
  }

dataset <- raster::brick("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/wind/Wind/1988/AG_1988.nc", varname = "wspd")
names <- names(dataset)
year <- str_sub(names, 2, 5)
curr_year <- str_subset(names, pattern = year)
curr_data <- extract(dataset, fishing_areas, fun=mean, na.rm=TRUE, df=TRUE)
