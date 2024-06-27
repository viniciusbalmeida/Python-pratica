
print('========Desafio 32========')

def verificar_ano_bissexto():
    try:
        ano = int(input('Digite um ano: '))

        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print('O ano {} é bissexto! '.format(ano))
        else:
            print(f'O ano {ano} não é bissexto.')

    except ValueError:
        print('Por avor, insira um número inteiro válido')

verificar_ano_bissexto()














