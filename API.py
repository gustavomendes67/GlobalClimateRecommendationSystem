# Dev 1 (Geolocalização) - Trata a entrada de nomes de cidades e busca as coordenadas/clima.)

import requests


API_KEY = '8e882ea9fbb3b97bbe17f1c764f79674'

def obter_clima(cidade):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br'

    resposta = requests.get(url)
    dados = resposta.json()

    if dados.get('cod') != 200:
        raise ValueError(f'Cidade não encontrada: {cidade}')

    return {
        'cidade': cidade,
        'temperatura': dados['main']['temp'],
        'clima': dados['weather'] [0] ['description']
    }

def obter_cidades():
    while True:
        cidades = input('Digite 5 cidades separadas por vírgula: ').strip().split(',')
        if len(cidades) == 5:
            break
        print("Você não digitou exatamente 5 cidades.")
    dados_cidades = []

    for cidade in cidades:
        try:
            dados = obter_clima(cidade.strip())
            dados_cidades.append(dados)
        except Exception as e:
            print(f'Erro ao buscar cidade: {cidade} -> {e}')

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

dados = obter_cidades()

for d in dados:
    d["classificacao"] = classificar(d)

# Dev 3 e 4 (Relatórios): Cuida da formatação do arquivo de saída e design do gráfico.

def gerar_relatorio_txt(dados):
    with open('relatorio_viagem.txt', 'w') as f:
        f.write("---RELATÓRIO DE VIAGENS MUNDIAIS---\n")
        f.write("-"*35+"\n")
        for item in dados:
            f.write(f"cidade: {item['cidade']:<17} | TEMP: {item['temperatura']}°C | STATUS: {item['classificacao']}\n")
        print("✓Arquivo 'relatorio_viagem.txt' gerado com sucesso!")

# Dev 4: Gráfico de Barras