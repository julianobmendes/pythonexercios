# pythonexercios
# Exercício 104 – Validando entrada de dados em Python
"""
Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante
‘a função input() do Python, só que fazendo a
validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)
"""
def leiaInt(msg):
    """
    obs. le em str e transforma em int
    :param msg: número a ser verificado
    :return: valor númerico altera para int
    by Juliano Boaventura Mendes
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m ERRO!!! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')