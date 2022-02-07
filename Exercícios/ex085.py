'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
numeros = [[], []]
for i in range(0, 7):
    numero = int(input(f'Digite o {i + 1}º número: '))
    if (numero % 2) == 0:
        if len(numeros[0]) == 0:
            numeros[0].append(numero)
        else:
            for j in numeros[0]:
                if numero >= max(numeros[0]):
                    numeros[0].append(numero)
                    break
                elif j <= numero:
                    numeros[0].insert(numeros[0].index(j), numero)
                    break
    else:
        if len(numeros[1]) == 0:
            numeros[1].append(numero)
        else:
            for h in numeros[1]:
                if numero >= max(numeros[1]):
                    numeros[1].append(numero)
                    break
                elif h <= numero:
                    numeros[1].insert(numeros[1].index(h), numero)
                    break
print(f'Números pares: {numeros[0]} e numeros ìmpares {numeros[1]}')
