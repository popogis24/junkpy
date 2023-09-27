import arcpy

workspace = arcpy.GetParameterAsText(0)

arcpy.env.workspace = workspace

featureclass = arcpy.ListFeatureClasses()
for fc in featureclass:

    nome_fc=fc
    with arcpy.EnvManager(outputZFlag="Disabled", MDomain=None, outputMFlag="Disabled"):
    fc_new=arcpy.conversion.FeatureClassToFeatureClass(
        in_features=fc,
        out_path=workspace,
        out_name=fr'{fc}_NoZM',
        where_clause="",
        field_mapping="",
        config_keyword=""
    )
    arcpy.management.Delete(
    in_data=fc,
    data_type=""
    )
    arcpy.Rename_management(fc_new, nome_fc)


codeblock_idestagio ='''
def usoestagio(estagio):
    if estagio == ' ':
        return 297
    elif estagio == "Avançado":
        return 277
    elif estagio == 'Médio':
        return 278
    else:
        return 0
    '''




