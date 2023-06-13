#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a)Apenas os primeiros 5 colocados.
#b)Os últimos 4 colocados da tabela.
#c)Uma lista com os times em ordem alfabética.
#d)Em qual posição na tabela está o time da Chapecoense.
s = 0
campeonato = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico', 'Atletico MG', 'Fortaleza', 'Sao Paulo', 'America MG',
              'Bota fogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atletico GO', 'Havai', 'Juventude')
print('--' *30)
print(f'OS 20 PRIMEIROS COLOCADOS SÃO: {campeonato}')
print('--' *30)
print('OS PRIMEIROS 5 COLOCADOS SÃO:', end='')
for c in range(-0, 6, ):
    print({campeonato[c]}, end=', ')
print('--' * 30)
print('OS ÚLTIMOS 4 COLOCADOS SÃO:', end='')
for c in range(-4, 0, ):
    print({campeonato[c]},end=', ')
print(f'--\n' * 0)
print('--' * 30)
print('LISTA DOS TIMES EM ORDEM ALFABÉTICA: ', end='')
for c in range(-0, 20, ):
    print({campeonato[c]}, end=',')
print('--' * 30)
print(f'O TIME FLUMINENSE ESTÁ NA {campeonato.index("Fluminense")+1}°posição')
print('--' * 30)




