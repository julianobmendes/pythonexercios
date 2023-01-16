def aumentar(num, porc):
    """
    -> Função de soma porcentagem ao valor.
    :param num: valor a ser aumentado.
    :param porc: porcentagem a ser aumentada no valor.
    :return: 'resp' = recebe a soma entre 'num' e 'porc'
    """
    resp = (porc * num) / 100
    return num + resp


def diminuir(num, porc):
    """
    -> Função de retirar porcentagem ao valor.
    :param num: valor a ser diminuido.
    :param porc: porcentagem a ser retirada no valor.
    :return: 'resp' = recebe 'num' menos 'porc'
    """
    resp = (porc * num) / 100
    return num - resp


def dobro(num):
    """
    -> Função para dobra o valor.
    :param num: recebe o valor a ser somado.
    :return: 'num' multiplicada por ele mesmo.
    """
    resp = num + num
    return resp


def metade(num):
    """
    -> Função para dividir um valor.
    :param num: recebe o valor a ser dividido.
    :return: 'num' dividido por dois
    """
    resp = num / 2
    return resp
