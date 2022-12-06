# pythonexercios
# Exercício 93 – Cadastro de Jogador de Futebol
"""
Crie um programa que gerencie o aproveitamento de um
jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de
gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""
jogador = dict()
part = 0
gols = list()
jogador['nome'] = str(input('Nome: '))
part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, part):
    gols.append(int(input(f'Quantos gols na {c+1}º partida?')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('')
print(f'O jogador {jogador["nome"]} jogou {part} partidas.')
for c in range(0, len(gols)):
    print(f'     => Na partida {c+1}, fez {jogador["gols"][c]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
