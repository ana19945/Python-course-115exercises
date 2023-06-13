#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo entre 1 a 500.

s = 0
cont = 0
for impar in range(1, 500+1, 2):
    if impar % 3 == 0:
        s = s + impar
        cont = cont + 1
print('A soma entre os {} números múltiplos por 3 é {}'.format(cont, s))
