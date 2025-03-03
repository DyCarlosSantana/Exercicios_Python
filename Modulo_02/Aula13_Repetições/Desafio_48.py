#Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500.
for c in range(1, 500):
    if c % 2 == 1:
        print(c)
print('Fim')