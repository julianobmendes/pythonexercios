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
from time import sleep
def contador(a, b, c):
    print('-='*16)
    if a < b:
        print(f'Contagem de {a} até {b} de {c} em {c}')
        for c in range(a, b+1, c):
            print(f'{c} ',end="")
            sleep(1)
        print()
    if a > b:
        print(f'Contagem de {a} até {b} de {c} em {c}')
        for c in range(a, b-1, -c):
            print(f'{c} ', end="")
            sleep(1)
        print()
    print('-='*16)
    
    
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem.')
while True:
    inic = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    contador(inic, fim, passo)
    break
