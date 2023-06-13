#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50
#por km para viagens de até 200km e R$0,45 para viagens mais longas.
km = float(input('Digite a distância da viagem em km: '))
c = km * 0.50
cc = km * 0.45
if c <= 200:
       print('Você rodou {}km e pagará R${} por essa viagem.'.format(km, c))
elif cc > 200:
    print('Você rodou {}km e pagará R${} por essa viagem.'.format(km, cc))
