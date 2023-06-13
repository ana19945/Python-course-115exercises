#Elabora um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento
#A vista dinheiro/cheque: 10% de desconto
#A vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros
preço = float(input('Informe o preço do produto: '))
print('''FORMAS DE PAGAMENTO 
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção?: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
    print('Sua compra de R${:.2f} vai custar no final R${:.2f}'.format(preço, total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print('Sua compra de R${:.2f} vai custar no final R${:.2f}'.format(opção, total))
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros'.format(total,parcela))
elif opção == 4:
    total = preço + ( preço * 20 / 100)
    totparc = int(input('Quantas parcelas?: '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totparc, parcela))
    print('Sua compra de R${:.2f} vai custar no final R${:.2f}'.format(preço, total))

