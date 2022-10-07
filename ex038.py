num01 = int(input('Digite o primeiro número: '))
num02 = int(input('Digite o segundo número: '))
if num01 < num02:
    print('O segundo valor {} é maior que o primeiro {}'.format(num02, num01))
elif num02 < num01:
    print('O primeiro valor {} é maior que o segundo {}'.format(num01, num02))
elif num01 == num02:
    print('Os números {} e {} sao iguais'.format(num01, num02))
