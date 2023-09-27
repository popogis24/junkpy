import arcpy
import os

def get_shapefiles_recursive(folder_path):
    """Recursively searches for shapefiles in a folder and its subfolders."""
    shapefiles = []
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith('.shp'):
                shapefiles.append(os.path.join(dirpath, filename))
    return shapefiles

def replace_spaces_with_underscores(file_path):
    """Replaces spaces in a file path with underscores."""
    return file_path.replace(' ', '_')

# Script arguments
input_folder = arcpy.GetParameterAsText(0)
if not input_folder:
    input_folder = input('Insira o Caminho da pasta de dados brutos:')

arcpy.env.workspace = input_folder

area_interesse = arcpy.GetParameterAsText(2)
if not area_interesse:
    area_interesse = input ('Insira o caminho da área de interesse em formato de feature class: ')

definition_query = arcpy.GetParameterAsText(1)
if not definition_query:
    definition_query = input('Insira o definition query em SQL (opcional): ')


output = arcpy.GetParameterAsText(3)
if not output:
    output = input('Insira o caminho do feature dataset de saída: ')

ai = arcpy.SelectLayerByAttribute_management(area_interesse, "NEW_SELECTION", definition_query)

featureclasses = get_shapefiles_recursive(input_folder)

for fc in featureclasses:
    selected_fc = arcpy.SelectLayerByLocation_management(fc, "INTERSECT", ai, "", "NEW_SELECTION", "NOT_INVERT")
    if selected_fc is not None:
        name = replace_spaces_with_underscores(os.path.splitext(os.path.basename(fc))[0])
        new_fc = arcpy.FeatureClassToFeatureClass_conversion(selected_fc, output, name, "")
        # Renomeia a feature class com o nome da pasta onde o shapefile foi encontrado
        folder_name = os.path.basename(os.path.dirname(fc))
        new_name = f"{folder_name}_{name}"
        arcpy.Rename_management(new_fc, new_name)
        print (new_name, "- Concluido")

print ('Processo finalizado')