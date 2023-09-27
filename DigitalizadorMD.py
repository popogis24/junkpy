import re

POINT = 'vértice'
P = 0
Y = 'N'
X = 'E'

# Expressões regulares para buscar coordenadas com espaço antes do 'E' e 'N'
RE_Y = r'(\d+,\d+\s+{})'.format(Y)
RE_X = r'(\d+,\d+\s+{})'.format(X)

def extract(line):
    global P
    
    if line is None:
        return
    
    g1 = re.search(RE_Y, line)
    g2 = re.search(RE_X, line)
    
    if g1 is None or g2 is None:
        return 
    
    g1 = g1.group(1).replace(Y, '').replace(',', '.')
    g2 = g2.group(1).replace(X, '').replace(',', '.')
    
    print('{} {};{};{}'.format(POINT, P, g1, g2))
    
    P = P + 1
        
    
if __name__ == '__main__':
    file = open(r'C:\Users\anderson.souza\Downloads\teste\teste.txt', encoding='utf-8')
    text = file.readlines()
    points = text[0].split(';')
    
    for point in points:
        extract(point)
