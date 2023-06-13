#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar
n = int(input('Digite um número: '))
c = n % 2
if c == 0:
    print('O número é PAR!'.format(c))
else:
    print('O número é ÍMPAR!')
