import math
ang = int(input('Digite o angulo: '))
seno = math.sin(math.radians(ang))
cosen = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('Baseado no angulo voce tem um seno de {:.2f} e um coseno de {:.2f} e uma tangente de angulo de {:.2f}'.format(seno, cosen, tang))
