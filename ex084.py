# pythonexercios
# Exercício 84 – Lista composta e análise de dados
"""
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
list_all = list()
list_leve = list()
list_pesado = list()
while True:
    nome = str(input('Nome: ')).strip()
    peso = float(input('Peso: '))
    if len(list_leve) == 0:
        list_leve.append([nome, peso])
        list_pesado.append([nome, peso])
    else:
        if list_pesado[0][1] <= peso:
            temp = list_pesado[:]
            list_pesado.clear()
            list_pesado.append([nome, peso])
            if list_pesado[0][1] == peso:
                list_pesado.append(temp[0])
        if list_leve[0][1] >= peso:
            temp = list_leve[:]
            list_leve.clear()
            list_leve.append([nome, peso])
            if list_leve[0][1] == peso:
                list_leve.append(temp[0])
    list_all.append([nome, peso])
    result = str(input('--== Continuar? [ S / N ]')).upper()
    if result == 'N':
        break
print(f'Foram {len(list_all)} pessoas cadastradas.'if len(list_all) >= 2 else f'Só 1 pessoa cadastrada')
print(f'Ouve {len(list_leve)} pessoa com peso mais leve de {list_leve[0][1]}kg que é', end="")
for c in range(0, len(list_leve)):
    print(f' {list_leve[c][0]}' if len(list_leve) == 1 else f', {list_leve[c][0]}', end="")
print('.')
print(f'Ouve {len(list_pesado)} pessoa com peso mais pesado de {list_pesado[0][1]}kg que é', end="")
for c in range(0, len(list_pesado)):
    print(f' {list_pesado[c][0]}' if len(list_pesado) == 1 else f', {list_pesado[c][0]}', end="")
print('.')
