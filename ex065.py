# pythonexercios
# Exercício 65 – Maior e Menor valores
"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e
qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
cont = []
var = 0
resp02 = 0
while var != 999:
    resp = int(input('Digite um número: '))
    if resp != 999:
        cont.append(resp)
        while resp02 != 999:
            resp02 = str(input('Deseja continuar? S/N')).upper()
            if resp02 == 'S':
                resp02 = 999
                continue
            if resp02 == 'N':
                resp02 = 999
                var = 999
            if resp02 != 'S' and 'N':
                resp02 = 666
                
