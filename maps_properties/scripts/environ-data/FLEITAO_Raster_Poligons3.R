
#######################

#Meanwhile I found a solution to my issue.
#First I had to uninstall the "tidyr" package because there was a conflict with the extract() function.


#https://community.rstudio.com/t/extract-raster-pixels-values-using-vector-polygons-in-r/59468/3

#https://www.rdocumentation.org/packages/raster/versions/3.4-13/topics/extract

#https://gis.stackexchange.com/questions/102870/step-by-step-how-do-i-extract-raster-values-from-polygon-overlay-with-q-gis-or
#https://www.neonscience.org/resources/learning-hub/tutorials/extract-values-rasters-r

1#video: https://www.youtube.com/watch?v=eXYf2INzOdM
2#https://rpubs.com/rural_gis/254726


library (raster) 
library (rgdal)
library (sp)
library (ncdf4)




#STEP 1 Extract the values of the pixels raster per area for 1 NC

ras=raster("D:/d1/Ualg_ICCE/Projectos/CLIMFISH/Divulgacao/Filme/TemperaturaMar_2006_2070/entrada/2006.nc")

ras=raster("E:/SDM_CLIMFISH/Extract_TSeries/Raster/2006.nc")


#read-in the polygon shapefile

poly<- shapefile("E:/SDM_CLIMFISH/Extract_TSeries/SST_RCP45.shp")


ext <- extract(raster.fd, poly, method="simple")

ext1 <- extract(ras, poly, Fun = "mean") 

ext2 <- raster::extract(ras, poly)

ex <- extract(ras, poly, fun=mean, na.rm=TRUE, df=TRUE)

plot(poly)



#with function Line 99

ex <- extract(ras, poly, fun=our_fun, na.rm=TRUE, df=TRUE)
ex <- extract(ras, poly, fun=our_fun)

#STEP2 #######################batch potencial process#################### all in the directory ## Multiple-raster.nc

#list files (in this case raster)



raster.dir <- "E:/SDM_CLIMFISH/Extract_TSeries/Raster"
grids <- list.files(raster.dir, pattern = ".nc", full.names=TRUE) #replace pattern ".nc" with whatever file ending you use, p.e. ".tif" or ".grd" "asc"
grids

#check the number of files in the raster list (grids)
length <- length(grids)

raster.fd <- raster::stack(grids)
names(raster.fd)



#read-in the polygon shapefile

poly<- shapefile("E:/SDM_CLIMFISH/Extract_TSeries/SST_RCP45.shp")



#extract raster cell count (sum, min, max, mean, count) within each polygon area (poly)
for (i in 1:length(grids)){
  ex <- extract(raster.fd, poly, fun=mean, na.rm=TRUE, df=TRUE)
}

#write to a data frame
df <- t(data.frame(ex))


#write to a CSV file
setwd(raster.dir)

variable <- "SST_RCP45_monthly"

write.csv(df, file=paste0(variable, "_mean.csv"))


getwd()

t(df)


#function1


our_fun <- function(x,na.rm = TRUE)
{
  avg = mean(x)
  all = length(x)# number of cells inside each polygon
  more_than_avg = sum(x>avg) # number of cells with value higher than the mean in each polygon
  prc = (more_than_avg/all)*100 # percentage of value higher than the mean in each polygon
  return(prc)
}
  


#function2
our_fun <- function(x,na.rm = TRUE)
{
  avg = mean(x)
  mini =  min (x)
  maxi =  max (x)
  desviop = sd(x)
}



#STEP3 #######################batch potencial process#################### all in the directory ## Multiple-raster.nc
## EXTRACT SDM information
#list files (in this case raster)



raster.dir <- "E:/RCP45_differences_HSM"
raster.dir <- "E:/RCP85_differences_HSM"

grids <- list.files(raster.dir, pattern = ".nc", full.names=TRUE) #replace pattern ".nc" with whatever file ending you use, p.e. ".tif" or ".grd" "asc"
grids

#check the number of files in the raster list (grids)
length <- length(grids)

raster.fd <- raster::stack(grids)
names(raster.fd)



#read-in the polygon shapefile

