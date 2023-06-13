#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até 20.
#Seu programa deverá ler um número pelo teclado( entre 0 e 20) e mostrá-lo por extenso.
números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    usuário = int(input('Digite um número entre 0 e 20: '))
    if 0 <= usuário <= 20:
        break
    print('Tente novamente.', end='')
    s = ' '
    while s not in 'SN':
        s = str(input('Quer continuar? [S/N]: ')).strip().upper[0]
    if s == 'N':
        break
    print('Programa finalizado!')
print(f'Você digitou o número {números[usuário]}')


