# Dev 1 (Geolocalização) - Trata a entrada de nomes de cidades e busca as coordenadas/clima.)

import requests

API_KEY = '8e882ea9fbb3b97bbe17f1c764f79674'

def obter_clima(cidade):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br'

    resposta = requests.get(url)
    dados = resposta.json()

    return {
        'cidade': cidade,
        'temperatura': dados['main']['temp'],
        'clima': dados['weather'] [0] ['description']
    }

def obter_cidades():
    cidades = input('Digite 5 cidades separadas por vírgula: ').strip().split(',')

    dados_cidades = []

    for cidade in cidades:
        try:
            dados = obter_clima(cidade.strip())
            dados_cidades.append(dados)
        except:
            print(f'Erro ao buscar cidade: {cidade}')

    return dados_cidades

# Dev 2 (Classificador): Cria as condicionais complexas para os "Status de Viagem".

def classificador_cidade(temp, chuva_mm, condicao):
    condicao = condicao.lower()

    if chuva_mm > 10 or "tempestade" in condicao:
        return "alerta: de chuva forte"
    elif temp <= 5 or "neve" in condicao:
        return "ideal para neve"
    elif 22 <= temp <= 35 and chuva_mm < 5:
        return "ideal para praia"
    else:
        return "clima agradável"

#Dev 3 (Relatórios): Cuida da formatação do arquivo de saída e design do gráfico.
