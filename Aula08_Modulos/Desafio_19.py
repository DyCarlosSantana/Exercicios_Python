# Um professor quer sortear  um dos seus 4 alunos para pagar o quadro. Faça um programa que ajude ele, lendo o nome deles e sorteando um dos alunos.

import random

alunos = ('Bruna', 'Carlos', 'Beth', 'Edy')
escolhido = random.choice(alunos)
#Retorna um elemento aleatório da sequência não vazia (alunos). Se (alunos) estiver vazio, IndexError.
print('O escolhido foi: {}'.format(escolhido))
