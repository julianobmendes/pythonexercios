def aumentar(num, porc):
    """
    -> Função de soma porcentagem ao valor.
    :param num: valor a ser aumentado.
    :param porc: porcentagem a ser aumentada no valor.
    :param resp: recebe a soma entre 'num' e 'porc'
    :return: 'resp': resposta
    """
    resp = (porc * num) / 100
    return num + resp


def diminuir(num, porc):
    """
    -> Função de retirar porcentagem ao valor.
    :param num: valor a ser diminuído.
    :param porc: porcentagem a ser retirada no valor.
    :param resp: 'resp' = recebe 'num' menos 'porc'
    :return: 'resp': resposta
    """
    resp = (porc * num) / 100
    return num - resp


def dobro(num):
    """
    -> Função para dobra o valor.
    :param num: recebe o valor a ser somado.
    :param resp: 'num' multiplicada por ele mesmo.
    :return: 'resp': resposta
    """
    resp = num + num
    return resp


def metade(num):
    """
    -> Função para dividir um valor.
    :param num: recebe o valor a ser dividido.
    :param resp: 'num' dividido por dois
    :return: 'resp': resposta
    """
    resp = num / 2
    return resp


def moeda(num):
    """
    -> Função para formatar em valor monetário.
    :param num: recebe o número a ser formatado.
    :param resp: formata 'num' em monetário com duas casas decimais
    :return: 'resp': resposta
    """
    resp = f'R$ {num:.2f}'
    return resp
