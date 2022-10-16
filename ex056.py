# pythonexercios
# Exercício 56 – Analisador completo
'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
nome = []
idade = []
sexo = []
i_homem = 0
n_homem = 0
cont = 0
for c in range(0, 4):
    i_nome = str(input('Digite o nome da {}º pessoa: '.format(c+1))).strip()
    nome.append(i_nome)
    i_idade = int(input('Digite a idade da {}º pessoa: '.format(c+1)))
    idade.append(i_idade)
    print('Digite o sexo da {}º pessoa: '.format(c+1))
    print('[M] para Masculino e [F] para Feminino')
    i_sexo = str(input()).upper()
    sexo.append(i_sexo)
m_idade = (sum(idade) / 4)
for i in range(0, 4):
    if sexo[i] == 'M' and idade[i] > i_homem:
        i_homem = idade[i]
        n_homem = nome[i]
for m in range(0, 4):
    if sexo[m] == 'F' and idade[m] < 21:
        cont = cont + 1
print('O grupo é composto por {} homens e {} mulheres.'.format(sexo.count('M'), sexo.count('F')))
print('A média de idade do grupo é de {:.0f} anos.'.format(m_idade))
print('O nome do homem mais velho é {} e ele tem {} anos.'.format(n_homem, i_homem))
print('A {} mulhere(s) com 20 anos ou menos.'.format(cont))
