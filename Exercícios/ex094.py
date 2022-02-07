# Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média
pessoas = []
mulheres = []
acimaMedia = []
pessoa = {}
cont = 0
idade = 0
func = True
while func:
    cont += 1
    pessoa['Nome'] = input(f'Digite o nome da {cont}ª pessoa: ')
    while True:
        sexo = input(f'Digite o sexo de {pessoa["Nome"]}: ').strip().upper()[0]
        if sexo in 'FM':
            pessoa['Sexo'] = sexo
            break
        else:
            print('Opção inválida, por favor digite "M" ou "F"')
    pessoa['Idade'] = int(input(f'Digite a idade de {pessoa["Nome"]}: '))
    idade += pessoa['Idade']
    pessoas.append(pessoa.copy())
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa.copy())
    print(f'{pessoa["Nome"]} cadastrado(a) com sucesso!!!')
    pessoa.clear()
    while True:
        resp = input('Deseja cadastrar mais alguma pessoa?: (S/N)').strip().upper()[0]
        if resp == 'N':
            func = False
            break
        elif resp == 'S':
            print('Continuando o cadastro!!!')
            break
        else:
            print('Opção inválida, por favor digite apenas ("S" ou "N")')
idade = idade / len(pessoas)
for i in pessoas:
    if i['Idade'] > idade:
        acimaMedia.append(i.copy())
cont = 0
print(f'\033[1;33mPessoas cadastradas:\033[m')
for i in pessoas:
    cont += 1
    print(f'{cont}: {i}')
cont = 0
print(f'\033[1;35mMulheres cadastradas:\033[m')
for i in mulheres:
    cont += 1
    print(f'{cont}: {i}')
cont = 0
print(f'\033[1;31mPessoas acima da média de idade\033[m que é de {idade:.2f} anos')
for i in acimaMedia:
    cont += 1
    print(f'{cont}: {i}')
