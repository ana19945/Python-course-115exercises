#Crie um programa que leia o nome completo de uma pessoa e mostre:
#1.O nome com todas as letras maísculas
#2.O nome com todas minúsculas
#3.Quantas letras sem considerar espaços
#4.Quantas letras tem o primeiro nome

frase = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letra maíscula é: {}'.format(frase.upper()))
print('Seu nome em letra minúscula é: {}'.format(frase.lower()))
print('Seu nome completo sem espaços possui {} letras '.format(len(frase) - frase.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(frase(find(' '))) um modo de encontrar
separa = frase.split()
#split gera listas
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa [0])))
#separa 0 diz respeito ao primeiro nome