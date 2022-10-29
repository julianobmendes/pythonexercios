# pythonexercios
# Exercício 10 – Conversor de Moedas
"""
Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira e mostre quantos dólares ela pode comprar.
"""
n1 = float(input('Quantos de Dinheiro para cambio: R$ '))
us = n1 / 3.27
print('Voce pode comprar US$ {:.2f} dolares com R$ {} reais que voce tem'.format(us, n1))
