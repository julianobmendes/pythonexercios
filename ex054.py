# pythonexercios
# conferencia de maior idade.
from datetime import date
lista = []
for c in range(0, 7):
    nasc = int(input('Digite o seu ano de nascimento: '))
    ano = date.today().year
    idade = ano - nasc
    if idade >= 18:
        lista.append(idade)
print(lista)
