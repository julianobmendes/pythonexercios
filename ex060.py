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
    num01 = num02
    print(f'fatorial de {num01}! = {num02}', end="" if show == True else f'fatorial de {num01}!')
    while num02 != 1:
        num02 -= 1
        num01 *= num02
        if show == True:
            print(f' x {num02}', end="")
    print(f' = {num01}')


fatorial(5)
