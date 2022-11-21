# pythonexercios
# Exercício 85 – Listas com pares e ímpares
"""
Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""
list_all = [[], []]
for c in range(0, 7):
    ler = int(input(f'Digite o {c+1}° valor: '))
    if ler % 2 == 0:
        list_all[0].append(ler)
    if ler % 2 == 1:
        list_all[1].append(ler)
list_all[0].sort()
list_all[1].sort()
print('Os números pares são:', end="")
for c in range(0, len(list_all[0])):
    print(f' {list_all[0][c]}', end="")
print('.')
print('Os números ímpares são:', end="")
for c in range(0, len(list_all[1])):
    print(f' {list_all[1][c]}', end="")
print('.')
