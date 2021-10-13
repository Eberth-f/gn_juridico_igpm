from bs4 import BeautifulSoup
import pandas as pd

def Main():
    # Acessando o site
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError

    url = 'https://www.portalbrasil.net/ipca/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

    # identificando o erro

    try:
        req = Request(url, headers=headers)
        response = urlopen(req)
        # print(response.read())
        html = response.read()

    except HTTPError as e:
        print(e.status, e.reason)

    except URLError as e:
        print(e.reason)

    html.split()

    # Convertendo Bytes para String

    # convertendo
    html = html.decode('utf-8')

    # Inserindo espaços
    " ".join(html.split())

    # Removendo caracteres especiais
    def trata_html(input):
        return " ".join(input.split()).replace('> <', '><').replace('\n', ' ')

    # Transferindo para outra variavel
    html = trata_html(html)

    # Transformando para um objeto BeautifulSoup
    capturando = BeautifulSoup(html, 'html.parser')

    # Capturando as informações com BeautifulSoup¶
    dados = capturando.find(string="Acumulado").parent.parent.parent.parent.parent.getText(' ')

    indice = dados.index('12 meses')
    indice += 9
    dados[indice]

    dados_atual = dados[indice:indice + 38]

    # Criando um dicionário
    all_dados = dados_atual.split()

    all_dados.pop(1)
    all_dados.pop(1)
    all_dados.pop(2)

    cabecalho = ['Mês/Ano', ' Acumulado nos últimos 12 meses']
    cabecalho

    # Criando a tabela no pandas
    tabela = pd.DataFrame(all_dados, cabecalho)

    # Rotacionar a tabela
    tabela = tabela.T

    # Definindo o Mês como o index se a tabela estiver na horizontal
    tabela = tabela.set_index(cabecalho)

    tabela.to_excel("shared/IPCA.xlsx")
    #tabela.to_excel("B:\Juridico\Bases\Fatos\IPCA.xlsx")