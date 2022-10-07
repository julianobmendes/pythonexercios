n1 = int(input('Digite um numero! '))
n2 = int(input('Digite outro numero! '))
s = n1 + n2
print('O valor de {}{} e {} {}somados é {}{}{}'.format('\033[1;30m', n1, n2, '\033[m', '\033[7;30m', s, '\033[m'))
