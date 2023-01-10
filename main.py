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