poly<- shapefile("E:/SDM_CLIMFISH/Extract_TSeries/SST_RCP45.shp")



#extract raster cell count (sum, min, max, mean, count) within each polygon area (poly)
for (i in 1:length(grids)){
  ex <- extract(raster.fd, poly, fun=max, na.rm=TRUE, df=TRUE)
}

#write to a data frame
df <- t(data.frame(ex))


#write to a CSV file
setwd(raster.dir)

variable <- "RCP85_diff_max"

write.csv(df, file=paste0(variable, ".csv"))


getwd()

t(df)






















# My Script to all in one using one dataset


coords <- read.csv("D:/d1/Ualg_ICCE/Alunos_Teses/Doutoramentos/Doutoramento_Vania/ProducaoCintifica/Habitats/V2/coords_extended_batimetria_igo1.csv", check.names = FALSE)


coords <- coords %>% gather(longitude, bathymetry, -latitude) %>%
  mutate(longitude = gsub("x", "", longitude))



write.csv(coords, "D:/d1/Ualg_ICCE/Alunos_Teses/Doutoramentos/Doutoramento_Vania/ProducaoCintifica/Habitats/V2/lat_long_bat_RiaFormosaFinal.csv")







#######################for points data ##################


# LOAD IN LOCAL DATA FROM DIRECTORIES  
#FROM ESRI SHAPEFILE
point.path <- "D:/d1/Ualg_ICCE/Alunos_Teses/Doutoramentos/Doutoramento_Vania/ProducaoCintifica/Habitats/batimetria_rf"
points <- rgdal::readOGR(dsn = dirname(point.path), layer = basename(point.path))


#RASTER FROM .NC (With Points) 
## single raster
raster.path <- "D:/ENVIRONMENTAL/cla/A20090012009031.L3m_MO_CHL_chlor_a_4km.nc"
raster.fp <- raster::raster(raster.path)


plot(raster.fp)
points(points)

pts.fp <- extractPointFromRaster(raster.fp, points)
head(pts.fp@data)
summary(pts.fp)


## all in the directory ## Multiple-raster.nc

raster.dir <- "D:/ENVIRONMENTAL/cla/"
raster.names <- list.files(raster.dir, pattern = ".nc", full.names=TRUE) #replace pattern ".nc" with whatever file ending you use, p.e. ".tif" or ".grd"
raster.names

raster.fd <- raster::stack(raster.names)
names(raster.fd)

pts.fd <- extractPointFromRaster(raster.fd, points)
pts.fd@data %>% colnames()

pts.fd@data %>% head()

#extract data into dir

rgdal::writeOGR(pts.fd, getwd(), "extractPR", driver="ESRI Shapefile")
write.csv(pts.fd@data, "extractPR.csv")




#####vento## Future: 2040-2049; 2010-2019

raster.dir <- "E:/RCP45_differences_HSM"
raster.names <- list.files(raster.dir, pattern = ".nc", full.names=TRUE) #replace pattern ".nc" with whatever file ending you use, p.e. ".tif" or ".grd"
raster.names

write.csv(raster.names,"rcp45.csv")


upresent <- "uas_EUR-11_MPI-M-MPI-ESM-LR_RCA4.Portugal.rcp45.2010-2019.nc"
urcp45future <- "uas_EUR-11_MPI-M-MPI-ESM-LR_RCA4.Portugal.rcp45.2040-2049.nc"
urcp85future <- "uas_EUR-11_MPI-M-MPI-ESM-LR_RCA4.Portugal.rcp85.2040-2049.nc"
vpresent <- "vas_EUR-11_MPI-M-MPI-ESM-LR_RCA4.Portugal.rcp45.2010-2019.nc"
vrcp45future <- "vas_EUR-11_MPI-M-MPI-ESM-LR_RCA4.Portugal.rcp45.2040-2049.nc"
vrcp45future<- "vas_EUR-11_MPI-M-MPI-ESM-LR_RCA4.Portugal.rcp85.2040-2049.nc"


RCP45_differences <- upresent - urcp45future
RCP45_differences <- upresent - urcp85future

RCP45_differences <- vpresent - vrcp45future
RCP45_differences <- vpresent - vrcp85future









