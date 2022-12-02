# pythonexercios
# Exercício 98 – Função de Contador
"""
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
def contador(a, b, c):
    if a < b:
        for c in range(a, b+1, c):
            print(f'{c} ',end="")
        print()
    if a > b:
        for c in range(a, b-1, -c):
            print(f'{c} ', end="")
    
    
contador(1, 10, 1)
contador(10, 0, 2)
