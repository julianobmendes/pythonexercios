# pythonexercios
# Exercício 91 – Jogo de Dados em Python
"""
Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses resultados em um
dicionário em Python. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
game = dict()
print('Valores sorteados:')
for c in range(0, 4):
    game[f'jogador 0{c+1}'] = int(randint(1, 6))
for k, v in game.items():
    print(f'O {k} tirou {v}')
    sleep(2)
sleep(2)
print('Ranking de Jogadores:')
c = 1
for i in sorted(game, key = game.get, reverse=True):
    sleep(2)
    print(f'{c}º lugar o {i} com {game[i]}')
    c += 1
