# pythonexercios
# Exercício 42 – Analisando Triângulos v2.0
"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes
"""
print('_-_'*14)
print('Vamos analizar a formacao de um triangulo.')
print('_-_'*14)
a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))
#tambem pode ser (a < B + c)
if ((b - c) < a < b + c) and ((a - c) < b < a + c) and ((a - b) < c < a + b):
    print('Com a formacao de {}, {} e {} voce tem um triangulo'.format(a, b, c))
    if a == b == c:
        print('Forma um triangulo equilátero')
    elif a != b != c != a:
        print('Forma um triangulo escaleno')
    else:
        print('Forma um triangulo esósceles')
else:
    print('Com as linhas {}, {} e {} nao formam um triangulo'.format(a, b, c))
