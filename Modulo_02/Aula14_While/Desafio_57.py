#Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'. Caso esteja errado peça a digitação novamente até ter um valor correto.

while True:
    print('-----'*15)
    print('Opções: [M]-> Masculino, [F]-> Feminino.')
    sexo = str(input('Sexo: ')).strip().upper()
    if sexo in ['F', 'M']:
        if sexo == 'M':
            m = 'Masculino'
            print(f'O sexo escolido foi: {m}')
        else:
            f = 'Feminino'
            print(f'O sexo escolido foi: {f}')
        break #Interronpe o loop se a resposta for valida
    else:
        print('Escolha Invalida! Tente novamente.')
print('Fim')
