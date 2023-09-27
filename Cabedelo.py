import csv

# Abrir o arquivo CSV para leitura
with open(fr'R:\09-Banco_De_Dados_Geografico\01-Clientes\Porto_Cabedelo\EXCEL\Deslocamento_draga\ONVAC DIEZ\MAIO\Percurso_omvac_07_05_a_13_05_teste.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    # Ler as linhas do arquivo CSV
    linhas = list(leitor_csv)

    # Imprimir o cabeçalho
    print(linhas[0])

    # Obter os índices das colunas "Latitude" e "Longitude"
    indice_latitude = linhas[0].index('Latitude')
    indice_longitude = linhas[0].index('Longitude')

    # Iterar sobre as linhas e extrair os valores de "Latitude" e "Longitude"
    for linha in linhas[1:]:
        latitude = linha[indice_latitude]
        longitude = linha[indice_longitude]

        # Fazer o que desejar com os valores de latitude e longitude
        print(f"Latitude: {latitude}, Longitude: {longitude}")
