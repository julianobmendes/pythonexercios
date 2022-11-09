# pythonexercios
# Exercício 57 – Validação de Dados
"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
sexo = 1
print('---=== Menu ===---')
print('Para sexo masculino digite [M]')
print('Para sexo feminino digite [F]')
print('Para sair digite [0] zero')
print('----------------------------------')
while sexo != '0':
    sexo = input('Digite o sexo da pessoa: ').strip().upper()
    if sexo == 'M':
        print(sexo)
        print('A pessoa é do sexo Masculino')
        print('----------------------------')
    elif sexo == 'F':
        print('A pesoa é do sexo Feminino')
        print('----------------------------')
    elif sexo != '0':
        print('Você digitou um valor errado, favor repitir')
        print('-------------------------------------------')
print('Fim do programa')
"""
sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F]')).strip().upper()[0]
print('Sexo registrado com sucesso'.format(sexo))
"""
