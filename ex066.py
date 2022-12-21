# pythonexercios
# Exercício 66 – Vários números com flag
"""
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada.
No final, mostre quantos números foram digitados e
qual foi a soma entre elas (desconsiderando o flag).
"""
cont = []
var = 0
print('Digite um valor inteiro para soma,\nQuando quiser para digite 999\n')
while True:
    resp = int(input('Digite um número: '))
    if resp == 999:
        break
    cont.append(resp)
if len(cont) == 0:
    print('')
    print('Não foi digitado nenhum valor!')
if len(cont) != 0:
    print('')
    print('Foram digitados {} vezes até o resultdo e a soma foi {}'.format(len(cont), sum(cont)))
