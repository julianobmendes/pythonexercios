km = float(input('Quantos km de distancia tem a viagem? '))
if km <= 200:
    pas = km * 0.5
    print('Voce pagara por essa viagem R$ {:.2f}'.format(pas))
else:
    pas = km * 0.45
    print('Voce pagara por essa viagem R$ {:.2f}'.format(pas))
