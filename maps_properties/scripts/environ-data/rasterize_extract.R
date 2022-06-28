# Extract values from points vector in a polygon location: U WIND and V WIND

# First: rasterize points
# Second: extract!

library (raster)

windu <- shapefile("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/environ-var/wind/Extract_UWind/Buffer_UWIND_ag_1987.shp")

r.raster <- raster()
extent(r.raster) <- extent(windu)
r <- rasterize(windu, r.raster, field="GRID_CODE", na.rm=TRUE)

plot(r)
mean(r)

x <- extract(r, fishing_areas, fun=mean, na.rm=TRUE, df=TRUE)

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