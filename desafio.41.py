#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SÊNIOR
#ACIMA: MASTER
from datetime import date
year = int(input('Informe seu ano de nascimento: '))
if year >= 2013:
    year = date.today().year
    print('Categoria Mirim'.format(year))
elif year >= 2008:
    print('Categoria Infantil'.format(year))
elif year >= 2003:
    print('Categoria Junior'.format(year))
elif year >= 2002:
    print('Categoria Sênior'.format(year))
else:
    year > 2001
    print('Categoria Master'.format(year))