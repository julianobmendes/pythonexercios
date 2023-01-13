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
    print(f'A Tabuada para o número {var} é:\n')
    for c in range(1, 11):
        print(f'{var} x {c:2} = {c*var:3}')
print('fim do programa!!')
