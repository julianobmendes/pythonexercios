# pythonexercios
# Exercício 51 – Progressão Aritmética
"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""
primeiro = int(input("Primeiro elemento: "))
razao = int(input("Razao: "))
n = 10
ultimo = primeiro + (n-1)*razao
ultimo = ultimo + 1
for c in range(primeiro, ultimo, razao):
    print('{} '.format(c), end='➞ ')
print('Acabou')
