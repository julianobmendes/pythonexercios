# pythonexercios
# Exercício 74 – Maior e menor valores em Tupla
"""
Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor
e o maior valor que estão na tupla.
"""
from random import randint
num = (randint(1,1000), randint(1,1000), randint(1,1000), randint(1,1000), randint(1,1000))
c = 0
print(('Os números sorteados foram'), end="")
while c != len(num):
    print((f', {num[c]}'), end="")
    c += 1
print('.')
print(f'O maior número foi {max(num)}.')
print(f'O menor número foi {min(num)}.')
