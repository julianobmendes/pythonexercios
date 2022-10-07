num = int(input('Digite um número inteiro: '))
print('Escolha por forma de número a opção desejada de conversão')
print('[1] - Binário')
print('[2] - Octal')
print('[3] - Hexadecimal')
base = int(input('Escolha: '))
if base == 1:
    resp = bin(num)[2:]
    print('O valor convertido de {} para binário é {}'.format(num, resp))
elif base == 2:
    resp = oct(num)[2:]
    print('O valor convertido de {} para Octal é {}'.format(num, resp))
elif base == 3:
    resp = hex(num)[2:]
    print('O valor convertido de {} para hexadecimal é {}'.format(num, resp))
elif base != (1, 2, 3):
    print('Valor digitado incorreto')
