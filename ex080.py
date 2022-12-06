# pythonexercios
# Exercício 80 – Lista ordenada sem repetições
"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""
lista = []
for c in range(0, 5):
    ler = int(input('Digite um valor: '))
    if len(lista) == 0:
        lista.append(ler)
    for i in range(0, len(lista)):
        if ler not in lista:
            if ler < lista[i]:
                lista.insert((i), ler)
    if ler not in lista:
        lista.append(ler)
print(lista)
