import arcpy

workspace = fr"C:\Users\anderson.souza\Documents\RIOS_URBANOS\CORRECAO_DOMINIO\Uso_Solo\Uso_Solo.gdb\Uso_Solo_Bacias"

arcpy.env.workspace = workspace

featureclass = arcpy.ListFeatureClasses()
print(featureclass)

codeblock = '''
def alt(x):
    if x == '9' or x == '12':
        return '15'
    elif x == '10' or x == '11':
        return '11'
    elif x == '16' or x == '15':
        return '12'
    elif x == '14' or x == '17':
        return '13'
    elif x == '2':
        return '16'
    elif x == '1':
        return '1'
    elif x == '3':
        return '3'
    elif x == '4':
        return '6'
    elif x == '5':
        return '4'
    elif x == '6':
        return '5'
    elif x == '7':
        return '7'
    elif x == '8':
        return '8'
    elif x == '13':
        return '9'
    elif x == '18' or x == '19':
        return '14'
    elif x == '20':
        return '16'
    elif x == '21':
        return '10'
    elif x == '22':
        return '2'

    
'''
for fc in featureclass:
    #mostra a ferramenta add field com todos os parametros
    arcpy.management.AddField(
    in_table=fc,
    field_name="class_rev01",
    field_type="TEXT",
    field_precision=None,
    field_scale=None,
    field_length=50,
    field_alias="",
    field_is_nullable="NULLABLE",
    field_is_required="NON_REQUIRED",
    field_domain="Uso_solo_2"
    )
    arcpy.management.CalculateField(
    in_table=fc,
    field="class_rev01",
    expression="alt(!Classificacao!)",
    expression_type="PYTHON3",
    code_block=codeblock,
    field_type="TEXT",
    enforce_domains="ENFORCE_DOMAINS"
    )