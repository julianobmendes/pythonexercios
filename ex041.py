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