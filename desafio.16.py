#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
#por exemplo: Digite um número:6.127 - O número 6.127 tem como parte inteira 6

import math
num = float(input('Digite um número: '))
trunc = math.trunc(num)
print ('O número inteiro de {} é igual a {}'.format(num, trunc))
