'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por acaso a CTPS for diferente de ZERO, o dicionário receberá tbm o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar '''
from datetime import datetime
pessoa = {}
anoAtual = datetime.now().year
pessoa['Nome'] = input('Digite o nome: ').strip()
pessoa['Idade'] = anoAtual - int(input('Digite o ano de nascimento: '))
pessoa['carteira'] = int(input('Digite o numero da carteira: '))
if pessoa['carteira'] != 0:
    pessoa['AnoContratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['Salario'] = float(input('Digite o salário: R$'))
    pessoa['IdadeDaAposentadoria'] = ((pessoa['AnoContratacao'] + 35) - anoAtual) + (pessoa['Idade'])
for i, j in pessoa.items():
    if i == 'Salario':
        print(f'{i}: R${j:.2f}')
    else:
        print(f'{i}: {j}')
