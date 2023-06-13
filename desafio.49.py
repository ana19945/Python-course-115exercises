#Refaça o desafio 009 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.
t= int(input('Digite o número da tabuada que deseja consultar: '))
for c in range(0, 10+1):
    print('{} x {:2} = {}'.format(t, c, t*c))
