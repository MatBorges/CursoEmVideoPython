'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''
valor = float(input('Digite o valor do produto: R$'))
print(f'Preço do produto R${valor:.2f}, com 5% de desconto o novo valor passa a ser R${valor - (valor * 0.05):.2f}')
