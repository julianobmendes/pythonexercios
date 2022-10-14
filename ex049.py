# pythonexercios
# Exercício 49 – Tabuada v.2.0
'''Refaça o DESAFIO 9, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.'''
n1 = int(input('Digite um número: '))
n2 = 1
print('A Tabuada para o numero {} é:'.format(n1))
print('='*13)
for c in range(0, 10):
    print('{} x {:2} = {:2}'.format(n1, n2, n1 * n2))
    n2 = n2 + 1
print('='*13)
