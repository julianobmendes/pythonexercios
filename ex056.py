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
for c in range (0, 4):
    nom = str(input('Digite o nome da {}º pessoa: '.format(c+1))).strip()
    nome.append(nom)
    idad = str(input('Digite a idade da {}º pessoa: '.format(c+1))).strip()
    idade.append(idad)
    print('Digite o sexo da {}º pessoa: '.format(c+1))
    print('[M] para Masculino e [F] para Feminino')
    sex = str(input('Digite o sexo da {}º pessoa: '.format(c+1))).strip()
    sexo.append(sex)
print(nome[0])   
