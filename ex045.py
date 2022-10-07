from random import randint
num01 = randint(0, 2)
lista = ['papel', 'pedra', 'tesoura']
esco = int(input('''Escolha entre papel, pedra ou tesoura:
[1] papel
[2] pedra
[3] tesoura
faça sua escolha: '''))
num02 = esco - 1

if num01 == 0:
    print('{} X {}: Empate'.format(lista[num01], lista[num02]))

elif num01 == 1:
    print('{} X {}: Você venceu!!!'.format(lista[num01], lista[num02]))
elif num02 == 2:
    print('{} X {}: Você perdeu!!!'.format(lista[num02], lista[num01]))
