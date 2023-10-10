import arcpy
import os
import os.path

# variavel do raster
raster = arcpy.GetParameterAsText(0)
#variavel do shapefile
shapefile = arcpy.GetParameterAsText(1)
field = arcpy.GetParameterAsText(2)
pasta_output = arcpy.GetParameterAsText(3)


#faça um extract by mask do raster utilizando o cada feição do shapefile usando a coluna nm_utp, e salve cada raster com o nome da feição
with arcpy.da.SearchCursor(shapefile, [field]) as cursor:
    for row in cursor:
        #cria um layer temporario para cada feição
        shapefile1=arcpy.MakeFeatureLayer_management(shapefile, "layer", fr"{field} = '" + row[0] + "'")
        arcpy.gp.ExtractByMask_sa(raster, shapefile1, os.path.join(pasta_output, row[0] + ".tif"))