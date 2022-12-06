# pythonexercios
# Exercício 73 – Tuplas com Times de Futebol
"""
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""
classe_A = ('Flamengo','Santos','Palmeiras','Grêmio','Athletico-PR','São Paulo',
'Internacional','Corinthians','Fortaleza','Goiás','Bahia','Vasco','Atlético-MG',
'Fluminense','Botafogo','Ceará','Cruzeiro','CSA','Chapecoense','Avaí')
c = 0
print('Os 5 primeiros times na tabela são:', end="")
while c < 5:
    print(f' {classe_A[c]}' if c == 0 else f', {classe_A[c]}', end="")
    c += 1
print('.')
c = 16
print('Os 4 últimos times na tabela são:', end="")
while c < 20:
    print(f' {classe_A[c]}' if c == 0 else f', {classe_A[c]}', end="")
    c += 1
print('.')
c = 0
lista = list(classe_A)
lista.sort()
print('Os times em ordem alfabética são:')
while c < 20:
    print(f'{lista[c]}' if c== 0 else f', {lista[c]}', end="" )
    c += 1
print('.')
print(f'A Chapecoense está na posição: {classe_A.index("Chapecoense")+1} da tabela.')
