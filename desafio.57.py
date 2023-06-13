#Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um
#valor correto.
s = 'M' or 'F'
while s == 'M' or 'F':
    s = str(input('Escolha seu sexo: [M/F] ')).upper()
    if s == 'M':
        print('Você digitou {} e seu sexo é Masculino'.format(s))
    if s == 'F':
        print('Você digitou {} e seu sexo é Feminino'.format(s))
    else:
        s != 'M' or 'F'
        print('Digite novamente uma opção válida')

