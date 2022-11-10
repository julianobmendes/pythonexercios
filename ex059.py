# pythonexercios
# Exercício 59 – Criando um Menu de Opções
"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
num01 = num02 = result = control = 0
num01 = int(input('Digite o 1º número: '))
num02 = int(input('Digite o 2º número: '))
while control != 'sair':
    #num01 = int(input('Digite o 1º número: '))
    #num02 = int(input('Digite o 2º número: '))
    print('---=== Menu ===---')
    print('[ 1 ] - Somar')
    print('[ 2 ] - Multiplicar')
    print('[ 3 ] - Maior')
    print('[ 4 ] - Redigitar novos números')
    print('[ 5 ] - Sair')
    control = int(input(''))
    if (control!=1) and (control!=2) and (control!=3) and (control!=4) and (control!=5) :
        print('Você digitou uma opção inválida!!!\n')
    if control == 1:
        result = num01 + num02
        print('A soma de {} + {} é {}.\n'.format(num01, num02, result))
    if control == 2:
        result = num01 * num02
        print('A multiplicação de {} x {} é de {}.\n'.format(num01, num02, result))
    if control == 3:
        if num01 > num02:
            print('O valor {} é maior que {}.\n'.format(num01, num02))
        if num02 > num01:
            print('O valor {} é maior que {}.\n'.format(num02, num01))
    if control == 4:
        num01 = int(input('Digite o 1º número: '))
        num02 = int(input('Digite o 2º número: '))
        print('\n')
    if control == 5:
        control = 'sair'
print('Fim do Programa!')
