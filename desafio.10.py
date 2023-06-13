#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.#CONVERSÃO DE MOEDAS
money = float(input('Digite um valor: R$'))
dolar = money / 5.21
print('Com R$ {:.2f} você pode comprar {:.2f} dólares'.format(money, dolar))

