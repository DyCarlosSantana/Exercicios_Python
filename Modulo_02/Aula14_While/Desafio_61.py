#Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('='*20)
print('10 PRIMEIROS TERMOS')
print('='*20)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao #Formula para o Decimo termo de uma PA

for c in range(primeiro_termo, decimo + razao, razao):
    print('{}'.format(c),end=' -> ')
print('Acabou')