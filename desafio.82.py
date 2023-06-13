#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.
numeros = list()
pares = list()
ímpares = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print(f'Os números digitados são{numeros}')
print(f'Os números pares são {pares}')
print(f'Os números ímpares são {ímpares}')

