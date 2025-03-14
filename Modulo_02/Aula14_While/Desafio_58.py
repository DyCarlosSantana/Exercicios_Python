#Melhore o jogo do desafio 29 onde o computador vai "Pensar" em um núemro de 0 a 10. Só que agora o jogador vai tentra adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer.
import random
import time
n = random.randint(0, 11)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*20)
palpites = 0
while True:
    jogador = int(input('Faça seu chute: '))
    print('PROCESSANDO...')
    time.sleep(1)
    palpites += 1
    if jogador == n:
        print('-'*25)
        print('Pensei no número {}'.format(n))
        if palpites == 1:
            print(f'Você acertou na {palpites}° tentativa')
        else:
            print(f'Você precisou de {palpites} tentativas')

        break #interronpe o loop caso o valor seja valido
    else:
        print('Errou! Mas você pode tente novamente')