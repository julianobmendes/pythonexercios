# pythonexercios
# Exercício 79 – Valores únicos em uma Lista
"""
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados, em ordem crescente.
"""
lista = []
while True:
    ler  = int(input('digite um valor'))
    if ler == 0:
        break
    if ler not in lista:
        lista.append(ler)
lista.sort()
print(f'Os valores digitados foram:', end="")
for c in range(0, len(lista)):
    print(f' {lista[c]}'if c == 0 else f', {lista[c]}', end="")
print('.')
 
