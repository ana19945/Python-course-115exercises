#Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: BAIXO DO PESO
#Entre 18.5 e 25: PESO IDEAL
#Entre 25 a 30: SOBREPESO
#Entre 30 a 40: OBESIDADE
#Acima de 40: OBESIDADE MÓRBIDA
a = float(input('Informe sua altura: '))
p = float(input('Informe seu peso: '))
imc = p / (a ** 2)
if imc <18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está em seu peso ideal')
elif 25 <= imc < 30:
    print('Você está em sobrepeso')
elif 30 <= imc < 40:
    print('Você está em obesidade')
elif imc >= 40:
    print('Você está em obesidade mórbida, cuidado!')