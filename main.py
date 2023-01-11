import requests
from bs4 import BeautifulSoup
import re
import csv

#funcao organiza lista de valores
def org_valores(lista):
    nova_lista = list()
    for items in lista:
        if len(items) != 0:
            for item in items:
                nova_lista.append(item)
        else:
            nova_lista.append('N/A')
    return(nova_lista)

#funcao conecta ao yahoo finance
def conecta_lookup():
    url = 'https://finance.yahoo.com/lookup'
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}
    website = requests.get(url, headers=headers)
    soup = BeautifulSoup(website.text, 'html.parser')
    return(soup)

#funcao conecta aos dados de uma empresa
def conecta_empresa(simbolo):
    url = f'https://finance.yahoo.com/quote/{simbolo}?p={simbolo}'
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}
    website = requests.get(url, headers=headers)
    soup = BeautifulSoup(website.text, 'html.parser')
    return(soup)

#funcao retorna empresas listadas
def lista_empresas(retorna):
    soup = conecta_lookup()
    simbolos = list()
    nomes= list()

    for item in soup.find_all(attrs={'class':'data-col0'}):
        simbolo = re.findall('">([A-Z]+?)<\/a><\/td>', str(item))
        simbolos.append(simbolo)
    
    for item in soup.find_all(attrs={'class':'data-col1'}):
        nome = re.findall('">(.*?)<\/td>', str(item))
        nomes.append(nome)

    nomes = [x for item in nomes for x in item]
    simbolos = [x for item in simbolos for x in item]

    if retorna == 'simbolo':
        return(simbolos)
    elif retorna == 'tudo':
        return(simbolos, nomes)
    elif retorna == 'nome':
        return(nomes)

#funcao pesquisa uma empresa
def pesquisa(simbolo, return_csv=False):
    soup = conecta_empresa(simbolo)
    valores = [[simbolo]]

    for items in soup.find_all(id='quote-summary'):
        for item in items.select('tr'):
            key = re.findall('W\(51%\)"><span>(.*?)<\/span>', str(item))

            if key[0] == 'Earnings Date':
                value = re.findall('data-test="EARNINGS_DATE-value"><span>(.*?)<\/span> - <span>(.*?)<\/span>', str(item))
            elif key[0] == 'Ex-Dividend Date':
                value = re.findall('data-test="EX_DIVIDEND_DATE-value"><span>(.*?)<\/span>', str(item))
            elif key[0] == 'Volume':
                value = re.findall('value="(.*?)"', str(item))
            else:
                value = re.findall('data-test="(?:.*)">(.*?)</td>', str(item))
            
            valores.append(value)
    valores = org_valores(valores)
    
    if return_csv == False:
        return(valores)
    elif return_csv == True:
        head = ['Previous Close', 'Open', 'Bid', 'Ask', "Day's Range", '52 Week Range', 'Volume', 'Avg. Volume', 'Market Cap', 'Beta (5Y Monthly)', 'PE Ratio (TTM)', 'EPS (TTM)', 'Earnings Date', 'Forward Dividend & Yield', 'Ex-Dividend Date', '1y Target Est']
        with open('data.csv', 'w') as file:
            writer = csv.writer(file)

            writer.writerow(head)
            writer.writerow(valores)

#funcao pesquisa todas as empresas
def pesquisa_todas(return_csv=False):
    simbolos = lista_empresas('simbolo')

    if return_csv == True:
        head = ['Previous Close', 'Open', 'Bid', 'Ask', "Day's Range", '52 Week Range', 'Volume', 'Avg. Volume', 'Market Cap', 'Beta (5Y Monthly)', 'PE Ratio (TTM)', 'EPS (TTM)', 'Earnings Date', 'Forward Dividend & Yield', 'Ex-Dividend Date', '1y Target Est']
        open_csv = open('data.csv', 'w')
        writer = csv.writer(open_csv)
        writer.writerow(head)

        for simbolo in simbolos:
            temp = pesquisa(simbolo)
            writer.writerow(temp)

        open_csv.close()
    elif return_csv == False:
        data = dict()
        for simbolo in simbolos:
            data[simbolo] = pesquisa(simbolo)
        return(data)