frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na pocisao {}'.format(frase.find('A')+1))
print('A ultima pocisao da letra a foi {}'.format(frase.rfind('A')+1))
