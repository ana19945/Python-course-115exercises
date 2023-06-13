#Escreva um programa que faça o computador mostrar um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir o número escolhido pelo pc.
#O programa deve mostrar se o usuário venceu ou perdeu
from random import choice
n = int(input('Adivinhe um número entre 0 à 5: '))
lista = [n]
escolhido = choice(lista)
if n <=5:
    print('Você ganhou, Parabéns')
else:
    print('Você perdeu, tente novamente!')
