#Crie um programa que leia duas notas de aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.
#Média abaixo de 5.0 - Reprovado
#Média entre 5.0 e 6.9 - Recuperação
#Média 7.0 ou superior - Aprovado
n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Média do Aluno: {}'.format(media))
    print('REPROVADO')
elif media == 5.0 or media <= 6.9:
    print('Média do Aluno: {}'.format(media))
    print('RECUPERAÇÂO')
elif media == 7.0:
    print('Média do Aluno: {}'.format(media))
    print('APROVADO')

