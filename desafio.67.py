#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando
#o número solicitado for negativo.
m = cont = 0
while True:
    t = int(input('Informe o número da tabuada que deseja consultar: '))
    if t < 0:
        break
    for c in range(1, 11):
        print(f'{t} x {c} = {t * c}')
print('Tabuada encerrada.')

