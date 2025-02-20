import random
n = random.randint(0, 5)
print('Tente adivinhar o numero entre 0 e 5')
chute = int(input('Faça seu chute: '))
if chute == n:
    print('Vocé acertou!')
else:
    print('Errou!')
