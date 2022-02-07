'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''
from math import trunc
num = float(input('digite um número'))
print(f'O número digitado foi {num}, sua porção inteira é {trunc(num)}')
