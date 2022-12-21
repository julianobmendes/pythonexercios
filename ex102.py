# pythonexercios
# Exercício 102 – Função para Fatorial
"""
Crie um programa que tenha uma função fatorial()
que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou
não na tela o processo de cálculo do fatorial.
"""


def fatorial(num02, show=False):
    """

    :param num02: recebe o número para calcular o fatorial
    :param show: mostra o calculo do fatorial
    :return: sem retorno
    by Juliano Boaventura Mendes
    """
    num01 = num02
    print(f'fatorial de {num01}! = {num02}' if show == True else f'fatorial de {num01}!', end="")
    while num02 != 1:
        num02 -= 1
        num01 *= num02
        if not show:
            continue
        print(f' x {num02}', end="")
    print(f' = {num01}')


fatorial(5, show=True)
