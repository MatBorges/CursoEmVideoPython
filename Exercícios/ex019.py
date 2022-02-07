'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
nome dos alunos e escrevendo na tela o nome do escolhido.'''
import random
alunos = [input('Digite o nome do primeiro aluno: '), input('Digite o nome do segundo aluno: '), input('Digite o nome do terceiro aluno: '), input('Digite o nome do quarto aluno: ')]

print(f'O aluno escolhido foi {random.choice(alunos)}')
