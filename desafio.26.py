#Faça um programa que leia uma frase e mostre quantas vezes aparece a letra 'A', em que posição ela aparece a primeira vez e em que posição ela
#aparece a última vez
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vez (es)'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
#O número +1 foi usado para contar a partir da posição 1, ou seja a 1° letra, já que a string conta a partir do espaço, sendo 0
#O rfind é usado para encontrar a letra A a partir do lado direito (right)
