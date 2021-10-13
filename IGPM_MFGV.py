from bs4 import BeautifulSoup
import pandas as pd
from pandas.plotting import table

def Main():
    # Acessando o site

    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError

    url = 'https://www.portalbrasil.net/igpm/'
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

    # Capturando as informações com BeautifulSoup

    # Capturando o Título
    titulo = capturando.findAll('div', {'class': 'lg_01_0_16emcr'}, limit=1)[0].getText()

    # Capturando os dados
    dados = capturando.find(string="Acumulado").parent.parent.parent.parent.getText(' ')
    #dados = capturando.findAll('div', {'class': 'div-mob1'}, limit=1)[0].getText(' ')
    #print(dados)
    # Inserindo o Titulo
    titulo = capturando.find(string="IGP-M/FGV – Fechamento do mês – 2021")

    all_dados = dados[95:136].split()

    all_dados.pop(1)
    all_dados.pop(1)
    all_dados.pop(2)
    filtro = all_dados

    cabecalho = ['Mês/Ano', ' Acumulado nos últimos 12 meses']

    # Criando a tabela no pandas
    tabela = pd.DataFrame(all_dados, cabecalho)

    # Rotacionar a tabela
    tabela = tabela.T

    # Definindo o Mês como o index se a tabela estiver na horizontal
    tabela = tabela.set_index(cabecalho)

    # Exportando para Exel
    tabela.to_excel("shared/IGPM.xlsx")
    #tabela.to_excel("B:\Juridico\Bases\Fatos\IGPM.xlsx")