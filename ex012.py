n1 = float(input('Qual o preco do produto? '))
n2 = float(input('Qual o valor de desconto? '))
n3 = (n1 * n2) / 100
print('O produto que custava R${:.2f} com o desconto de {:.0f}%'.format(n1, n2))
print('Foi para R${:.2f}, Voce teve R${:.2f} de desconto.'.format((n1 - n3), n3))
