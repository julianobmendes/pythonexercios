# pythonexercios
# Exercício 89 – Boletim com listas compostas
"""
Crie um programa que leia nome e duas notas de vários alunos e
guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente.
"""
lista = list()
while True:
    nome = str(input('Nome do aluno: '))
    nota_01 = float(input('1º nota: '))
    nota_02 = float(input('2º nota: '))
    lista.append([nome, nota_01, nota_02])
    resp = str(input('--== Continuar [ S/N ]? ==--')).upper()
    if resp == 'N':
        break
print('-='*15)
print('No.  Nome            Média')
print('-'*27)
for c in range(0, len(lista)):
    print(f'{c+1}    {lista[c][0]:15} {(lista[c][1]+lista[c][2])/2}')
print('-'*27)
while True:
    resp = int(input('Qual aluno você deseja ver as notas?\n(para interroper digite 999'))
    if resp > len(lista) and resp != '999':
        print('-'*35)
        print('aluno inexistente!!!')
        print('-'*35)
    if resp == '999':
        break
    if resp <= len(lista):
        resp -= 1
        print('-'*35)
        print(f'Notas de {lista[resp][0]} são: {lista[resp][1]} e {lista[resp][2]}')
        print('-'*35)
