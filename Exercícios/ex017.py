'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
mostre o comprimento da hipotenusa.'''
from math import hypot
oposto = float(input('Digite o valor do cateto oposto:'))
adjacente = float(input('Digite o valor do cateto adjacente:'))
print(f'Cateto oposto {oposto:.2f}, cateto adjacente {adjacente:.2f}, hipotenusa {hypot(oposto, adjacente):.2f}')
