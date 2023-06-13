#TUPLAS modelo 1
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

#print(sorted(lanche)) para organizar em ordem alfabética

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição{cont}') #quando for necessário mostrar a posição ou ..

#for pos, comida in enumerate(lanche):
    #print(f'Eu vou comer {comida} na posição {pos}')

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('Comi pra caramba!')

#TUPLAS modelo 2
a = (2, 5, 4)
b = (7, 8, 9)
c = a + b
print(c)  #não mostrará o cálculo entre as tuplas mas juntará ambas.
#print(len(c)) mostrará o tamanho da tupla, ou seja, unirá ambas.
#print(c.count(5)) mostrará quantas vezes aparece o número 5.
#print(c.index(8)) mostrará a posição do número 8.
#print(c.index(5, 1)) mostrará em que posição o número se encontra a partir da posição 1.

pessoa = ('Ana Paula', 28, 'F', 70)
print(pessoa) #podemos mesclar números com palavras.
del(pessoa) #serve para apagar uma tupla por inteiro, mas não é possível apagar itens. 
