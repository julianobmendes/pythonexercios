# pythonexercios
# Exercício 96 – Função que calcula área
"""
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
"""
def área(a, b):
    x = a * b
    print(f'A área do terreno {a}m x {b}m é de {x}m²')


print('    Controle de Terrenos')
print('='*28)
larg = float(input('Qual a largura da área? '))
compr = float(input('Qual o comprimento da área? '))
print('-'*28)
área(larg, compr)
