print('Vamos analizar suas notas!!!')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Sua média de {:.1f} foi abaixo de 5.0'.format(media))
    print('\033[1;30;41m__--* REPROVADO *--__\033[m')
elif 5 <= media < 7:
    print('Você não atingiu nota necessaria, sua média foi {:.1f}'.format(media))
    print('\033[1;33;46m__--** RECUPERAÇÃO **--__\033[m')
else:
    print('Sua média foi de {:.1f}, parabéns!!!'.format(media))
    print('\033[1;33m__--** APROVADO **--__\033[m')
