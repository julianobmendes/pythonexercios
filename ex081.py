# pythonexercios
# Exercício 81 – Extraindo dados de uma Lista
"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
while True:
    ler = int(input('Digite um número: '))
    if ler == 0:
        break
    lista.append(ler)
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} valores.')
print(f'Os valores digitados foram:', end="")
for c in range(0, len(lista)):
    print(f' {lista[c]}'if c == 0 else f', {lista[c]}', end="")
print('.')
print(f'O valor cinco esta na lista.'if lista.count(5) >= 1 else f'O valor cinco não foi encontrado.')
