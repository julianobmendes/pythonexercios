# pythonexercios
# Exercício 62 – Super Progressão Aritmética v3.0
"""
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""
n = 10
while n != 0:
    print('Você deseja fazer uma Progressão Aritmética')
    n = str(input('[ S ] para SIM \n[ N ] para NÃO')).upper()
    if n == 'S':
        n = 10
    elif n == 'N':
        n = 0
    else:
        print('Você digitou um valor inválido!\n')
        continue
    if n != 0:
        primeiro = int(input("Primeiro elemento: "))
        razao = int(input("Razao: "))
        ultimo = (primeiro + (n-1)*razao) + 1
        for var in range(primeiro, ultimo, razao):
            print('{}, '.format(var), end="")
        print('\n')
print('Fim do programa')
