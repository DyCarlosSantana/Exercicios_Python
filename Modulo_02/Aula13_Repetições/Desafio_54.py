#Crie um programa que leia o ano de nascimento de 7 pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já sõa maiores.
import datetime
for c in range(0,1):
    ano = int(input('Ano de Nascimento: '))
    idade = datetime.date.today().year - ano
