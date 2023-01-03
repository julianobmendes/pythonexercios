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
    :param num:
    :param sit:
    :return:
    """
    lista = {'total': len(num),'maior'max(num), 'menor': min(num), 'media': sum(num) / len(num)}
    print(lista)
    
    
notas(5, 6, 5.5, 4)
