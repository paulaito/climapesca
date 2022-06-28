from qgis.core import *
import os

#base conda 3.8.8 64-bit

# Specify path of shapefiles that will be used to generate the map images.
vEuropePath = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/vector_PtEur/europe.shp"
vPortugalPath = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/vector_PtEur/portugal.shp"
vZonesPath = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/vector_PtEur/Sea_area.shp"

# Function to create and export MARGINALITY/SPECIALIZATION layouts as .tif images
# For 'Difference between...' maps, set title as NULL

def mspec_layout(mspec_dir, final_dir, template, type, title, small_title):
    n = 0
    for current_mspec in os.listdir(mspec_dir):
        if current_mspec.endswith(".nc"):
            n += 1
            # new project and layout
            project = QgsProject.instance()
            manager = project.layoutManager()
            
            # getting current species name:
            genus = current_mspec[:1]
            specific = (current_mspec.split('_')[0])[1:]
            current_sp = genus + ". " + specific
            
            # adding spec/mar map
            current_path = mspec_dir + current_mspec
            current_mspec = QgsRasterLayer(current_path, current_sp)
            QgsProject.instance().addMapLayer(current_mspec)
            
            # getting stats for further use
            stats = current_mspec.dataProvider().bandStatistics(1, QgsRasterBandStats.All)
            min = stats.minimumValue
            max = stats.maximumValue

            x = (max-min)*1/4 # (max-min) = range

            # converting stats into string to put on layout
            Min = str("{:.2f}".format(min))
            minMid = str("{:.2f}".format(min + x))
            mid = str("{:.2f}".format(min + 2*x))
            midMax = str("{:.2f}".format(min + 3*x))
            Max = str("{:.2f}".format(max))
            
            # adjusting symbology for spec/mar map
            fcn = QgsColorRampShader()
            fcn.setColorRampType(QgsColorRampShader.Interpolated)

            lst = [QgsColorRampShader.ColorRampItem(min, QColor.fromRgb(215,25,28)), 
                    QgsColorRampShader.ColorRampItem(float(minMid), QColor.fromRgb(253,174,97)), 
                    QgsColorRampShader.ColorRampItem(float(mid), QColor.fromRgb(255,255,191)),
                    QgsColorRampShader.ColorRampItem(float(midMax), QColor.fromRgb(171,221,164)),
                    QgsColorRampShader.ColorRampItem(max, QColor.fromRgb(43,131,186))]

            fcn.setColorRampItemList(lst)
            shader = QgsRasterShader()
            shader.setRasterShaderFunction(fcn)

            myPseudoRenderer = QgsSingleBandPseudoColorRenderer(current_mspec.dataProvider(), current_mspec.type(), shader)
            current_mspec.setRenderer(myPseudoRenderer)
            current_mspec.triggerRepaint()
    
            # creating vector layer objects
            vEurope = QgsVectorLayer(vEuropePath, "europe", "ogr")
            vPortugal = QgsVectorLayer(vPortugalPath, "portugal", "ogr")
            vZonesPT = QgsVectorLayer(vZonesPath, "zones", "ogr")
            
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
            layoutName = "mspec"
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
            layout.itemById("sp").setText(current_sp)
            
            # title ("Presente", "RCP 45" or "RCP 85". If you are doing a 'difference' map, set title = NULL)
            if title != NULL:
                layout.itemById("title").setText(title)
            
            # type ("Marginalidade" or "Especialização")
            layout.itemById("type").setText(type)
            
            # statistics: changing min, min-mid, mid, mid-max, max and then change items id
            stats = current_mspec.dataProvider().bandStatistics(1, QgsRasterBandStats.All)
            min = stats.minimumValue
            max = stats.maximumValue
            x = (max-min)*1/4
            # converting starts into string to put on layout
            Min = str("{:.2f}".format(min))
            minMid = str("{:.2f}".format(min + x))
            mid = str("{:.2f}".format(min + 2*x))
            midMax = str("{:.2f}".format(min + 3*x))
            Max = str("{:.2f}".format(max))
            
            #changing stats items 
            layout.itemById("min").setText(Min)
            layout.itemById("min-mid").setText(minMid)
            layout.itemById("mid").setText(mid)
            layout.itemById("mid-max").setText(midMax)
            layout.itemById("max").setText(Max)
            
            # difference '45' or '85'
            if "diff_rcp45" in small_title:
                layout.itemById("rcp").setText("45")
            elif "diff_rcp85" in small_title:
                layout.itemById("rcp").setText("85")
            
            # create page collection
            pc = layout.pageCollection()

            # resize page to contents
            margins = QgsMargins()
            pc.resizeToContents(margins, QgsUnitTypes.LayoutMillimeters)

            # export  as tif image
            tif_path = ''.join(final_dir + genus + specific + "_" + small_title + ".tif")
            print("({})".format(n), tif_path)

            exporter = QgsLayoutExporter(layout)
            exporter.exportToImage(tif_path, QgsLayoutExporter.ImageExportSettings())
            
            # clear project
            project.removeAllMapLayers()
            project.clear()
        else:
            continue


# map production
mspec = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/spec/spec_nc/diff85/running/"
final = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/FINAL/spec/"
tmp = "C:/Users/pa-ak/Documents/UAlg/CLIMA-PESCA/maps/layout/mar-spec/mar-spec_template/mar-spec_diffPT.qpt"
type = "Especialização"
ttl = NULL
small_ttl = "spec_diff_rcp85PT"
# For 'Difference between...' maps, set title as NULL

mspec_layout(mspec, final, tmp, type, ttl, small_ttl)

