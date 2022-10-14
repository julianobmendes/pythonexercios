# pythonexercios
# Exercício 48 – Soma ímpares múltiplos de três.
'''Faça um programa que calcule a soma entre todos os números que
são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = c + soma
        cont = cont + 1
print("Tem {} impares divisivel por 3 de 1 a 500 e o valor total e de {}".format(cont, soma))
