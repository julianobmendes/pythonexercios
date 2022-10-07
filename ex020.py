import random
a1 = input('Digite um nome: ')
a2 = input('Outro nome: ')
a3 = input('Outro nome: ')
a4 = input('Outro nome: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem para apresentacao do trabalho é:{}'.format(lista))
