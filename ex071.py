# pythonexercios
# Exercício 71 – Simulador de Caixa Eletrônico
"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
c = 0 #R$50
v = 0 #R$20
d = 0 #R$10
u = 0 #R$1
total = 0
while 1 != 2:
    print('---=== Bem vindo ao caixa eletrônico! ===---')
    saque = int(input('Quanto será o valor a ser sacado? '))
    total = saque
    while saque >= 50:
        saque = saque - 50
        c += 1
    while saque >= 20:
        saque = saque - 20
        v += 1
    while saque >= 10:
        saque = saque - 10
        d += 1
    while saque >= 1:
        saque = saque - 1
        u += 1
    if saque == 0:
        break
print('Você está sacando {:.2f} reais, sendo'.format(total), end="")
if c != 0:
    print(' {} notas de R$ 50.00'.format(c), end="")
    if v != 0 or d != 0 or u != 0:
        print(',', end="")
if v != 0:
    print(' {} notas de R$ 20.00'.format(v), end="")
    if d != 0 or u != 0:
        print(',', end="")
if d != 0:
    print(' {} notas de R$ 10.00'.format(d), end="")
    if u != 0:
        print(',', end="")
if u != 0:
    print(' {} notas de R$ 1.00'.format(u), end="")
print('.')
