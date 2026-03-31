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