#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador, e em quantos anos ele vai pagar.
#Calcular o valor da prestação mensal, sabendo que ele não pode exceder 30% do salario ou então o emprestimo será negado
import time
#Coleta dos dados:
nome = str(input('Digite seu nome: '))
renda_mensal = float(input('Informe sua renda mensal: '))
valor_imovel = float(input('Informe o valor do imovel: '))
tempo_pagamento = int(input('Em quantos anos pretende pagar o emprestimo?: '))
print('PROCESSANDO...')
time.sleep(2)

#Calculo
qt_meses = tempo_pagamento * 12
prestacao = valor_imovel / qt_meses
limite = renda_mensal * 30 /100

#Verificação
if prestacao > limite:
    print('Emprestimo NEGADO!')
else:
    print('{}, seu emprestimo foi APROVADO!'.format(nome))
    print('O valor da prestação mensal será de R${:.2f}'.format(prestacao))