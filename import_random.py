import random
n = random.randint(0,5)
nchute = int(input('Tente adivinhar um número inteiro entre 0 e 5 que será sorteado aleatóriamente: '))
print('Parabéns cachoeira! Tu conseguiu acertar um valor aleatório dog, brabo!' if nchute == n else 'É dog, não é fácil acertar um chute aleatório.. O número escolhido pelo gerador aleatório foi {}.'.format(n))

'''from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer! ')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))'''