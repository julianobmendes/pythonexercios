from datetime import date
ano = int(input('\033[1;30mQual o ano voce quer verificar\033[m \nse voce quiser ferificar o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('O ano de {} é um ano bissexto'.format(ano))
else:
    print('O ano de {} \033[1;30mnao\033[m é um ano bissexto'.format(ano))
