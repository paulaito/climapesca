from qgis.core import *
import os

#base conda 3.8.8 64-bit

# Specify path of shapefiles that will be used to generate the map images
vEuropePath = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/vector_PtEur/europe.shp"
vPortugalPath = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/vector_PtEur/portugal.shp"
vZonesPath = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/vector_PtEur/Sea_area.shp"

# Function to create and export HSM layouts as .tif images
# For 'Difference between...' maps, set title as NULL

def hsm_layout(hsm_dir, final_dir, symbology, template, title, small_title):
    for current_hsm in os.listdir(hsm_dir):
        if current_hsm.endswith(".nc"):
            # new project and layout
            project = QgsProject.instance()
            manager = project.layoutManager()
            
            
            # getting current species name:
            genus = current_hsm[:1]
            specific = (current_hsm.split('_')[0])[1:]
            current_sp = genus + ". " + specific
            
            # adding hsm map
            current_path = hsm_dir + current_hsm
            current_hsm = QgsRasterLayer(current_path, current_sp)
            project.addMapLayer(current_hsm)
            current_hsm.loadNamedStyle(symbology)
            current_hsm.triggerRepaint()
            
            # creating vector layer objects
            vEurope = QgsVectorLayer(vEuropePath, "europe", "ogr")
            vPortugal = QgsVectorLayer(vPortugalPath, "portugal", "ogr")
            vZonesPT = QgsVectorLayer(vZonesPath, "zones", "ogr")
            
            # adding vector layers
            project.addMapLayer(vZonesPT)
            project.addMapLayer(vEurope)
            project.addMapLayer(vPortugal)
            
            # change symbology for ZonesPT layer
            props = vZonesPT.renderer().symbol().symbolLayer(0).properties()
            props['line_color'] = '0,0,0,255'
            props['line_style'] = 'dash'
            props['line_width'] = 'Hairline'
            vZonesPT.renderer().setSymbol(QgsLineSymbol.createSimple(props))
            vZonesPT.triggerRepaint()
            
            # change symbology for Portugal layer
            renderer_pt = vPortugal.renderer()
            symbol_pt = renderer_pt.symbol()
            symbol_pt.setColor(QColor.fromRgb(213,202,203))
            symbol_pt.symbolLayer(0).setStrokeColor(QColor.fromRgb(174, 174, 174))
            vPortugal.triggerRepaint()
            
            # change symbology for Europe layer
            renderer_eur = vEurope.renderer()
            symbol_eur = renderer_eur.symbol()
            symbol_eur.setColor(QColor.fromRgb(213,202,203))
            symbol_eur.symbolLayer(0).setStrokeColor(QColor.fromRgb(174, 174, 174))
            vEurope.triggerRepaint()
            
            # new layout 
            layoutName = "hsm"
            layouts_list = manager.printLayouts()
            for layout in layouts_list:
                if layout.name() == layoutName:
                    manager.removeLayout(layout)
            layout = QgsPrintLayout(project)

            layout.initializeDefaults()
            layout.setName(layoutName)
            manager.addLayout(layout)
            
            # load template 
            with open(template) as f:
                template_content = f.read()
            doc = QDomDocument()
            doc.setContent(template_content)
            
            layout.loadFromTemplate(doc, QgsReadWriteContext(), False)

            ## changing layout items:
            
            # change label according to specie
            spp = layout.itemById("sp")
            spp.setText(current_sp)
            
            if title != NULL:
                layout.itemById("title").setText(title)
            
            # difference '45' or '85'
            if small_title.startswith("diff_rcp45"):
                layout.itemById("rcp").setText("45")
            if small_title.startswith("diff_rcp85"):
                layout.itemById("rcp").setText("85")
            
            # create page collection
            pc = layout.pageCollection()

            # resize page to contents
            margins = QgsMargins()
            pc.resizeToContents(margins, QgsUnitTypes.LayoutMillimeters)

            # export  as tif image
            tif_path = ''.join(final_dir + genus + specific + "_" + small_title + ".tif")
            print(tif_path)

            exporter = QgsLayoutExporter(layout)
            exporter.exportToImage(tif_path, QgsLayoutExporter.ImageExportSettings())
            
            # clear project
            project.removeAllMapLayers()
            project.clear()
        else:
            continue


# applying the function to produce: hsm rcp 45 
hsm = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/hsm/hsm_nc/diff_rcp85/running/"
final = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/FINAL_MAPS/HSM_spp/"
tmp = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/layout/hsm/hsm_template/hsm_diffPT.qpt"
smb = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/layout/hsm/hsm_symbology/style_diff.qml"
ttl = NULL # For 'difference'' maps, set title as NULL
small_ttl = "diff_rcp85PT"

hsm_layout(hsm, final, smb, tmp, ttl, small_ttl)