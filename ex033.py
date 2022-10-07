n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro: '))
n3 = int(input('Digite outro: '))
# verifica o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verifica o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor numero é {}{}{}'.format('\033[1;30m', menor, '\033[m'))
print('O maior numero é {}{}{}'.format('\033[1;30m', maior, '\033[m'))
