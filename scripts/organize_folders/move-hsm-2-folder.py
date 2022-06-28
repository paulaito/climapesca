# Moving maps to correct species folder

import os 



# Function to create folder for each species
# dir = folder with files containing species' names; final_dir = directory to be created all species' folders
def create_spp_folder(dir, final_dir):
    for file in os.listdir(dir):
        specific = (file.split('_')[0])[0:]
        spfolder = final_dir + specific
        print(spfolder)
        if not os.path.exists(spfolder):
            spfolder = os.makedirs(spfolder)

# Function to move each map to appropriate species folder
# dir = folder containining maps; final_dir = directory containing all species' folders

def move_map2folder(dir, final_dir):
    for filename in os.listdir(dir):
        path_specific = (filename.split('/')[0])[0:]
        specific = filename.split('_')[0][0:] + "/"
        os.rename((dir + filename), (final_dir + specific + filename))

# running function: 

move_map2folder("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/FINAL_MAPS/HSM/", "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/FINAL_MAPS/HSM_spp/")
