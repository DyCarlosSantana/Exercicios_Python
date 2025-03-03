#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo (divisiveis apenas por 1 ou por ele mesmo).

print('VERIFIQUE SE O NÚMERO É UM NÚMERO PRIMO')
print('')
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % 1 == 0:
        print('')


# Solicita um número inteiro do usuário
num = int(input("Digite um número inteiro: "))

# Inicializa uma variável para contar quantas vezes o número foi divisível
total_divisores = 0

# Verifica quantas vezes o número pode ser dividido sem resto
for i in range(1, num + 1):
    if num % i == 0:
        total_divisores += 1

# Se for divisível apenas por 1 e por ele mesmo, é primo
if total_divisores == 2:
    print(f"O número {num} é PRIMO!")
else:
    print(f"O número {num} NÃO é primo!")
