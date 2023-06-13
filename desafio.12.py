#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

valor = float(input('Qual é o valor do produto?: R$'))
novo = valor - (valor * 3/100)
print('O produto que custava R$ {}, na promoção com desconto de 3% custa R${}'.format(valor, novo))
