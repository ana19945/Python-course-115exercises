#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.
km = float(input('Digite km/h rodados: '))
multa = (km - 80) * 7
if km > 80:
    print('Você ultrapassou a velocidade de 80 km/h e pagará R${} em multas'.format(multa))
else:
    print('A velocidade percorrida está dentro do limite e você não será multado')
