casa = float(input('Qual é o valor do imóvel que você quer adquirir? R$ '))
salario = float(input('Qual é o valor da sua renda mensal? R$ '))
ano = int(input('Em quantos anos você quer pagar esté imóvel? '))
parcela = casa / (ano * 12)
renda30 = (salario * 30) / 100
renda25 = (salario * 25) / 100
renda20 = (salario * 20) / 100
print('Para pagar uma casa de R$ {:.2f} em {} parcelas'.format(casa, (ano * 12)))
print('o parcelamento ficara em R$ {:.2f} por mes'.format(parcela))
if parcela <= renda30 and parcela > renda25:
    print('Seu parcelamento vai consumir 30% do seu salario!')
    print('\033[7;30mCredito aprovado!\033[m')
elif parcela <= renda25 and parcela > renda20:
    print('Seu parcelamento vai consumir 25% do seu salario!')
    print('\033[7;30mCredito aprovado!\033[m')
elif parcela <= renda20:
    print('Seu parcelamento vai consumir 20% do seu salario!')
    print('\033[7;30mCredito aprovado!\033[m')
elif parcela > renda30:
    print('Valor acima de 30% de seu salario')
    print('\033[;33mCredito \033[1;31mNegado\033[m')
