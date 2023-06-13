#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
opção = 0
while opção != 5:
    print('''Opções:
    [ 4 ] Somar
    [ 3 ] Multiplicar
    [ 2 ] Identificar Maior
    [ 1 ] Novos números
    [ 0 ] Sair do programa ''')
    opção = int(input('Digite o número da opção desejada: '))
    if opção == 4:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2,soma))
    elif opção == 3:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 2:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 1:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 0:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
    print('Fim do programa! Volte sempre!')