# pythonexercios
# Exercício 70 – Estatísticas em produtos
"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""
prod = []
preco = []
p_maior = 0
p_menor = [0, 0]
while 1 != 2:
    i_prod = str(input('Qual o nome do produto: '))
    prod.append(i_prod)
    i_preco = float(input('Qual é o valor da mercadoria: '))
    preco.append(i_preco)
    if i_preco >= 1000:
        p_maior += 1
    if i_preco <= p_menor[1] or p_menor[1] == 0:
        del p_menor[0]
        p_menor.insert(0, i_prod)
        del p_menor[1]
        p_menor.insert(1, i_preco)
    print('')
    c = str(input('Deseja continuar? S/N')).upper()
    if c == 'N':
        break
print('Você teve um tota de gasto de R$ {:.2f}'.format(sum(preco)))
print('Dos produtos {} custaram mais de R$ 1000,00'.format(p_maior))
print('E o produto mais barato foi {}, que custou R$ {:.2f}'.format(p_menor[0], p_menor[1]))
print('fim programa!')
