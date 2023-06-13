#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salário = float(input('digite seu sálario: '))
novo = salário + (salário * 15 /100)
print('O salário era R${} e com o aumento passou a ser R${}'.format(salário, novo))