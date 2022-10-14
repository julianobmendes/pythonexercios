# pythonexercios
# Exercício 52 – Números primos
num = int(input("Verificar numeros primos ate: "))
mult = 0
for count in range(2, num):
    if num % count == 0:
        mult += 1
if mult == 0:
    print("É primo")
else:
    print("Tem {} múltiplos acima de 2 o numero {} não é primo.".format(mult, num))
