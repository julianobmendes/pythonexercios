# pythonexercios
# Exercício 2 – Respondendo ao Usuário
"""
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
"""
nome = input('Qual é o seu nome? ')
print('Olá! Prazer em te conhecer, {}{}{}!'.format('\033[7;37;41m', nome, '\033[m'))
