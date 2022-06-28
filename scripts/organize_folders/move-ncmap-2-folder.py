import os
import shutil

# elif = quando o objeto de cada de interação se encaixa com apenas uma das condicionais.
# dessa maneira, assim que a condicional do objeto é correspondida, a ação é executada e
# pula para a próxima iteração, sem ter que passar pelas outras condicionais.

# Moving present, rcp45 and rcp85 .nc files to appropriate folder
#dir1 = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/hsm/hsm_nc/"

for filename in os.listdir(dir1):
    if filename.endswith("present_hsm.nc"): 
         os.rename((dir1 + filename), ("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/hsm/hsm_nc/present/" + filename))
    elif filename.endswith("rcp45_hsm.nc"):
        os.rename((dir1 + filename), ("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/hsm/hsm_nc/rcp45/" + filename))
    elif filename.endswith("rcp85_hsm.nc"):
        os.rename((dir1 + filename), ("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/hsm/hsm_nc/rcp85/" + filename))

dir = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/spec/nc/"

# Moving marginality and specialization .nc files to appropriate folder
def moveMarSpec2folder(dir, final_dir):
    for filename in os.listdir(dir):
        if filename.endswith("rcp45_li_Mar.nc") or filename.endswith("rcp45_li_Spec1.nc"): 
            os.rename((dir + filename), (final_dir + "rcp45/" + filename))
        elif filename.endswith("rcp85_li_Mar.nc") or filename.endswith("rcp85_li_Mar.nc"):
            os.rename((dir + filename), (final_dir + "rcp85/" + filename))
        elif filename.endswith("li_Mar.nc") or filename.endswith("li_Spec1.nc"):
            os.rename((dir + filename), ((final_dir + "present/" + filename)))

moveMarSpec2folder(dir, dir)

# Moving difference files to appropriate folder
#dir2 = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/hsm/hsm_nc/diff/"
#for filename in os.listdir(dir2):
#    if filename.endswith("rcp45.nc"): 
#         os.rename((dir2 + filename), ("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/hsm/hsm_nc/diff/diff_rcp45/" + filename))
 #        continue
  #  elif filename.endswith("rcp85.nc"):
   #     os.rename((dir2 + filename), ("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/hsm/hsm_nc/diff/diff_rcp85/" + filename))


