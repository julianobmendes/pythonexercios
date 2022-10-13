# pythonexercios
# Leia o peso de 5 pessoas e diga qual é o maior e o menor peso
maior = 0
menor = 0
for c in range (0, 5):
    peso = float(input('Digite um peso: '))
    if maior == 0 and menor == 0:
        maior = peso
        menor = peso
    elif peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso
print('A pessoa com o maior peso é de {:.2f}kg'.format(maior))
print('A pessoa com o menor peso é de {:.2f}kg'.format(menor))
