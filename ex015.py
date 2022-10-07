d = int(input('Quantos dias o carro ficou no aluguel? '))
km = float(input('Quantos km o carro percorreu? '))
c = (d * 60) + (km * 0.15)
print('Total a pagar é de R${:.2f}'.format(c))
