'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''
salario = float(input('Digite o salário do funcionário: R$'))
print(f'O salário do funcionário é de R${salario:.2f}, com 15% de desconto passa a ser R${salario + (salario * 0.15):.2f}')
