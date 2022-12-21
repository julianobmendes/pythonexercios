# pythonexercios
# Exercício 64 – Tratando vários valores v1.0
"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
cont = []
var = resp02 = 0
while var != 999:
    resp = int(input('Digite um número: '))
    if resp != 999:
        cont.append(resp)
        resp02 = 0
    if resp == 999:
        break
print('')
print('Você digitou {} vezes até o resultado final.'.format(len(cont)))
print('E a soma de todos os valores é {}'.format(sum(cont)))
