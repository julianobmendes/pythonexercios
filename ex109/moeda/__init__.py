def aumentar(num=0, porc=0, show=False):
    """
    -> Função de soma porcentagem ao valor.
    :param num: valor a ser aumentado.
    :param porc: porcentagem a ser aumentada no valor.
    :param resp: recebe a soma entre 'num' e 'porc'
    :param show: define se o valor vai aparecer formatado em formato contábil
    :return: 'resp': resposta
    """
    resp = num + ((porc * num) / 100)
    return f'R$ {moeda(resp)}' if show else num + resp


def diminuir(num=0, porc=0, show=False):
    """
    -> Função de retirar porcentagem ao valor.
    :param num: valor a ser diminuído.
    :param porc: porcentagem a ser retirada no valor.
    :param resp: 'resp' = recebe 'num' menos 'porc'
    :param show: define se o valor vai aparecer formatado em formato contábil
    :return: 'resp': resposta
    """
    resp = num - ((porc * num) / 100)
    return f'R$ {moeda(resp)}' if show else num - resp


def dobro(num=0, show=False):
    """
    -> Função para dobra o valor.
    :param num: recebe o valor a ser somado.
    :param resp: 'num' multiplicada por ele mesmo.
    :param show: define se o valor vai aparecer formatado em formato contábil
    :return: 'resp': resposta
    """
    resp = num + num
    return f'R$ {moeda(resp)}' if show else resp


def metade(num=0, show=False):
    """
    -> Função para dividir um valor.
    :param num: recebe o valor a ser dividido.
    :param resp: 'num' dividido por dois
    :param show: define se o valor vai aparecer formatado em formato contábil
    :return: 'resp': resposta
    """
    resp = num / 2
    return f'R$ {moeda(resp)}' if show else resp


def moeda(num=0):
    """
    -> Função para formatar em valor monetário.
    :param num: recebe o número a ser formatado.
    :param resp: formata 'num' em monetário com duas casas decimais
    :return: 'resp': resposta
    """
    resp = f'R$ {num:.2f}'.replace('.', ',')
    return resp
