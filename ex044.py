produto = float(input('Qual o valor do produto: R$ '))
forma = int(input('''Escolha a forma de pagamento digitando o número correspondente:
[1] Dinheiro
[2] Cheque
[3] Cartão
Escolha de opção: '''))
lista = ['erro #404', 'ávista', '2x vezes', '3x vezes']
tipoforma = ['erro #404: opção inválida', produto - (produto * 5 / 100), produto, produto + (produto * 20 / 100)]
if forma == 3:
    print('Escolha em quantas vezes?')
    tipo = int(input('''
    [1] Ávista
    [2] 2x vezes
    [3] 3x ou mais
    Escolha de opção: '''))
    if tipo == 3:
        vezes = float(input('Em quantas vezes: '))
        print('O produto que custava R${:.2f} vai para R${:.2f}'.format(produto, tipoforma[tipo]))
        print('Você tera {:.0f} parcelas de R${:.2f}'.format(vezes, tipoforma[tipo] / vezes))
    elif tipo == 1 or tipo == 2:
        print('Com a forma de pagamento em cartão em {}'.format(lista[tipo]))
        print('O produto que custava R${:.2f} vai para R${:.2f}'.format(produto, tipoforma[tipo]))
elif forma == 1:
    print('''Para pagamentos em dinheiro o produto 
que custava R${:.2f} vai para R${:.2f}'''.format(produto, produto - (produto * 10 / 100)))
elif forma == 2:
    print('''Para pagamentos em cheque o produto 
que custava R${:.2f} vai para R${:.2f}'''.format(produto, produto - (produto * 10 / 100)))
else:
    print('Erro na forma de pagamento!')
