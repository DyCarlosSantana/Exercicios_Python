#Calcular o IMC de uma pessoa e exibir a faixa de valores...
idade = int(input('Insira sua Idade: '))
altura = float(input('Insira sua Altura: '))
peso = float(input('Insira seu peso: '))

imc = peso / (altura ** 2)
print('')
print('-=-'*15)
print('Sua idade: {}'.format(idade))
print('Seu Altura: {:.2f}m'.format(altura))
print('Seu Peso: {:.2f}Kg'.format(peso))
print('Seu IMC: {:.2f}'.format(imc))
print('')
if imc < 18.5:
    print('Classificação: Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Classificação: Peso normal')
elif 25 <= imc < 30:
    print('Classificação: Sobrepeso')
elif 30 <= imc < 35:
    print('Classificação: Obesidade Grau I')
elif 35 <= imc < 40:
    print('Classificação: Obesidade Grau II (severa)')
else:
    print('Classificação: Obesidade Grau III (mórbida)')
print('-=-' * 15)