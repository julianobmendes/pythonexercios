print('Vamos Medir seu IMC?')
print('_-'*10)
alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = (peso / (alt * alt))
if imc <= 18.5:
    print('Você está abaixo do peso, sua massa corporal é {:.2f}'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('Você está no peso normal, sua massa corporal é {:.2f}'.format(imc))
elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso, sua massa corporal é {:.2f}'.format(imc))
elif imc > 30 and imc <= 40:
    print('Você está com obesidade, sua massa corporal é {:.2f}'.format(imc))
else:
    print('Você está com obesidade mórbida, sua massa corporal é {:.2f}'.format(imc))
