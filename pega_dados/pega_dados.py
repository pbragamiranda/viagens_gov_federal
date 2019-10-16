import requests

print('Iniciando o download dos dados')

url = 'http://www.portaltransparencia.gov.br/download-de-dados/viagens/2019'
r = requests.get(url)

with open('/home/blackmamba/Documents/analise_dados/viagens_gov_federal/dados/2019_Viagens.zip', 'wb') as f:
    f.write(r.content)

print('Download concluído com sucesso')

    