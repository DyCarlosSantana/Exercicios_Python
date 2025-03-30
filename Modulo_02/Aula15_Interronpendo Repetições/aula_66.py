# Desafio 66: Vários Números com Flag
# Objetivo:
# Ler vários números inteiros pelo teclado.
# O programa só deve parar quando o usuário digitar 999.
# No final, mostrar:
# Quantos números foram digitados.
# A soma entre eles (desconsiderando o 999).
cont = 0
soma = 0
print('Condição de parada [999]')
while True:
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if num == 999:
        cont -=1
        soma -= 999
        break
print(f'Forma digitados {cont} números.\n A soma deles é: {soma}')
