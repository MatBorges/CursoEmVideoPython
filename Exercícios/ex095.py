#   Aprimore o exercicio 93, para que ele funcione com vários jogadores, incluindo um sistema de visualização de
#   detalhes do aproveitamento de cada jogador
time = list()
gols = list()
jogador = dict()
resp = ''
qtd_partidas = 0
while True:
    #   LEITURA DOS DADOS DE CADAS JOGADOR
    jogador['nome'] = input(f'Nome do {len(time) + 1}º jogador: ')
    qtd_partidas = int(input(f'Quantos jogos {jogador["nome"]} jogou?: '))
    for i in range(0, qtd_partidas):
        gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na {i + 1}ª partida?: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())
    print(f'\033[1;32m{jogador["nome"]} cadastrado com sucesso!!\033[m')
    #   CADASTRAR MAIS ALGUM JOGADOR?
    while True:
        resp = input('Deseja cadastar mais algum outro jogador (S/N)?: ').strip().upper()[0]
        if resp == 'N':
            break
        elif resp == 'S':
            gols.clear()
            jogador.clear()
            break
        else:
            print('\033[1;31mOPÇÃO INVÁLIDA!!!\033[m')
    if resp == 'N':
        break
#   MOSTRA TODOS OS JOGADORES CADASTRADOS
#   CABEÇALHO
print('COD ', end='')
for i in jogador.keys():
    print(f'{i.upper():<10} ', end='')
print()
print('=-' * 30)
#   VALORES
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for j in v.values():
        print(f'{str(j):<10} ', end='')
    print()
print('-=' * 10)
#   PESQUISA INDIVIDUAL DE JOGADOR
while True:
    resp = int(input('Mostrar os dados de qual jogador '
                     '\033[1;33m(digite o código do jogador ou qualquer numero negativo p/ sair)\033[m?: '))
    if resp >= len(time):
        print(f'\033[1;31mJOGADOR {resp} NÃO EXISTE\033[m')
    elif resp < 0:
        print('ATÉ LOGO!!!')
        break
    else:
        print(f'\033[1;36mjOGADOR {time[resp]["nome"]}\033[m')
        for k, v in enumerate(time[resp]['gols']):
            print(f'{v} gols no {k + 1}º jogo')
