#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = int(input('Informe km percorrido: '))
dias = float(input('Informe a quantidade de dias: '))
m = (dias * 60.00) + (km * 0.15 )
print ('O veículo percorreu {} km em {} dias, totalizando R$ {:.2f} pelo aluguel'.format (km, dias, m))