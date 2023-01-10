import requests
from bs4 import BeautifulSoup
import re
import csv

#conecta ao yahoo finance
url = 'https://finance.yahoo.com/lookup'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}
website = requests.get(url, headers=headers)
soup = BeautifulSoup(website.text, 'html.parser')

#funcao retorna empresas listadas
def lista_empresas(retorna):
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