n1 = int(input('Digite um número: '))
n2 = 1
print('A Tabuada para o numero {} é:'.format(n1))
print('='*13)
for c in range(0, 10):
    print('{} x {:2} = {:2}'.format(n1, n2, n1 * n2))
    n2 = n2 + 1
print('='*13)
