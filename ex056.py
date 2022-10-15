# pythonexercios
# Exercício 56 – Analisador completo
"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
nome = []
idade = []
sexo = []
for c in range(0, 2):
    i_nome = str(input('Digite o nome da {}º pessoa: '.format(c+1))).strip()
    nome.append(i_nome)
    i_idade = int(input('Digite a idade da {}º pessoa: '.format(c+1)))
    idade.append(i_idade)
    print('Digite o sexo da {}º pessoa: '.format(c+1))
    print('[M] para Masculino e [F] para Feminino')
    i_sexo = str(input()).upper()
    sexo.append(i_sexo)
m_idade = (sum(idade) / 4)
print(nome)
print(idade)
print('{:.0f}'.format(m_idade))
print('{}'.format(sexo.count('M')))
