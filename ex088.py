# pythonexercios
# Exercício 88 – Palpites para a Mega Sena
"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai
sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""
from random import randint
quant = int(input('Quantos jogos você quer gerar? '))
mega = [[] for _ in range(quant)]
for c in range(0, len(mega)):
    while True:
        num = randint(1, 60)
        if num not in mega[c]:
            mega[c].append(num)
        if len(mega[c]) == 6:
            mega[c].sort()
        if len(mega[c]) == 6:
            break
for c in range(0, len(mega)):
    print(f'{mega[c]}')
