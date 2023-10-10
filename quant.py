import arcpy
import os.path
import os
import pandas as pd

arcpy.OverwriteOutput = True

#LT X AREA     
#Utilizado para: Biomas // Processos Minerários // Lei Mata Atlantica // Remanescentes Florestais // Zonas Carsticas
#Potencial Espeleologico // APCB //
arcpy.env.workspace = fr'C:\Users\anderson.souza\Documents\CHESF\Piloto_quantitativo\workspace'

def ltxarea():
    #insira os fields de interesse
    tema = arcpy.GetParameterAsText(0)
    fields_interesse = arcpy.GetParameterAsText(1)
    arcpy.AddMessage(fields_interesse)
    lt = arcpy.GetParameterAsText(2)
    unidade = arcpy.GetParameterAsText(3)
    output = arcpy.GetParameterAsText(4)
    #dissolve o tema com os fields de interesse
    arcpy.Dissolve_management(tema, 'tema_dissolve', fields_interesse)
    #intersecta o tema com o lt
    arcpy.Intersect_analysis([lt, 'tema_dissolve'], 'lt_x_area')
    #cria um field extensao
    arcpy.AddField_management('lt_x_area', 'extensao', 'FLOAT')
    #calcula a extensao da lt (linha)
    if unidade == 'metros':
        arcpy.CalculateField_management('lt_x_area', 'extensao', '!shape.length@meters!', 'PYTHON')
    elif unidade == 'kilometros':
        arcpy.CalculateField_management('lt_x_area', 'extensao', '!shape.length@kilometers!', 'PYTHON')
    elif unidade == 'milhas':
        arcpy.CalculateField_management('lt_x_area', 'extensao', '!shape.length@miles!', 'PYTHON')
    elif unidade == 'pes':
        arcpy.CalculateField_management('lt_x_area', 'extensao', '!shape.length@feet!', 'PYTHON')
    elif unidade == 'jardas':
        arcpy.CalculateField_management('lt_x_area', 'extensao', '!shape.length@yards!', 'PYTHON')
    
    #gera o output
    #deleta todos os fields exceto os de interesse e o field extensao e o field Vertices
    #fields = arcpy.ListFields('lt_x_area')
    #field_names = [field.name for field in fields]
    #fields_to_keep = [fields_interesse, 'extensao', 'Vertices', 'Shape_Length','OBJECTID','Shape']
    #fields_to_drop = [x for x in field_names if x not in fields_to_keep]
    #arcpy.DeleteField_management('lt_x_area', fields_to_drop)
    arcpy.CopyFeatures_management('lt_x_area', output)
    
    arcpy.conversion.ExportFeatures(
        in_features=output,
        out_features='output2',
        where_clause="",
        use_field_alias_as_name="NOT_USE_ALIAS",
        field_mapping='Bioma "Bioma";CD_Bioma "CD_Bioma";extensao "extensao"',
        sort_field=None
    )

ltxarea()
