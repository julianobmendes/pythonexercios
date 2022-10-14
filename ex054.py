# pythonexercios
# Exercício 54 – Grupo da Maioridade
from datetime import date
maior = []
menor = []
for c in range(0, 4):
    nasc = int(input('Digite o seu ano de nascimento: '))
    ano = date.today().year
    idade = ano - nasc
    if idade >= 21:
        maior.append(idade)
    else:
        menor.append(idade)
print('A {} pessoa com idade maior a 21 anos esta são {}'.format(len(maior), maior))
