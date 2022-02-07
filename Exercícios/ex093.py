#   Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
#   quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final tudo isso será
#   quardado em um dicionário incluindo o total de gol marcados durante o campeonato
jogador = {}
auxPartidas = []
jogador['Nome'] = input('Digite o nome do jogador?: ')
jogador['qtdPartidas'] = int(input(f'Digite quantas partidas {jogador["Nome"]} jogou?: '))
if jogador['qtdPartidas'] != 0:
    for i in range(0, jogador['qtdPartidas']):
        auxPartidas.append(int(input(f'Quantos gols {jogador["Nome"]} marcou na {i + 1}ª partida?: ')))
    jogador['Partidas'] = auxPartidas[:]
    auxPartidas.clear()
jogador['TotalGols'] = sum(jogador['Partidas'])
for i, j in jogador.items():
    if i == 'Partidas':
        print('\033[1;31mGols por partida\033[m')
        for a, b in enumerate(jogador['Partidas']):
            print(f'{a + 1}ª Partida, {b} gols')
    else:
        print(f'{i}: {j}')
