# pythonexercios
# Exercício 77 – Contando vogais em Tupla
"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
tupla = ('beringela', 'dado', 'fogo', 'amor', 'vogal', 'computador', 'piramide')
vog = ['a','e','i','o','u']
cont = 0
while cont < (len(tupla)):
    soma = 0
    for c in range(0, 5):
        sub = tupla[cont].count(vog[c])
        soma += sub
    cont += 1
    print(f'O nome {tupla[cont-1]} tem {soma} vogais.')
