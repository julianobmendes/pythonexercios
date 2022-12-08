# pythonexercios
# Exercício 101 – Funções para votação
"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""
from datetime import date
from typing import Union, Any


def voto(ano):
    """
    ==> Identifica baseado na idade se pode ou não votar
    :param ano: recebe idade
    :return: sem retorno
    by Juliano Boaventura Mendes
    """
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end="")
    if idade >= 65:
        print('Voto OPCIONAL')
    if idade >= 18 <= 64:
        print('Voto OBRIGATÓRIO')
    if idade >= 16 <= 17:
        print('Voto OPCIONAL')
    if idade <= 15:
        print('Voto NEGADO')


voto(int(input('Em que ano você nasceu? ')))
