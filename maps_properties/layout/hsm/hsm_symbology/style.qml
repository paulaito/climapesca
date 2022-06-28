<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" maxScale="0" hasScaleBasedVisibilityFlag="0" version="3.16.11-Hannover" styleCategories="AllStyleCategories">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal fetchMode="0" mode="0" enabled="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <customproperties>
    <property key="WMSBackgroundLayer" value="false"/>
    <property key="WMSPublishDataSourceUrl" value="false"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="identify/format" value="Value"/>
  </customproperties>
  <pipe>
    <provider>
      <resampling zoomedInResamplingMethod="nearestNeighbour" maxOversampling="2" zoomedOutResamplingMethod="nearestNeighbour" enabled="false"/>
    </provider>
    <rasterrenderer alphaBand="-1" type="singlebandpseudocolor" classificationMax="1" classificationMin="0" nodataColor="" band="1" opacity="1">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader minimumValue="0" colorRampType="INTERPOLATED" maximumValue="1" labelPrecision="2" clip="0" classificationMode="1">
          <colorramp type="gradient" name="[source]">
            <prop v="215,25,28,255" k="color1"/>
            <prop v="43,131,186,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="0.25;253,174,97,255:0.5;255,255,191,255:0.75;171,221,164,255" k="stops"/>
          </colorramp>
          <item alpha="255" color="#d7191c" value="0" label="0.00"/>
          <item alpha="255" color="#fdae61" value="0.25" label="0.25"/>
          <item alpha="255" color="#ffffbf" value="0.5" label="0.50"/>
          <item alpha="255" color="#abdda4" value="0.75" label="0.75"/>
          <item alpha="255" color="#2b83ba" value="1" label="1.00"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" gamma="1" brightness="0"/>
    <huesaturation colorizeStrength="100" grayscaleMode="0" colorizeRed="255" colorizeGreen="128" saturation="0" colorizeBlue="128" colorizeOn="0"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <originalStyle>
    <maplayer refreshOnNotifyEnabled="0" minScale="1e+08" maxScale="0" refreshOnNotifyMessage="" autoRefreshTime="0" type="raster" autoRefreshEnabled="0" hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories">
      <extent>
        <xmin>-38</xmin>
        <ymin>-0.00000000000123634</ymin>
        <xmax>42.99999999967701569</xmax>
        <ymax>74.99999999969999465</ymax>
      </extent>
      <id>Acarbo_present_hsm_1f8e9c77_c719_45ff_b3b2_4d058df99326</id>
      <datasource>../hsm/nc/Acarbo_present_hsm.nc</datasource>
      <keywordList>
        <value/>
      </keywordList>
      <layername>Acarbo_present_hsm</layername>
      <srs>
        <spatialrefsys>
          <wkt/>
          <proj4/>
          <srsid>0</srsid>
          <srid>0</srid>
          <authid/>
          <description/>
          <projectionacronym/>
          <ellipsoidacronym/>
          <geographicflag>false</geographicflag>
        </spatialrefsys>
      </srs>
      <resourceMetadata>
        <identifier/>
        <parentidentifier/>
        <language/>
        <type/>
        <title/>
        <abstract/>
        <contact>
          <name/>
          <organization/>
          <position/>
          <voice/>
          <fax/>
          <email/>
          <role/>
        </contact>
        <links/>
        <fees/>
        <encoding/>
        <crs>
          <spatialrefsys>
            <wkt/>
            <proj4/>
            <srsid>0</srsid>
            <srid>0</srid>
            <authid/>
            <description/>
            <projectionacronym/>
            <ellipsoidacronym/>
            <geographicflag>false</geographicflag>
          </spatialrefsys>
        </crs>
        <extent>
          <spatial crs="" miny="0" maxy="0" maxx="0" minx="0" minz="0" maxz="0" dimensions="2"/>
          <temporal>
            <period>
              <start/>
              <end/>
            </period>
          </temporal>
        </extent>
      </resourceMetadata>
      <provider>gdal</provider>
      <noData>
        <noDataList bandNo="1" useSrcNoData="1"/>
      </noData>
      <map-layer-style-manager current="default">
        <map-layer-style name="default"/>
      </map-layer-style-manager>
      <flags>
        <Identifiable>1</Identifiable>
        <Removable>1</Removable>
        <Searchable>1</Searchable>
      </flags>
      <temporal fetchMode="0" mode="0" enabled="0">
        <fixedRange>
          <start/>
          <end/>
        </fixedRange>
      </temporal>
      <customproperties>
        <property key="WMSBackgroundLayer" value="false"/>
        <property key="WMSPublishDataSourceUrl" value="false"/>
        <property key="embeddedWidgets/count" value="0"/>
        <property key="identify/format" value="Value"/>
      </customproperties>
      <pipe>
        <provider>
          <resampling zoomedInResamplingMethod="nearestNeighbour" maxOversampling="2" zoomedOutResamplingMethod="nearestNeighbour" enabled="false"/>
        </provider>
        <rasterrenderer alphaBand="-1" type="singlebandpseudocolor" classificationMax="1" classificationMin="0" nodataColor="" band="1" opacity="1">
          <rasterTransparency/>
          <minMaxOrigin>
            <limits>None</limits>
            <extent>WholeRaster</extent>
            <statAccuracy>Estimated</statAccuracy>
            <cumulativeCutLower>0.02</cumulativeCutLower>
            <cumulativeCutUpper>0.98</cumulativeCutUpper>
            <stdDevFactor>2</stdDevFactor>
          </minMaxOrigin>
          <rastershader>
            <colorrampshader minimumValue="0" colorRampType="INTERPOLATED" maximumValue="1" labelPrecision="2" clip="0" classificationMode="1">
              <colorramp type="gradient" name="[source]">
                <prop v="215,25,28,255" k="color1"/>
                <prop v="43,131,186,255" k="color2"/>
                <prop v="0" k="discrete"/>
                <prop v="gradient" k="rampType"/>
                <prop v="0.25;253,174,97,255:0.5;255,255,191,255:0.75;171,221,164,255" k="stops"/>
              </colorramp>
              <item alpha="255" color="#d7191c" value="0" label="0.00"/>
              <item alpha="255" color="#fdae61" value="0.25" label="0.25"/>
              <item alpha="255" color="#ffffbf" value="0.5" label="0.50"/>
              <item alpha="255" color="#abdda4" value="0.75" label="0.75"/>
              <item alpha="255" color="#2b83ba" value="1" label="1.00"/>
            </colorrampshader>
          </rastershader>
        </rasterrenderer>
        <brightnesscontrast contrast="0" gamma="1" brightness="0"/>
        <huesaturation colorizeStrength="100" grayscaleMode="0" colorizeRed="255" colorizeGreen="128" saturation="0" colorizeBlue="128" colorizeOn="0"/>
        <rasterresampler maxOversampling="2"/>
        <resamplingStage>resamplingFilter</resamplingStage>
      </pipe>
      <blendMode>0</blendMode>
    </maplayer>
  </originalStyle>
  <blendMode>0</blendMode>
</qgis>
