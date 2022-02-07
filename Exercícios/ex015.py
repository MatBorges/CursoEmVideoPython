'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''
percorrido = float(input('Digite a quantidade percorrida em Km: '))
dias = int(input('Digite quantos dias você ficou com o carro: '))
print(f'Valor total da locação do carro R${(dias * 60) + (percorrido * 0.15):.2f}')
