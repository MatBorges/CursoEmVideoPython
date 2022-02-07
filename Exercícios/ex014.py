'''Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''
celsius = float(input('Digite a temperatura em graus Celsius: Cº'))
print(f'{celsius}ºC são {(((celsius * 9) / 5) + 32):.1f}ºF')
