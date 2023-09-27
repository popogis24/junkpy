
# Import arcpy module
import arcpy
import os


# Script arguments
#input_folder = arcpy.GetParameterAsText(0)
input_folder = fr'C:\Users\anderson.souza\Downloads\Base_de_Dados_fev_22\teste' # provide a default value if unspecified

arcpy.env.workspace = input_folder

#definition_query = arcpy.GetParameterAsText(1)
definition_query = "NM_UF In ( 'Bahia', 'Sergipe', 'Alagoas')" # provide a default value if unspecified

#area_interesse = arcpy.GetParameterAsText(2)
area_interesse = fr"R:\09-Banco_De_Dados_Geografico\01-Clientes\ABENGOA\LOTE_6_23\LT_500kV_Xingo_Camacari_II_C1_C2_CD.shp.gdb\Dados_Referenciais\BR_UF_2022_IBGE" # provide a default value if unspecified

#output = arcpy.GetParameterAsText(3)
output = fr'C:\Users\anderson.souza\Downloads\Base_de_Dados_fev_22\teste\meuteste.gdb\dataset'

ai = arcpy.SelectLayerByAttribute_management(area_interesse, "NEW_SELECTION", definition_query)

featureclasses = arcpy.ListFeatureClasses()
print(featureclasses)

for fc in featureclasses:
    selected_fc = arcpy.SelectLayerByLocation_management(fc, "INTERSECT", ai, "", "NEW_SELECTION", "NOT_INVERT")
    if selected_fc is not None:
        #print(selected_fc)
        name = str(fc).replace('.shp','')
        print(name)
        new_fc = arcpy.FeatureClassToFeatureClass_conversion(selected_fc, output, f'{name}', "")

        
feature_classes = arcpy.ListFeatureClasses()
print      
for feature_class in feature_classes:
    # Define o nome do campo de saída para cada atributo de geometria
    area_field = "Area"
    length_field = "Length"

    # Adiciona os campos de saída ao shapefile se eles ainda não existirem
    if not arcpy.ListFields(feature_class, area_field):
        arcpy.AddField_management(feature_class, area_field, "DOUBLE")
    if not arcpy.ListFields(feature_class, length_field):
        arcpy.AddField_management(feature_class, length_field, "DOUBLE")

    # Calcula os atributos de geometria para cada feature class
    arcpy.CalculateGeometryAttributes_management(feature_class, [[area_field, "AREA"], [length_field, "LENGTH"]], "", "SQUARE_METERS", "")
