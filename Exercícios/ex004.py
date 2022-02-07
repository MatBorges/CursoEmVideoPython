'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''
algo = input('Digite algo: ')
print(f'Tipo primitivo: {type(algo)}')
print(f'É um número? {algo.isnumeric()}')
print(f'É uma letra? {algo.isalpha()}')
print(f'Está em maiúsculo? {algo.isupper()}')
