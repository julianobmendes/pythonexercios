# pythonexercios
# Exercício 61 – Progressão Aritmética v2.0
"""
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
primeiro = int(input("Primeiro elemento: "))
razao = int(input("Razao: "))
n = 0
while n != 10:
    n += 1
    if n != 10:
        print('{} ➜ '.format(primeiro), end="")
    else:
        print('{}'.format(primeiro), end="")
    primeiro = primeiro + razao
