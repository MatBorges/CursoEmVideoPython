'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''
altura = float(input('Digite a altura da parede (em metros): '))
largura = float(input('Agora digite a largura da parede (em metros)'))
print(f'A área da parede é de {altura * largura:.2f} metros, você vai precisar de {(altura * largura) / 2:.3f} litros de linta para pinta-la')
