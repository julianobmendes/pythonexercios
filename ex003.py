# pythonexercios
# Exercício 3 – Somando dois números
"""
Crie um programa que leia dois números e mostre a soma entre eles.
"""
n1 = int(input('Digite um número! '))
n2 = int(input('Digite outro número! '))
soma = n1 + n2
print('O valor de {}{} e {} {}somados é {}{}{}'.format('\033[1;30m', n1, n2, '\033[m', '\033[7;30m', soma, '\033[m'))
