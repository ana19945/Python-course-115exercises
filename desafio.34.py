#Escreva um programa que pergunte um sálario de um funcionário e calcule o aumento do mesmo. Para sálarios superiores a R$1.250,00 aumento de 10%
#Para os inferiores o aumento é 15%
s = float(input('Digite o seu sálario: '))
if s <= 1250:
    novo = s + ( s * 15 / 100)
else:
    novo = s + (s * 10 / 100)
    print(' Quem ganhava R${} passa a ganhar {}.'.format(s, novo))