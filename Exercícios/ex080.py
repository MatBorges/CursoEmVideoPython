'''Crie um programa onde o usuário possa digitas 5 valores numéricos e casdastre-os em uma lista, já na posição correta
de inserção (sem usar .sort()) no final mostre a lista ordenada na tela'''
numeros = []
for i in range(0, 5):
    numero = int(input(f'Digite o numero da {i + 1}ª posição da lista: '))
    if i == 0:
        numeros.append(numero)
    else:
        if numero >= max(numeros):
            numeros.append(numero)
        else:
            for e in numeros:
                if numero <= e:
                    numeros.insert(numeros.index(e), numero)
                    break
print(f'Lista ordenada {numeros}')
