# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor
n1 = int(input('digite um valor'))
sub = n1 - 1
s = n1 + 1
print('O número é {}, seu antecessor é {} e sucessor é {}'.format(n1, sub, s))
#outra maneira de escrever a solução .format(n1, (n1-1), (n1+1)