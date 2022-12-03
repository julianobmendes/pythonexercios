# pythonexercios
# Exercício 100 – Funções para sortear e somar
"""
Faça um programa que tenha uma lista chamada números e
duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre
todos os valores pares sorteados pela função anterior.
"""
from random import randint
from time import sleep
def sorteia(lst, quant):
    for c in range(quant):
        lst.append(randint(1, 10))
    print(f'Sorteando {quant} valores para a lista: ', end="")
    for c in range(0, 5):
        print(f'{lst[c]} ', end="")
        sleep(.5)
    print()


def somaPar(lst):
    p = 0
    for c in lst:
        if c % 2 == 0:
            p += c
    print(f'Somando os valores pares de {lst}, temos o valor {p}')


numeros = list()
sorteia(numeros, 5)
somaPar(numeros)
