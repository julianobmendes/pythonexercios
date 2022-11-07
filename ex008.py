# pythonexercios
# Exercício 8 – Conversor de Medidas
"""
Escreva um programa que leia um valor em metros e o exiba
convertido em centímetros e milímetros.
"""
me = float(input('Digite quantos metros? '))
cent = int(me * 100)
mili = int(me * 1000)
print('Para os {} metros que voce tem,\nvoce tambem tem {:.0f} centimetros e {:.0f} milimetros'.format(me, cent, mili))
