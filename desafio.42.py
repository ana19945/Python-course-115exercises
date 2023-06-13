#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes
r1 = float(input('Informe a 1° medida do triângulo: '))
r2 = float(input('Informe a 2° medida do triângulo: '))
r3 = float(input('Informe a 3° medida do triângulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isósceles')