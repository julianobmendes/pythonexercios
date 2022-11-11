# pythonexercios
# Exercício 72 – Número por Extenso
"""
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.
"""
cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Desesseis', 'Desessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    print('Digite um número de 0 a 20:')
    num = int(input('Digite o número que você quer ver? '))
    if 0 <= num <= 20:
        break
    print('Tente novamente!\n')
print(f'O número {num} por extenço é {cont[num]}')
