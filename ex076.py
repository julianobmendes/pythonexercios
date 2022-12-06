# pythonexercios
# Exercício 76 – Lista de Preços com Tupla
"""
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular.
"""
lista = ('Samsung S10',1149.50,'Samsung S20 Ultra',3509,'Samsung S22 Ultra',7599,'iPhone 11',
2949.9,'iPhone 14 Pro Max',10499,'iPhone 13',4918.77,'Xiaomi 11T',3447.13,
'Xiaomi Note 11S',1477.02,'Motorola Edge 30',1979.10,'Motorola Edge 30 Pro',3149.1)
c = 0
print('='*34)
print('Produto               Preço')
print('='*34)
while c < (len(lista)):
    print(f'{lista[c]:22}R$ {lista[c+1]:8.2f}')
    c += 2
print('='*34)
