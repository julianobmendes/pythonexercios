# pythonexercios
# Exercício 103 – Ficha do Jogador
"""
Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um
jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
"""
def ficha(nome='<Desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


nome = str(input('Qual o nome: '))
gols = str(input('Quantos gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)
