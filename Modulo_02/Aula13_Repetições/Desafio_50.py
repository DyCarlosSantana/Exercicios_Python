#Desenvolva um programa que leia seis números inteiros e mostre apenas a soma daqueles que forem pares. se o valor for impar, desconsidere-o.
soma = 0
for c in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma = soma + n
print('A soma apenas dos números PARES, resulta em: {}'.format(soma))
print('Fim')