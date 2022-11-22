# pythonexercios
# Exercício 86 – Matriz em Python
"""
Crie um programa que declare uma matriz de dimensão 3×3 e
preencha com valores lidos pelo teclado. No final,
mostre a matriz na tela, com a formatação correta.
"""
matriz = [[], [], []]
for c in range(0, 3):
    for i in range(0, 3):
        num = int(input(f'Digite o {i+1}º número da linha {c+1}'))
        matriz[c].append(num)
for c in range(0, 3):
    print(f'[ {matriz[c][0]} ] [ {matriz[c][1]} ] [ {matriz[c][2]} ]')
