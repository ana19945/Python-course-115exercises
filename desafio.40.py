#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5 reprovado
#Média entre 5 e 6.9 recuperação
#Média 7 ou superior aprovado
n1 = float(input('Informe a 1° nota: '))
n2 = float(input('Informe a 2° nota: '))
c = (n1 + n2) / 2
if c < 5:
    print('Sua nota é {} e infelizmente você foi reprovado'.format(c))
elif c == 5 < 6.9:
    print('Sua nota é {} e infelizmente você está em recuperação'.format(c))
else:
    c >= 7
    print('Sua nota é {} e você foi aprovado'.format(c))