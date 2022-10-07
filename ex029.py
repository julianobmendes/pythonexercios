km = int(input('A quantos km/h voce esta? '))
multa = (km - 80) * 7
if km <= 80:
    print('Fique tranquilo, voce está dentro do limite de velocidade')
else:
    print('Voce excedeu o limite de velocidade e recebera uma multa de R$ {:.2f}'.format(multa))
