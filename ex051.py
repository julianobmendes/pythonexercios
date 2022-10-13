# pythonexercios
# Exercício 51 – Progressão Aritmética
primeiro = int(input("Primeiro elemento: "))
razao = int(input("Razao: "))
n = 10
ultimo = primeiro + (n-1)*razao
ultimo = ultimo + 1
for var in range(primeiro, ultimo, razao):
    print(var)
