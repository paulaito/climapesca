from qgis.core import *
import os

### PATH TO FILES
path_europe = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/vector_PtEur/europe.shp"
path_portugal = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/vector_PtEur/portugal.shp"
path_zonespt = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/vector_PtEur/nor_cen_sou.shp"
path_spp = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/hsm/hsm_nc/present/Aantennatus_present_hsm.nc"

### PROJECT
project = QgsProject.instance()
manager = project.layoutManager()

# adjust project coordinate reference system 
crs = QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.PostgisCrsId)
project.setCrs(crs)

### LAYERS 

# creating vector layer objects
vEurope = QgsVectorLayer(path_europe, "europe", "ogr")
vPortugal = QgsVectorLayer(path_portugal, "portugal", "ogr")
vZonesPT = QgsVectorLayer(path_zonespt, "zones", "ogr")

# creating raster layer object
rSpecies = QgsRasterLayer(path_spp, "A. antennatus") # REGEX DEPOIS!!!!

# adding layers:

#species Map
if not rSpecies.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(rSpecies)

#zones PT:
if not vZonesPT.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vZonesPT)

#europe:
if not vEurope.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vEurope)

#portugal:
if not vPortugal.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vPortugal)

### SYMBOLOGY

# change symbology for Portugal layer
renderer_pt = vPortugal.renderer()
symbol_pt = renderer_pt.symbol()
symbol_pt.setColor(QColor.fromRgb(213,202,203))
symbol_pt.symbolLayer(0).setStrokeColor(QColor.fromRgb(174, 174, 174))

# change symbology for Europe layer
renderer_eur = vEurope.renderer()
symbol_eur = renderer_eur.symbol()
symbol_eur.setColor(QColor.fromRgb(213,202,203))
symbol_eur.symbolLayer(0).setStrokeColor(QColor.fromRgb(174, 174, 174))

#change symbology for ZonesPT layer
props = vZonesPT.renderer().symbol().symbolLayer(0).properties()
props['line_color'] = '0,0,0,255'
props['line_style'] = 'dash'
props['line_width'] = 'Hairline'
vZonesPT.renderer().setSymbol(QgsLineSymbol.createSimple(props))
vZonesPT.triggerRepaint() # show the changes

#change symbology for rSpecies: existing style 
rSpecies.loadNamedStyle("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/layout/symbology/style.qml")
rSpecies.triggerRepaint()

### LAYOUT: 

# create layout 

layoutName = "hsm"
layouts_list = manager.printLayouts()
for layout in layouts_list:
    if layout.name() == layoutName:
        manager.removeLayout(layout)
layout = QgsPrintLayout(project)

# initializes default settings and create layout
layout.initializeDefaults()
layout.setName(layoutName)
manager.addLayout(layout)

# load template to layout from file
tmpfile = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/layout/template/hsm_present-rcp.qpt"
with open(tmpfile) as f:
    template_content = f.read()
doc = QDomDocument()
doc.setContent(template_content)

layout.loadFromTemplate(doc, QgsReadWriteContext(), False)

# change label according to specie
specie = "current-spp"
spp = layout.itemById("sp")
spp.setText(specie)

# create page collection
pc = layout.pageCollection()

# resize page to contents
margins = QgsMargins()
pc.resizeToContents(margins, QgsUnitTypes.LayoutMillimeters)

# export  as tif image
base_path = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/final_hsm/draft/"
tif_path = ''.join(base_path + specie + ".tif")
print(tif_path)

exporter = QgsLayoutExporter(layout)
exporter.exportToImage(tif_path, QgsLayoutExporter.ImageExportSettings())