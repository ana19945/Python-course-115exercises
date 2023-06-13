#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa pergunta o valor da casa, o salário do comprador
#e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
v = float(input('Informe o valor da Casa: '))
s = float(input('Informe o seu salário:  '))
p = int(input('Informe em quantos anos irá pagar a casa: '))
c = v / (p * 12)
mínimo = s * 30 / 100
if c <= mínimo:
   print('Seu empréstimo foi aprovado e você pagará parcelas de R${} mensais'.format(c))
else:
    print('Empréstimo negado')