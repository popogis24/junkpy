import arcpy

# Define os inputs como parâmetros do script
torres = arcpy.GetParameterAsText(0)
#torres = fr'C:\Users\anderson.souza\Downloads\lixo\torres.shp'
lt = arcpy.GetParameterAsText(1)
#lt = fr'C:\Users\anderson.souza\Downloads\lixo\LT.shp'

# Define as variáveis de saída
field_comprimento = arcpy.GetParameterAsText(2)
#field_comprimento = '20'
field_largura = arcpy.GetParameterAsText(3)
#field_largura = '10'
output = arcpy.GetParameterAsText(4) #endereço
#output = fr'C:\Users\anderson.souza\Downloads\lixo\teste_python'

# Processa o buffer das torres
#fr Força string
#temp1 = fr'{output}\temp1.shp'
arcpy.Buffer_analysis(torres, "buff1output", field_comprimento, "FULL", "ROUND", "NONE", "", "PLANAR")


# Processa o intersect
arcpy.Intersect_analysis(["buff1output", lt], "intersect_output", "ALL", "", "INPUT")
#temp = fr'{output}\temp.shp'
#arcpy.analysis.Intersect([temp1, lt], temp, "ALL")

# Processa o buffer da lt
poligono_torres = fr'{output}\poligono_torres.shp'
arcpy.Buffer_analysis('intersect_output', output, field_largura, "FULL", "FLAT", "NONE", "", "PLANAR")

########################################Segunda Etapa###########################################
#feature vertices to points> select layer by location> delete features >