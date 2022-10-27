# pythonexercios
# Exercício 63 – Sequência de Fibonacci v1.0
"""
Escreva um programa que leia um número N inteiro qualquer e mostre na
tela os N primeiros elementos de uma Sequência de Fibonacci.
Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
"""
num = int(input('Digite um número inteiro para a Sequência Fibonacci: '))
cont = int(input('Digite quantos números da Sequência Fibonacci deseja ver: '))
var = 2
ant = 0
if num == 0:
    num = 1
    print('0 - 1', end="")
    while var != cont:
        var += 1
        ant = num + ant
        #print(ant)
        print(' - {}'.format(ant), end="")
        #ant = num
        num = ant + num
        #print(num)
elif num != 0:
    var = 1
    print(num, end="")
    while var != cont:
        var += 1
        ant = num
        num = num + ant
        print(' - {}'.format(num), end="")
        #prox = num
        #num = num + prox
