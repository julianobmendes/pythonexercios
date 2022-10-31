# pythonexercios
# Exercício 68 – Jogo do Par ou Ímpar
"""
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
cont = 0
winner = ['Par','Ímpar']
print('Vamos jogar par ou ímpar!\n[ 1 ] - Ímpar\n[ 2 ] - Par')
while cont != 999:
    num = int(input('Escolha sua sorte: '))
    comp = randint(1, 2)
    resp = (comp + num) % 2
    cont += 1
    if resp == num:
        print('Deu {}, você ganhou!'.format(winner[resp]))
        print('')
    if resp != num:
        print('')
        break
print('Após {} tentativa você não resistiu!!!'.format(cont))
print('Deu {}, você perdeu!'.format(winner[resp]))
