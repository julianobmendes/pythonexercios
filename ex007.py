# pythonexercios
# Exercício 7 – Média Aritmética
"""
Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre a sua média.
"""
n1 = float(input('Vamos somar as notas\nDigite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Voce teve as notas {:.1f} e {:.1f}\ne sua media é final {:.1f}'.format(n1, n2, media))
