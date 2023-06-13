#Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.
a = int(input('Digite o 1° número: '))
b = int(input('Digite o 2° número: '))
c = int(input('Digite o 3° número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
    print('O menor número é {}'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
    print('O maior número é {}'.format(maior))