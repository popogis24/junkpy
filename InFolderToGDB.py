# Import arcpy module
import arcpy
import os


# Script arguments
#input_folder = arcpy.GetParameterAsText(0)
input_folder = fr'R:\09-Banco_De_Dados_Geografico\01-Clientes\ABENGOA\LOTE_6_23\SHP\Dados_originais' # provide a default value if unspecified

arcpy.env.workspace = input_folder

#definition_query = arcpy.GetParameterAsText(1)
definition_query = "NM_UF In ( 'Bahia', 'Sergipe', 'Alagoas')" # provide a default value if unspecified

#area_interesse = arcpy.GetParameterAsText(2)
area_interesse = fr"R:\09-Banco_De_Dados_Geografico\01-Clientes\ABENGOA\LOTE_6_23\LT_500kV_Xingo_Camacari_II_C1_C2_CD.shp.gdb\Dados_Referenciais\BR_UF_2022_IBGE" # provide a default value if unspecified

#output = arcpy.GetParameterAsText(3)
output = fr'R:\09-Banco_De_Dados_Geografico\01-Clientes\ABENGOA\LOTE_6_23\LT_500kV_Xingo_Camacari_II_C1_C2_CD.shp.gdb\Dados_Referenciais'

ai = arcpy.SelectLayerByAttribute_management(area_interesse, "NEW_SELECTION", definition_query)

listfolder = arcpy.ListWorkspaces()
print(listfolder)

for folder in listfolder:
    
    arcpy.env.workspace = folder
    featureclasses = arcpy.ListFeatureClasses()
    print(featureclasses)
    
    for fc in featureclasses:
        selected_fc = arcpy.SelectLayerByLocation_management(fc, "INTERSECT", ai, "", "NEW_SELECTION", "NOT_INVERT")

        if selected_fc is not None:
            name = str(fc).replace('.shp','')
            print(name)
            new_fc = arcpy.FeatureClassToFeatureClass_conversion(selected_fc, output, f'{name}', "")   
    