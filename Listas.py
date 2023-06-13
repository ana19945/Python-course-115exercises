#listas
#lanche.append('1') O COMANDO APPEND ADICIONA NO FINAL DA LISTA
#lanche.insert(0,'1') adiciona o 1 na posição 0
#dellanche[3] apaga o indice 3
#lanche.pop(3) apaga o indice 3
#lanche.remove('pizza') apaga pelo conteúdo e não pela posição em que se encontra
#lanche.pop() apaga o último elemento
#EXAMPLE:
 #if pizza in lanche:
  #lanche.remove('pizza')
#valores = list(range(4,11)) cria uma estrutura organizada
#valores.sort() organiza os valores acima de forma crescente
#valores.sort(reverse=True) organiza os valores acima de forma decrescente

num = [2, 5, 7, 9]
num[2] = 3
num.sort(reverse=True) #coloquei em ordem decrescente
print(num)  #troquei o 7 pelo 3

num = [2, 5, 7, 9]
num[2] = 3
num.append(7) #adiciona o 7
num.sort() #coloquei em ordem crescente
num.insert(0, 1) #na posição 0 adicionei o 1
if 10 in num:
    num.remove(10)
else:
    print('Não achei o número 10')
num.pop(0) #apaguei a posição 0
num.pop()  #apaguei a última posição
print(num) #adicionei o 7 no final da lista
print(f'Essa lista tem {len(num)} elementos.')  #contagem dos elementos da lista.

valores = []
valores.append(2)
valores.append(3)
valores.append(5)

for v in valores:
    print(f'{v}...') #ou print(f'{v}...', end=') para mostrar na horizontal

a = [2, 3, 5, 6, 7]
b = a #junção/ligação de listas
print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [3, 2, 7, 9, 0]
b = a[:] #criando uma cópia da lista a
b[0] = 1
print(f'Lista A: {a}')
print(f'Lista B: {b}')

valores = []
valores.append(2)
valores.append(3)
valores.append(5)

valores = list()
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei no final da lista')
