from random import randint
from time import sleep

num01 = randint(0, 5)
#num01 = random.choice([0, 1, 2, 3, 4, 5])
num02 = int(input('Desculbra em qual numero\nestou pensando de 0 a 5\ne digite ai pra ver se acerta? '))
print('Procesando...')
sleep(2)
print('Prosesando.....')
sleep(2)
if num01 == num02:
    print('Parabens, voce é um telepata?')
else:
    print('Nao foi dessa vez amiguinho, era {}'.format(num01))
    print('Tentar de novo?')
