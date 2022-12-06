# pythonexercios
# Exercício 94 – Unindo dicionários e listas
"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista.
No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
lista = list()
total_idade = list()
while True:
    nome = str(input('Nome: '))
    test = 0
    while test != 999:
        sexo = str(input('Sexo? [ M/F]' )).upper()
        if sexo == 'M':
            sexo = 'Masculino'
            test = 999
        elif sexo == 'F':
            sexo = 'Feminino'
            test = 999
        else:
            print('Você selecionou um sexo errado!!!')
    idade = int(input('Idade: '))
    total_idade.append(idade)
    lista.append({'nome': nome, 'sexo': sexo, 'idade': idade})
    while True:
        resp = str(input('--== Continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!!!    Resposta: S ou N')
    if resp == 'N':
        break
print(f'O grupo de pesquisa tem {len(lista)} pessoas.')
print(f'A média de idade do grupo é {sum(total_idade) / len(lista):.2f} anos')
print('As mulheres que foram cadastradas são:')
for c in lista:
    if c['sexo'] == 'Feminino':
        print(f'- {c["nome"]}')
print('As pessoas mais velhas cadastradas são:')
for c in lista:
    if c['idade'] >= (sum(total_idade) / len(lista)):
        for k, v in c.items():
            print(f'{k} = {v}   ', end="")
        print('')
