# pythonexercios
# Exercício 105 – Analisando e gerando Dicionários
"""
Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um
dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para
consulta pelo desenvolvedor.
"""


def notas(* num, sit=False):
    """
    -> Função para analizar a situação da turma.
    :param num: recebe varias notas da turma.
    :param sit: Valor opcional que mostra como está a situação da turma.
    :return: Um dicionário com uma analize da turma.
    """
    lista = dict()
    lista['total'] = len(num)
    lista['maior'] = max(num)
    lista['menor'] = min(num)
    lista['média'] = sum(num) / len(num)
    if sit:
        if lista['média'] >= 7:
            lista['situação'] = 'BOA'
        elif lista['média'] >= 5:
            lista['situação'] = 'RAZOÁVEL'
        else:
            lista['situação'] = 'RUIM'
    return lista
    
    
# Programa Principal
resp = notas(7, 6, 5.5, 1, sit=True)
print(resp)
help(notas)
