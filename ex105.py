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
def notas(**num, sit=False):
    """

    :param num:
    :param sit:
    :return:
    """
    print(f'A maior nota foi: {max(num)}')
    print(f'A menor nota foi: {min(num)}')
    print(f'A média da turma: {sum(num) / len(num)}')
    print(f'Situação: {}')