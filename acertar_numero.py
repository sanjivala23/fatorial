import random
from logging import exception

print(50 * '*', ' ACERTAR O NÚMERO ', 50 * '*')

limite = 50
acerto = False
erros = 3
aleatorio = random.randint(1, limite)

while acerto == False and erros > 0:
    try:
        question = int(input('Escolhe um número no intervalo de 1 à {}: '.format(limite)))
        if question.is_integer():
            if question > aleatorio:
                print('Número maior')
            elif question < aleatorio:
                print('Número menor')
            else:
                print('Parabéns | Você acertou o número: {}'.format(aleatorio))
                acerto = True
                break
            erros -= 1
        else:
            print('Insere apenas número inteiros')
        print('Tentativas restantes: ', erros)
    except ValueError:
        print('Insere apenas números inteiros|\n')
    print()
else:
    print('Você excedeu o número de tentativas|\nBOA SORTE PARA A PRÓXIMA')