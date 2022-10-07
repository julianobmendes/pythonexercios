n1 = int(input('Digete um numero inteiro: '))
n2 = 0
count = 0
print('A Tabuada para o numero {} é:'.format(n1))
print('='*13)
while count <= 10:
    print('{} x {:2d} = {:3d}'.format(n1, n2+1, (n2+1)*n1))
    n2 = n2 +1
    count += 1
    if count > 9: break
print('='*13)
