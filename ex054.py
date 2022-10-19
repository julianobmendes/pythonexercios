# pythonexercios
# Exercício 54 – Grupo da Maioridade
'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.'''
from datetime import date
maior = []
menor = []
for c in range(0, 7):
    nasc = int(input('Digite o seu ano de nascimento: '))
    ano = date.today().year
    idade = ano - nasc
    if idade >= 21:
        maior.append(idade)
    else:
        menor.append(idade)
print('A {} pessoa com idade maior a 21 anos esta são {}'.format(len(maior), maior[0:len(maior)]))
print('A {} pessoa com idade menor a 21 anos esta são {}'.format(len(menor), menor))
