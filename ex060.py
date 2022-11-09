# pythonexercios
# Exercício 60 – Cálculo do Fatorial
"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""
num02 = int(input('Digite um número para saber seu fatorial: '))
num01 = num02
print(('fatorial de {}! = {}').format(num01, num01),end="")
while num02 != 1:
    num02 = num02 - 1
    num01 *= num02
    print(' x {}'.format(num02),end="")
print(' = {}'.format(num01))
