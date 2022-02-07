'''Faça um programa que leia nome e média de um aluno, guardando tbm a situação em um dicionário. No final, mostre o
conteúdo da estrutura na tela'''
aluno = dict()
aluno['Nome'] = input('Digite o nome do aluno: ')
aluno['Média'] = float(input('Digite a média do aluno: '))
if aluno['Média'] < 7:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Aprovado'
print(f'O aluno {aluno["Nome"]} tem média {aluno["Média"]:.2f} e está {aluno["Situação"]}')
