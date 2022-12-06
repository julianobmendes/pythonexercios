# pythonexercios
# Exercício 82 – Dividindo valores em várias listas
"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas
os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
listotal = []
lista_par = []
lista_impar = []
print('Digite vários valores inteiros, quando quiser parar digite 0')
while True:
    ler = int(input('Digite um valor: '))
    if ler == 0:
        break
    listotal.append(ler)
    if ler % 2 == 0:
        lista_par.append(ler)
    if ler % 2 != 0:
        lista_impar.append(ler)
print('Os valores digitados foram ', end="")
for t in range(0, len(listotal)):
    print(f'{listotal[t]}'if t == 0 else f', {listotal[t]}', end="")
print('.')
print('Os valores pares são ', end="")
for p in range(0, len(lista_par)):
    print(f'{lista_par[p]}'if p == 0 else f', {lista_par[p]}', end="")
print('.')
print('Os valores ímpares são ', end="")
for i in range(0, len(lista_impar)):
    print(f'{lista_impar[p]}'if i == 0 else f', {lista_impar[i]}', end="")
print('.')
