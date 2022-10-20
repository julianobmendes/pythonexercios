# pythonexercios
# Exercício 58 – Jogo da Adivinhação v2.0
"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
num01 = randint(1, 10)
result = 0
cont = 1
while result != num01:
    result = int(input('digite um numero de 1 a 10: '))
    if result == num01:
        print('Fim de jogo!!!')
    else:
        cont += 1
print('Você levou {} tentativas para acertar'.format(cont))






'''
from random import randint
from time import sleep

num01 = randint(0, 5)
#num01 = random.choice([0, 1, 2, 3, 4, 5])
num02 = int(input('Desculbra em qual numero\nestou pensando de 0 a 5\ne digite ai pra ver se acerta? '))
print('Procesando...')
sleep(2)
print('Prosesando.....')
sleep(2)
if num01 == num02:
    print('Parabens, voce é um telepata?')
else:
    print('Nao foi dessa vez amiguinho, era {}'.format(num01))
    print('Tentar de novo?')'''
