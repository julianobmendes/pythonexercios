# pythonexercios
# Exercício 41 – Classificando Atletas
"""
A Confederação Nacional de Natação precisa de um
programa que leia o ano de nascimento de um atleta e
mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER
"""
from datetime import date
ano = int(input('Qual o ano de seu nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print(idade)
    print('Mirim')
elif idade <= 14:
    print(idade)
    print('Infantil')
elif idade <= 19:
    print(idade)
    print('Junior')
elif idade == 20:
    print('Senior')
else:
    print('Master')
