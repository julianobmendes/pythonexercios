# pythonexercios
# Exercício 75 – Análise de dados em uma Tupla
"""
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
num = (int(input('Digite um número: ',)),
    int(input('Digite outro número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite o último número:')))
print(f'O valor 9 aparece {num.count(9)} vezes.')
if 3 in num:
    print(f'O número três aparece pela primeira vez na posição: {num.index(3)+1}')
else:
    print('Não teve número três!')
print(f'Os valores pares que aparecem são: ', end="")
for c in num:
    if c % 2 == 0:
        print(c, end="")
