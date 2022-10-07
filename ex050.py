n2 = int(0)
for c in range(0, 6):
    n1 = int(input('Digite um número: '))
    if n1 % 2 == 0:
        n2 = n1 + n2
print('Os números pares somados é {}'.format(n2))
