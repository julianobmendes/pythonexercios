# pythonexercios
# Exercício 58 – Jogo da Adivinhação v2.0
"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
computador = randint(1, 10)
result = False
cont = 0
print('Oi sou o computador estou pensando em um número entre 0 e 10')
while not result:
    jogador = int(input('digite seu palpite: '))
    cont += 1
    if jogador == computador:
        result = True
        print('Fim de jogo!!!')
    else:
        if jogador < computador:
            print('Mais... tente de novo')
        if jogador > computador:
            print('Menos... tente de novo')
print('Você levou {} tentativas para acertar'.format(cont))
