# pythonexercios
# Exercício 53 – Detector de Palíndromo
"""Crie um programa que leia uma frase qualquer e diga
se ela é um palíndromo, desconsiderando os espaços"""
pali = input('Digite um palavra: ').strip().upper()  # coloca afrse toda em letras maiusculas
frase_dividida = pali.split()  # usamos o .split para separar a frase em espaços
frase_junta = ''.join(frase_dividida)   # o join junta as palavras q o .split separou
frase_invertida = ''
for cont in range(len(frase_junta) - 1, -1, -1):
    frase_invertida += frase_junta[cont]
if frase_junta == frase_invertida:
    print('Temos um Palíndromo')
else:
    print('A frase dividida não é um Palíndromo')
