# pythonexercios
# Exercício 40 – Aquele clássico da Média
"""
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida: 
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO
"""
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
