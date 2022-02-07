'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado, no final mostre a
matriz com a formatação correta'''
matriz = []
aux = []
for linha in range(0, 3):
    for coluna in range(0, 3):
        aux.append(int(input(f'Digite o {coluna + 1}º valor da matriz: ')))
    matriz.append(aux[:])
    aux.clear()
print(matriz)
