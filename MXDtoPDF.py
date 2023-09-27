import arcpy
import os

# Defina a pasta que contém os arquivos MXD
input_folder = r"R:\09-Banco_De_Dados_Geografico\01-Clientes\Engie\ENGIE R3 ACO\MXD"

# Defina a pasta de saída para os arquivos PDF
output_folder = r"C:\Users\anderson.souza\Downloads\pdf_Teste"

# Defina a resolução máxima para exportação em DPI
max_resolution = 300

# Lista os arquivos MXD na pasta de entrada
mxd_files = [f for f in os.listdir(input_folder) if f.endswith('.mxd')]

# Loop através de cada arquivo MXD
for mxd_file in mxd_files:
    # Crie o caminho completo para o arquivo MXD
    mxd_path = os.path.join(input_folder, mxd_file)
    
    # Abra o arquivo MXD
    mxd = arcpy.mapping.MapDocument(mxd_path)
    
    # Crie um nome para o arquivo PDF de saída
    pdf_output = os.path.splitext(mxd_file)[0] + ".pdf"
    pdf_output_path = os.path.join(output_folder, pdf_output)
    
    # Configure as opções de exportação
    pdf_export = arcpy.mapping.PDFDocumentCreate(pdf_output_path)
    pdf_resolution = max_resolution
    
    # Exporte o MXD para PDF
    arcpy.mapping.ExportToPDF(mxd, pdf_output_path, resolution=pdf_resolution)
    
    # Adicione o PDF exportado ao PDFDocument
    pdf_export.appendPages(pdf_output_path)
    
    # Salve o PDFDocument
    pdf_export.saveAndClose()
    
    # Feche o arquivo MXD
    del mxd

print("Exportação concluída!")
