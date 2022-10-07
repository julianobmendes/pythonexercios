alt = float(input('Qual é a altura: '))
larg = float(input('Qual é a largura: '))
m2 = alt * larg
tint = m2 / 2
print('Voce tem {:.2f}m² de parede e vai precizar de {:.2f} litros de tinta para pintar'.format(m2, tint))