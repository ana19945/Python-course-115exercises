#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
ângulo = float (input('Digite o ângulo que deseja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o Seno de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print(' O ângulo de {} tem o cosseno de {:.2f}'.format(ângulo,cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))

