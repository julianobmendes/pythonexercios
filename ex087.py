# pythonexercios
# Exercício 87 – Mais sobre Matriz em Python
"""
Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
matriz = [[], [], []]
for c in range(0, 3):
    for i in range(0, 3):
        num = int(input(f'Digite o {i+1}º número da linha {c+1}'))
        matriz[c].append(num)
print('='*17)
for c in range(0, 3):
    print(f'[ {matriz[c][0]} ] [ {matriz[c][1]} ] [ {matriz[c][2]} ]')
print('='*17)
soma = 0
for c in range(0, 3):
    for i in range(0, 3):
        if matriz[c][i] % 2 == 0:
            soma += matriz[c][i]
print(f'A soma dos pares é {soma}')
print(f'A soma dos valores da terceira coluna é {sum(matriz[2])}')
print(f'E o maior valor da segunda linha é {max(matriz[1])}')
