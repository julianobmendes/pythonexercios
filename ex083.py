# pythonexercios
# Exercício 83 – Validando expressões matemáticas
"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os
parênteses abertos e fechados na ordem correta.
"""
ler = 0
ler = str(input('Digite uma expressão: '))
lista = list(ler)
if lista.count('(') == lista.count(')'):
    print('A expressão está correta, parabêns')
else:
    print('Você errou!!! A expressão está errada.')
