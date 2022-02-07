'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''
import math
angulo = float(input('Digite o valor do ângulo: '))
print(f'Para o ângulo de {angulo} o seno é {math.sin(math.radians(angulo)):.2f}, o cosseno {math.cos(math.radians(angulo)):.2f} e a tangente é {math.tan(math.radians(angulo)):.2f}')
