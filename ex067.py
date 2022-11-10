# pythonexercios
# Exercício 67 – Tabuada v3.0
"""
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""
print('Digete um número para saber a Tabuada.')
print('Quando quiser para digite um número negativo.\n')
while True:
    var = int(input('Digite um número:'))
    if var <= 0:
        break
    print('A Tabuada para o numero {} é:\n'.format(var))
    for c in range(1, 11):
        print('{} x {:2} = {:3}'.format(var, c, c*var))
print('fim do programa!!')
