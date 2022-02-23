#   Faça um programa que tenha a função contador(), que receba três parâmetros: inicio, fim e passo e realize a contagem
#   a) de 0 a 10 pulando de 1 em 1
#   b) de 10 a 0 pulando de 2 em 2
#   c) contagem personalizada


def contagem(ini, fim, cont):
    if cont < 0:
        cont *= -1
    elif cont == 0:
        cont = 1
    if fim == ini:
        print('\033[1;31mInicio e Fim são iguais\033[m')
    elif fim < ini:
        while fim <= ini:
            print(ini)
            ini -= cont
    else:
        while fim > ini:
            print(ini + 1)
            ini += cont

contagem(0, 10, 1)
contagem(10, 0, 2)
print('Agora você decide')
contagem(int(input('Inicio: ')), int(input('Fim: ')), int(input('Contagem: ')))
