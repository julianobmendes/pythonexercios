from math import hypot
opos = float(input('Digite o cateto oposto: '))
adj = float(input('Digite o cateto adjacente: '))
'''hipo = (opos ** 2 + adj ** 2) ** (1/2)'''
hipo = hypot(opos, adj)
print('A soma do cateto oposto {} e o cateto adjacente {} de um triangulo retangulo'.format(opos, adj))
print('tem um comprimento de hipotenusa {:.2f}'.format(hipo))
