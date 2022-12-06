# pythonexercios
# Exercício 97 – Um print especial
"""
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e
mostre uma mensagem com tamanho adaptável.
Ex: 
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~
"""
def escreva(txt):
    print(f'≈'*(len(txt)+8))
    print(f'    {txt}')
    print(f'≈'*(len(txt)+8))


escreva('Gustavo Guanabara')
escreva('Curso em Vídeo no Youtube')
escreva('CeV')
