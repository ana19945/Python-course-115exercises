#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição
#de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag 999)
n = 0
soma = 0
tentativas = 0
flag = 999
while n != flag:
        n = int(input('Digite um número inteiro: '))
        soma += n
        tentativas += 1
        if n == flag:
                tentativas -= 1
                print('Você digitou {} números tendo um total de {}'.format(tentativas, soma - 999))
