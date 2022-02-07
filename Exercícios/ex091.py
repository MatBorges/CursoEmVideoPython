'''Crie um programa onde quatro jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado'''
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'JogadorUm':0, 'JogadorDois':0, 'JogadorTres':0, 'JogadorQuatro':0}
ranking = list()
for i in jogadores.keys():
    jogadores[i] = randint(1, 6)
    print(f'O {i} tirou {jogadores[i]}')
    sleep(0.3)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('=+' * 12)
#print(ranking)
for i, v in enumerate(ranking):
    print(f'O {v[0]} tirou {v[1]} e ficou em {i + 1}º')
