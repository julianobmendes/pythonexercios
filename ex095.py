# pythonexercios
# Exercício 95 – Aprimorando os Dicionários
"""
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do
aproveitamento de cada jogador.
"""
jogador = dict()
lista = list()
part = 0
gols = list()
while True:
    jogador['nome'] = str(input('Nome: '))
    part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, part):
        gols.append(int(input(f'Quantos gols na {c+1}º partida?')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    lista.append(jogador.copy())
    gols.clear()
    while True:
        resp = str(input('--== Continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Errou!!! - resposta ( S ou N )')
        print()
    if resp == 'N':
        break
print('-='*20)
print('Cod. ', end="")
for c in jogador.keys():
    print(f'{c:<15}', end="")
print()
print('-'*40)
for k, v in enumerate(lista):
    print(f'{k:>3} ', end="")
    for c in v.values():
        print(f' {str(c):<14}', end="")
    print()
print('-='*20)
while True:
    print('Para encerrar digite "999"')
    part = int(input('Qual jogador quer ver os dados? '))
    if part == 999:
        break
    print('-'*47)
    print(f'---LEVANTAMENTO DO JOGADOR: {lista[part]["nome"]}')
    for c in range(0, len(lista[part]["gols"])):
        print(f'      No jogo {c+1}, fez {lista[part]["gols"][c]} gols.')
    print(f'- Fez um total de {lista[part]["total"]} gols.')
    print(f'- E com uma media de gols de {lista[part]["total"] / len(lista[part]["gols"])} por partida.')
    print('-'*47)
print('Fim do programa.')
