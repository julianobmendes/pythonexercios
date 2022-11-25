# pythonexercios
# Exercício 92 – Cadastro de Trabalhador em Python
"""
Crie um programa que leia nome, ano de nascimento e carteira de
trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá
também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date
cad_trab = dict()
while True:
    cad_trab['nome'] = str(input('Nome: '))
    cad_trab['nasc'] = int(input('Ano de nascimento: '))
    cad_trab['idade'] = date.today().year - cad_trab["nasc"]
    cad_trab['ctps'] = int(input('Nº Carteira de Trabalho: (0 se não tem) '))
    if cad_trab["ctps"] == 0:
        break
    cad_trab['contratação'] = int(input('Ano de contratação: '))
    cad_trab['salário'] = float(input('Salário: '))
    cad_trab['aposento'] = (35 - (date.today().year - cad_trab["contratação"])) + cad_trab["idade"]
    #del cad_trab["nasc"]
    break
for k, v in cad_trab.items():
    print(f'{k} tem o valor {v}')
