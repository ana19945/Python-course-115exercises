#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles desconsiderando a flag.
n = s = 0
while True:
    n = int(input('Informe um número inteiro: '))
    if n == 999:
        break
    s += n
print(f'A soma dos números é {s}')