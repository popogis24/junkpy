from ebird.api import get_nearby_hotspots
import pandas as pd

api_key='r1ks5eh97sv1'
nearby = get_nearby_hotspots(api_key, -27.60, -48.47, dist=50)

tabela_pd = pd.DataFrame(nearby)

print(tabela_pd)

tabela_pd.to_csv('teste1', sep=',', index=False, encoding='utf-8')
