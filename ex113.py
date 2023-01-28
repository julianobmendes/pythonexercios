# pythonexercios
# Exercício 113 – Funções aprofundadas em Python
"""
Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número
de tipo inválido.
Aproveite e crie também uma função leiaFloat()
com a mesma funcionalidade.
"""

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERROR: Valor digitado não é um número inteiro!')
            continue
        except (KeyboardInterrupt):
            print('ERROR: Usuário preferiu não digitar este número! ')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERROR: Valor digitado não é um número real!')
            continue
        except (KeyboardInterrupt):
            print('ERROR: Usuário preferiu não digitar este número! ')
            return 0
        else:
            return n


n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'O número inteiro foi {n1} e o real foi {n2}.')
