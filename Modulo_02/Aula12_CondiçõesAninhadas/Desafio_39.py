#Faça um programa que leia a idade de um jovem e informe, de acordo com sua idade: Se ele ainda vai se alistar ao serviço militar; Se é a hora de se alistar, ou se ja passou do tempo do alistameto.
#Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo.
idade = int(input('Informe sua idade: '))
alistamento = 18
if idade < alistamento:
    print('Você ainda irá realizar seu alistamento militar')
    print('Ainda falta {} anos.'.format(alistamento - idade))
elif idade == alistamento:
    print('Você ja completou {} anos.'.format(idade))
    print('Esta na hora de realizar seu alistamento militar')
elif idade > alistamento:
    print('Já passou da hora de realizar seu alistamento militar')
    print('Já passou {} anos, do periodo de alistamento.'.format(idade - alistamento))