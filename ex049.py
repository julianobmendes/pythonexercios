# pythonexercios
# Exercício 49 – Tabuada v.2.0
'''Refaça o DESAFIO 9, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.'''
n1 = int(input('Digite um número: '))
print('A Tabuada para o numero {} é:'.format(n1))
print('='*13)
for c in range(1, 11):
    print('{} x {:2} = {:2}'.format(n1, c, n1 * c))
print('='*13)
