# pythonexercios
# Exercício 99 – Função que descobre o maior
"""
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
def contador(* num):
    print(f'Analisando os valores passados...')
    for c in range(0, len(num)):
        print(f'{num[c]}, ', end="")
    print(f'foram informados {len(num)} valores ao todo.')
    print(f'O maior valor infomado foi {max(num)}.')


contador(2, 9, 4, 5, 7, 1)
contador(4, 7, 0)
contador(1, 2)
contador(6)
contador(0)
