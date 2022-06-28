## Shapefile path
vEuropePath = "C:/Users/folder/example/maps/vectors/europe.shp"
vPortugalPath = "Users/folder/example/vectors/portugal.shp"
vZonesPath = "Users/folder/example/vectors/Sea_area.shp"



## HSM_LAYOUT

# applying the function to produce HSM for RCP 45 scenario in English 
hsm = "C:/Users/folder/example/HSM_nc/rcp45/"
final = "C:/Users/folder/example/maps/FINAL_MAPS/HSM/"
tmp = "C:/Users/folder/example/layout-template/hsm_present-rcpEN.qpt"
smb = "C:/Users/folder/example/symbology/style.qml"
ttl = "RCP 45"
small_ttl = "rcp45EN"

hsm_layout(hsm, final, smb, tmp, ttl, small_ttl)

# applying the function to produce HSM for Difference between RCP 85 and Present
# in Portuguese

hsm = "C:/Users/folder/example/HSM_nc/diff_rcp85/"
final = "C:/Users/folder/example/maps/FINAL_MAPS/HSM/"
tmp = "C:/Users/folder/example/layout-template/hsm_diffPT.qpt"
smb = "C:/Users/folder/example/symbology/style_diff.qml"
ttl = NULL
small_ttl = "diff_rcp85PT"

hsm_layout(hsm, final, smb, tmp, ttl, small_ttl)


## MSPEC_LAYOUT

# MAR map images (PT) in a RCP 85 scenario 
mspec = "C:/Users/folder/example/MAR_nc/rcp85/"
final = "C:/Users/folder/example/maps/FINAL_MAPS/MAR/"
tmp = "C:/Users/folder/example/layout-template/mar-spec_present-rcpPT.qpt"
type = "Marginalidade"
ttl = "RCP 85"
small_ttl = "mar_rcp85PT"

mspec_layout(mspec, final, tmp, type, ttl, small_ttl)

# SPEC map images (EN) for DIFF between RCP 45 and Present 
mspec = "C:/Users/folder/example/SPEC_nc/diff_rcp45/"
final = "C:/Users/folder/example/maps/FINAL_MAPS/SPEC/"
tmp = "C:/Users/folder/example/layout-template/mar-spec_diffEN.qpt"
type = "Specialization"
ttl = NULL
small_ttl = "spec_diff_rcp45EN"

mspec_layout(mspec, final, tmp, type, ttl, small_ttl)
