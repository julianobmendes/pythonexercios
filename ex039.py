from datetime import date
nasc = int(input('Digite o seu ano de nascimento: '))
print('Qual o seu sexo masculino ou feminino?')
sexo = str(input('[M] para masculino \n[F] para feminino \nDigite opção: ')).strip().upper()
ano = date.today().year
idade = ano - nasc
if idade < 18 and sexo == 'M':
    falta = 18 - idade
    novoano = ano + falta
    print('Estamos em {} e você só pode se alistar em {}'.format(ano, novoano))
    print('Para você se alistar faltam {} anos'.format(falta))
elif idade == 18 and sexo == 'M':
    print('Você deve se alista ainda este ano, não se esqueça!')
elif idade > 18 and sexo == 'M':
    venc = idade - 18
    novoano = ano - venc
    print('Estamos em {} e você deveria ter se alistado em {}'.format(ano, novoano))
    print('Para se regularizar você deve pagar uma multa de R$ {:.2f}'.format(venc * 7))
else:
    print('Por ser do sexo feminino o alistamento não é obrigatório')
