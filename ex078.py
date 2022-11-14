# pythonexercios
# Exercício 78 – Maior e Menor valores na Lista
"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e
as suas respectivas posições na lista.
"""
lista = []
for c in range(0, 5):
    leia = int(input('Digite um valor: '))
    lista.append(leia)
print(f'O maior valor é {max(lista)} e ele está na posições {(lista.index(max(lista)))+1}')
print(f'O menor valor é {min(lista)} e ele está na posições {(lista.index(min(lista)))+1}')
