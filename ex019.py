import random
a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome do proximo aluno: ')
a3 = input('Digite o nome do proximo aluno: ')
a4 = input('Digite o nome do proximo aluno: ')
lista = [a1, a2, a3, a4]
print('O aluno que vai apagar  o quadro é {}'.format(random.choice(lista)))
