#Mostre um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5!= 5x4x3x2x1=120
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))
