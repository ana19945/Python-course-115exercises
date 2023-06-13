#Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo
a = int(input('\033[1:31:40m Digite o comprimento a: \033[m '))
b = int(input('Digite o comprimento b: '))
c = int(input('Digite o comprimento c: '))
s = a + b
if s > c:
    print('O triângulo mede {}cm e é possível formá-lo!'.format(s))
else:
    s < c
    print('O triângulo não pode ser formado')