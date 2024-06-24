import random

print('========Desafio 28========')

def pensar_numero():
    return random.randint(0, 5)

numero_pensado = pensar_numero()

print('Pensei em um número entre 0 e 5. Consegue adivinhar qual é?')

palpite = None

while palpite!= numero_pensado:
    palpite = int(input('digite seu palpite: '))

    if palpite == numero_pensado:
        print(f'Parabéns! Você adivinhou o número {numero_pensado}.')
    else:
        print('Tente novamente!')







