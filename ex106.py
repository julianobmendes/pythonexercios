# pythonexercios
# Exercício 106 – Interactive helping system in Python
"""
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
Importante: use cores.
"""
from time import sleep
cor = ( \033[m',        # 0 - sem cor
        \033[0;30;41m', # 1 - vermelho
        \033[0;30;42m', # 2 - verde
        \033[0;30;43m', # 3 - amarelo
        \033[0;30;44m', # 4 - azul
        \033[0;30;45m', # 5 - roxo
        \033[7;30m',    # 6 - branco
        );


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(cor[6], end='')
    help(com)
    print(cor[0], end='')
    sleep(2)


def titulo(msg, c=0):
    tam = len(msg) + 4
    print(cor[c], end='')
    print('~' * tam)
    print(f'')
    print('~' * tam)
    print(cor[0], end='')
    sleep(1)


# Programa Principal:
comando = ''
while True:
    comando = str(input('Função ou Biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
