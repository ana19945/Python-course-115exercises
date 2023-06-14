#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
nome = str(input('Digite o nome do aluno: '))
média = int(input('Digite a média do aluno: '))
inf = {nome, média}
if média >= 7: print(f'{nome} está Aprovado(a) e a média é {média}!')
else:
        print(f'{nome} está Reprovado e a média é {média}!')

