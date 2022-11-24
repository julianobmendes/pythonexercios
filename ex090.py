# pythonexercios
# Exercício 90 – Dicionário em Python
"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.
"""
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Qual a média de {dados["nome"]}:'))
if dados["média"] >= 7:
    dados['situação'] = 'Aprovado'
else:
    dados['situação'] = 'Reprovado'
for k, v in dados.items():
    print(f'O {k} é {v}' if k == "nome" else f'A {k} é {v}')
