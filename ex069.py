# pythonexercios
# Exercício 69 – Análise de dados do grupo
"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""
idade = []
sexo = []
c = 0
men = 0
womam = 0
while True:
    i_sexo = str(input('Digite o sexo.\n[ M ] - masculino\n[ F ] - feminino\n')).upper()
    sexo.append(i_sexo)
    i_idade = int(input('Qual é a idade da pessoa: '))
    idade.append(i_idade)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você deseja continuar. S/N')).upper()
    if resp == 'N':
        break
for i in range(0, len(idade)):
    if idade[i] >= 18:
        c += 1
    if sexo[i] == 'M':
        men += 1
    if sexo[i] == 'F' and idade[i] <= 20:
        womam += 1
print('A {} pessoas maiores de 18 anos.'.format(c))
print('E foram cadastrados {} homens no processo.'.format(men))
print('E {} mulheres tem menos de 20 anos.'.format(womam))
