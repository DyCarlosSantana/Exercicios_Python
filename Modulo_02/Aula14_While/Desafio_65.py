#crie um programa que leia varios numeros inteiros pelo teclado, no final da execução mostre a média entre todos os valores e quais foram o maior e menor valores lidos. O programa deve perguntar aos usuario de quer ou não continuar a digitra valores.
cont = 0
total = 0
print('Para encerra o programa digite "000"')
while True:
    num = int(input('Digite um número: '))
    total += num
    cont += 1
    if num == 000:
        cont -= 1
        break
    print('-----'*5)
    
print(f'{cont}, {total}')
media = total / cont
print(f'A média de todos os valores inseridos é de: {media}')
print('Programa encerrado!')
