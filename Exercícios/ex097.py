#   Faça um programa que tenha uma função escreva() e receba um texto qualquer como parametro e mostre uma mensagem com
#   linhas de tamanho adaptavel

def escreva(msg):
    tam = len(msg) + 2
    print('-' * tam)
    print(f' {msg}')
    print('-' * tam)


escreva(input('Qual a mensagem você quer mostrar?: ').strip())
