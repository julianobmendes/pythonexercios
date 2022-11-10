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
        resp02 = 0
    if resp == 999:
        break
print('')
print('Você digitou {} vezes até o resultado final.'.format(len(cont)))
print('O valor mínimo foi  de {}.'.format(min(cont)))
print('O valor maxímo foi de {}.'.format(max(cont)))
print('E a soma de todos os valores é {}'.format(sum(cont)))
