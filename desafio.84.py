#faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#a)Quantas pessoas foram cadastradas
#b)Uma listagem com as pessoas mais pesadas
#c)Uma listagem com as pessoas mais leves
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='* 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men}kg. Peso de', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()




