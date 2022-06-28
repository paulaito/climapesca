from qgis.core import *
import os

# directory with hsm.nc files 
dir = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/hsm/hsm_nc/rcp45/continue/"

# directory to save .tif 
final_dir = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/final_hsm/rcp45/"
    


for current_hsm in os.listdir(dir):
    if current_hsm.endswith(".nc"):
        # new project and layout
        project = QgsProject.instance()
        manager = project.layoutManager()
        
        # getting current species name:
        genus = current_hsm[:1]
        specific = (current_hsm.split('_')[0])[1:]
        current_sp = genus + ". " + specific
        
        # adding hsm map
        current_path = dir + current_hsm
        current_hsm = QgsRasterLayer(current_path, current_sp)
        QgsProject.instance().addMapLayer(current_hsm)
        current_hsm.loadNamedStyle("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/layout/symbology/style.qml")
        current_hsm.triggerRepaint()
        
        # creating vector layer objects
        vEurope = QgsVectorLayer("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/vector_PtEur/europe.shp", "europe", "ogr")
        vPortugal = QgsVectorLayer("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/vector_PtEur/portugal.shp", "portugal", "ogr")
        vZonesPT = QgsVectorLayer("C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/vector_PtEur/nor_cen_sou.shp", "zones", "ogr")
        
        # adding vector layers
        QgsProject.instance().addMapLayer(vZonesPT)
        QgsProject.instance().addMapLayer(vEurope)
        QgsProject.instance().addMapLayer(vPortugal)
        
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
        template = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/layout/template/hsm_present-rcp.qpt"
        with open(template) as f:
            template_content = f.read()
        doc = QDomDocument()
        doc.setContent(template_content)
        
        layout.loadFromTemplate(doc, QgsReadWriteContext(), False)

        ## changing layout items 
        
        # change label according to specie
        spp = layout.itemById("sp")
        spp.setText(current_sp)
        
        layout.itemById("title").setText("RCP 45")
        
        # create page collection
        pc = layout.pageCollection()

        # resize page to contents
        margins = QgsMargins()
        pc.resizeToContents(margins, QgsUnitTypes.LayoutMillimeters)

        # export  as tif image
        tif_path = ''.join(final_dir + genus + specific + "_rcp45" + ".tif")
        print(tif_path)

        exporter = QgsLayoutExporter(layout)
        exporter.exportToImage(tif_path, QgsLayoutExporter.ImageExportSettings())
        
        # clear project
        project.removeAllMapLayers()
        project.clear()
    else:
        continue
