satual = float(input('Imforme seu salario atual: '))
if satual > 1250:
    snovo = ((satual * 10 / 100) + satual)
else:
    snovo = ((satual * 15 / 100) + satual)
print('Seu salario é de R$ {:.2f} e agora passa a ser R$ {:.2f}'.format(satual, snovo))
print('-=-' * 20)