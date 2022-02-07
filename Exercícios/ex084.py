'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
dados = []
pessoas = []
pesado = leve = 0
pesados = []
leves = []
while True:
    dados.append(input('Digite o nome da pessoa: '))
    dados.append(float(input(f'Digite o peso de {dados[0]}: ')))
    if len(pessoas) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        elif dados[1] < leve:
            leve = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    if input('Quer cadastrar mais alguma pessoa?(s/n): ')[0] in 'Nn':
        break
for i in pessoas:
    if i[1] == pesado:
        pesados.append(i[:])
    elif i[1] == leve:
        leves.append(i[:])
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'As pessoas mais pesadas são: {pesados}')
print(f'E as pessoas mais leves são: {leves}')
