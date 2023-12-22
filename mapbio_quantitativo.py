import arcpy
import os
from arcpy import env
from arcpy.sa import *

arcpy.env.addOutputsToMap = False
arcpy.env.overwriteOutput = True
dataset = r"R:\\09-Banco_De_Dados_Geografico\\01-Clientes\\Neoenergia\\Lote1_24\\GDB_22_12_23\\Dados_Lote6.gdb\\Tracados"
fuso = '23S'
mapbiomas = fr'C:\Users\anderson.souza\Downloads\rtp_mapbiomas_{fuso}.shp'
buff = 40
arcpy.env.workspace = dataset
fclist = arcpy.ListFeatureClasses()

for fc in fclist:
    if fc.startswith('Tracado_'):
        caminho = fr'R:\09-Banco_De_Dados_Geografico\01-Clientes\Neoenergia\Lote1_24\Outros\Quantitativo_Uso_Solo\{fuso}\Buffer'
        filename = 'Uso_Solo_'+fc  
        output = arcpy.analysis.PairwiseBuffer(fc, os.path.join(caminho, filename), buff)
        caminho_clip = fr'R:\09-Banco_De_Dados_Geografico\01-Clientes\Neoenergia\Lote1_24\Outros\Quantitativo_Uso_Solo\{fuso}\Clip'
        clipped = arcpy.analysis.PairwiseIntersect([mapbiomas, output], os.path.join(caminho_clip, filename))
        dissolved = arcpy.analysis.PairwiseDissolve(clipped, os.path.join(caminho_clip,filename+'_diss'),['Classes','Name'])
        arcpy.management.CalculateField(dissolved,'Area_ha','!shape.area@hectares!')
        caminho_excel = r'R:\09-Banco_De_Dados_Geografico\01-Clientes\Neoenergia\Lote1_24\Outros\Quantitativo_Uso_Solo\Planilhas'
        arcpy.conversion.TableToExcel(os.path.join(caminho_clip,filename+'_diss'),os.path.join(caminho_excel,filename+'.xlsx'))
        print(filename +'--- Concluído')
