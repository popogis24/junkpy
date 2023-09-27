import arcpy
arcpy.env.overwriteOutput = True

codeblock_autoincrement = '''
rec=0
def autoIncrement():
 global rec
 pStart = 1 #muda para nao iniciar do num 1
 pInterval = 1 #mude este numero para mudar o intervalo de seq
 if (rec == 0): 
  rec = pStart 
 else: 
  rec = rec + pInterval 
 return rec
 '''

# Obter os parâmetros de entrada
shapefile = arcpy.GetParameterAsText(0)
nome_coluna_existente = arcpy.GetParameterAsText(1)
nova_coluna = arcpy.GetParameterAsText(2)
lt = arcpy.GetParameterAsText(3)
output = arcpy.GetParameterAsText(4)
workspace = arcpy.GetParameterAsText(5)

arcpy.management.CalculateField(shapefile, 'cont', 'autoIncrement()', "", codeblock_autoincrement, "", "")


# Adicionar a nova coluna à tabela de atributos
arcpy.AddField_management(shapefile, nova_coluna, "TEXT")

# Criar uma lista para armazenar os nomes dos pontos
pontos = []

# Preencher a lista com os nomes de cada ponto
with arcpy.da.SearchCursor(shapefile, [nome_coluna_existente]) as search_cursor:
    for row in search_cursor:
        ponto_nome = row[0]
        pontos.append(ponto_nome)

# Atualizar a nova coluna com a concatenação dos nomes dos pontos adjacentes
with arcpy.da.UpdateCursor(shapefile, [nome_coluna_existente, nova_coluna]) as update_cursor:
    primeiro_ponto = None

    for row in update_cursor:
        ponto_atual = row[0]

        if primeiro_ponto is None:
            primeiro_ponto = ponto_atual
        else:
            concatenacao = f"{primeiro_ponto} - {ponto_atual}"
            row[1] = concatenacao

            update_cursor.updateRow(row)

            primeiro_ponto = ponto_atual

#dissolve a linha e splita linha pelas torres
lt_d = arcpy.management.Dissolve(in_features=lt, out_feature_class='lt_d')
#arcpy.management.SplitLine(in_features=lt_d, out_feature_class=output)
sj_lt_d = arcpy.management.SplitLineAtPoint(in_features=lt_d, point_features=shapefile, out_feature_class='sj_lt_d', search_radius='10 Meters')
#arcpy.management.CalculateField(output, 'cont', 'autoIncrement()', "", codeblock_autoincrement, "", "")

endpoint = arcpy.management.FeatureVerticesToPoints(in_features=output, out_feature_class='endpoint', point_location='END')
sj_endpoint = arcpy.analysis.SpatialJoin(target_features=endpoint, join_features=shapefile, out_feature_class='sj_endpoint', join_operation="JOIN_ONE_TO_ONE",
    join_type="KEEP_ALL",
    match_option="INTERSECT",
    search_radius="10 Meters")

    
arcpy.analysis.SpatialJoin(target_features=sj_lt_d, join_features=shapefile, out_feature_class=output, join_operation="JOIN_ONE_TO_ONE",
    join_type="KEEP_ALL",
    match_option="INTERSECT",
    search_radius="10 Meters")

arcpy.management.JoinField(in_data=output, in_field='cont', join_table=sj_endpoint, join_field='cont')