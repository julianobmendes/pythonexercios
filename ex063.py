# pythonexercios
# Exercício 63 – Sequência de Fibonacci v1.0
"""
Escreva um programa que leia um número N inteiro qualquer e mostre na
tela os N primeiros elementos de uma Sequência de Fibonacci.
Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
"""
n = int(input('Quantos termos você quer mostar? '))
t1 = 0
t2 = 1
print('{} ➜ {}'.format(t1, t2), end="")
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' ➜ {}'.format(t3), end="")
    t1 = t2
    t2 = t3
    cont += 1
print(' ➜ Fim!')
"""
num = int(input('Digite um número inteiro para a Sequência Fibonacci: '))
cont = int(input('Digite quantos números da Sequência Fibonacci deseja ver: '))
var = 1
ant = 0
print('')
if num == 0:
    num = 1
    while var != cont:
        res = var % 2
        if var == 1:
            print(' {}'.format(ant), end="")
            num += ant
        if res == 0:
            print(' - {}'.format(ant), end="")
            num += ant
        if res == 1:
            print(' - {}'.format(num), end="")
            ant += num
        var += 1
elif num != 0:
    while var != cont:
        res = var % 2
        if var == 1:
            print(' {}'.format(num), end="")
            ant += num
        if res == 0:
            print(' - {}'.format(num), end="")
            ant += num
        if res == 1:
            print(' - {}'.format(ant), end="")
            num += ant
        var += 1
"""
