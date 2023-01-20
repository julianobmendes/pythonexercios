def leiaInt(msg):
    """
    obs. lê em str e transforma em int
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
