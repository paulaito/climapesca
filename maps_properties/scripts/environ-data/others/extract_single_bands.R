# extracting single bands from multiple band raster file

library(raster)

#open your raster with n bands
r<-stack('C:/Users/pa-ak/Downloads/nocs_v2_0_prelim_wspd_2011.nc')
#Plot it just to see if everything is ok
plot(r)
#Check the number of bands
nlayers(r)
for(i in 1:nlayers(r)){
  band<-r[[i]]
  #save raster in a separate file
  writeRaster(band,paste('band',i,'.nc', sep=''))
}


