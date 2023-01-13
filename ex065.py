# pythonexercios
# Exercício 65 – Maior e Menor valores
"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e
qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
cont = []
var = resp02 = 0
while var != 999:
    resp = int(input('Digite um número: '))
    if resp != 999:
        cont.append(resp)
        resp02 = 0
        while resp02 != 999:
            resp02 = str(input('--== Deseja continuar? S/N ==--\n')).upper().strip()
            if resp02 == 'S':
                resp02 = 999
                continue
            if resp02 == 'N':
                resp02 = 999
                var = 999
                continue
            if resp02 != ('S') and resp02 != ('N'):
                resp02 = 666
                print('Você digitou um valor errado!')
print('')
print('Você digitou {} vezes até o resultado final.'.format(len(cont)))
print('O valor mínimo foi  de {}.'.format(min(cont)))
print('O valor maxímo foi de {}.'.format(max(cont)))
print('E a soma de todos os valores é {}'.format(sum(cont)))
