#   Faça um programa que tenha uma funçõa area(), que receba as dimenções de um terreno retangular (largura e
#   comprimento) e mostre a área do terreno

def area(lar, comp):
    print(f'A area do seu terreno é de {(lar * comp):.2f}')


lar = float(input('Qual a largura do seu terreno?: '))
comp = float(input('Qual o comprimento do seu terreno?: '))
area(lar, comp)
