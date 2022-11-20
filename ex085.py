
# pythonexercios
# Exercício 85 – Listas com pares e ímpares
"""
Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valorespares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""
list_all = [[], []]
for c in range(0, 7):
    ler = int(input(f'Digite o {c+1}° valor: '))
    #if len(list_all) == 0:
    #    if ler 
    #    list_all.append(ler)
    for i in range(0, len(list_all)):
        if len(list_all) != 0 and ler % 2 == 0:
            if list_all[i] > ler and ler not in list_all:
                list_all[0].insert(i, ler)
            if list_all[i] < ler and ler not in list_all:
                list_all[0].append(ler)
        if len(list_all) != 0 and ler % 2 == 1:
            if list_all[i] > ler and ler not in list_all:
                list_all[1].insert(i, ler)
            if list_all[i] < ler and ler not in list_all:
                list_all[1].append(ler)
print(list_all)
