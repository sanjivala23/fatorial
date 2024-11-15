print(50 * '*', ' FATORIAL DE UM NÚMERO ', 50 * '*')

valor = 1
try:
    numero = int(input('Insere o valor a ser fatorado: '))
    valor = numero
    for i in range(1, numero):
        valor *= numero - i
    print('Fatorial de {}! = {}'.format(numero, valor))
except ValueError:
    print('Insere apenas valores numéricos!!!')