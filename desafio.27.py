#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('O primeiro nome é {}'.format(nome[0]))
print('O último nome é {}'.format(nome[len(nome)-1]))

