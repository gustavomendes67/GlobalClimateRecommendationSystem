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

def classificar(dado):
    temp = dado["temperatura"]
    clima = dado["clima"]

    if "chuva" in clima.lower():
        return "Alerta: Chuva Forte"
    elif temp >= 25:
        return "Ideal para praia"
    elif temp <= 10:
        return "Ideal para neve"
    else:
        return "clima agradável"

for d in obter_cidades():
    d["classificacao"] = classificar(d)

#Dev 3 (Relatórios): Cuida da formatação do arquivo de saída e design do gráfico.

def gerar_relatorio_txt(dados_finais):
    with open('relatorio_viagem.txt', 'w') as f:
        f.write("---RELATÓRIO DE VIAGENS MUNDIAIS---\n")
        f.write("-"*35+"\n")
        for item in dados_finais:
            f.write(f"cidade: {item['cidade']:<17} |TEMP: {item['temp']}°C" 
                    f"|STATUS: "f""f"{item['status']}\n")
            print("✓Arquivo 'relatorio_viagem.txt' gerado com sucesso!")
def gerar_grafico_barras(dados_finais):
    cidades=[c['cidade'] for c in dados_finais]
    temperatura=[c['temp']for c in dados_finais]

