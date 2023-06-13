teste = list()
teste.append('Ana')
teste.append(29)
galera = list()
galera.append(teste[:])
teste[0] = 'Francisco'
teste[1] = 37
galera.append(teste[:])
print(galera)

turma = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in turma:
    print(p)
    print(p[0]) #para aparecer apenas os nomes e [1] para as idades
    print(f'{p[0]} tem {p[1]} anos de idade')

pessoal = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoal.append(dado[:])
    dado.clear()

for p in pessoal:
    if p[1] >= 21:
        print(f'{p[0]} é o maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')