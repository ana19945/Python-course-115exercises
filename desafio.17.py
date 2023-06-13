#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento
#da hipotenusa
import math
o = float(input('Digite o comprimento do cateto oposto: '))
a = float(input('Digite o comprimento do cateto adjacente: '))
e = (o * o + a * a) ** (1/2)
print('A medida do cateto oposto é {}, já a medidado do cateto adjacente é {} resultando em {:.0f} da hipotenusa'.format(o , a , e, ))
