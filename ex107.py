# pythonexercios
# Exercício 107 – Exercitando módulos em Python
"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e
use algumas dessas funções.
"""
from ex107 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13% temos {moeda.diminuir(p, 13)}')

def aumentar(num, porc):
    """
    -> Função de soma porcentagem ao valor.
    :param num: valor a ser aumentado.
    :param porc: porcentagem a ser aumentada no valor.
    :return: 'resp' = recebe a soma entre 'num' e 'porc'
    """
    resp = (porc * num) / 100
    return num + resp


def diminuir(num, porc):
    """
    -> Função de retirar porcentagem ao valor.
    :param num: valor a ser diminuido.
    :param porc: porcentagem a ser retirada no valor.
    :return: 'resp' = recebe 'num' menos 'porc'
    """
    resp = (porc * num) / 100
    return num - resp


def dobro(num):
    """
    -> Função para dobra o valor.
    :param num: recebe o valor a ser somado.
    :return: 'num' multiplicada por ele mesmo.
    """
    resp = num + num
    return resp


def metade(num):
    """
    -> Função para dividir um valor.
    :param num: recebe o valor a ser dividido.
    :return: 'num' dividido por dois
    """
    resp = num / 2
    return resp
