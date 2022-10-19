# pythonexercios
# Exercício 55 – Maior e menor da sequência
"""Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos."""
maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Digite o peso {}º pessoa: '.format(c+1)))
    if maior == 0 and menor == 0:
        maior = peso
        menor = peso
    elif peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso
print('A pessoa com o maior peso é de {:.2f}kg'.format(maior))
print('A pessoa com o menor peso é de {:.2f}kg'.format(menor))
