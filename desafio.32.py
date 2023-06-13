#Faça um programa que leia um ano qualquer e mostre se ele é bissexto
#Para analisar o ano atual em python basta importar a biblioteca datetime
from datetime import date
year = int(input('Digite o ano que deseja analisar:  ou digite 0 verificar o ano atual: '))
if year == 0:
   year = date.today().year
#Cálculo abaixo para verificar se o ano é bissexto ou não
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} é bissexto'.format(year))
else:
    print('O ano {} não é bissexto'.format(year))
