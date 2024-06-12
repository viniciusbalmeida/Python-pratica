

print('========Desafio 24========')


cidade = input('Qual o nome da cidade? : ')

cidade_maiuscula = cidade.upper()

comeca_com_santo = cidade_maiuscula.startswith('SANTO')

comeca_com_santa = cidade_maiuscula.startswith('SANTA')

if comeca_com_santa:
    print("O nome da cidade começa com 'SANTA'.")
else:
    print("O nome da cidade não começa com 'SANTA'.")

if comeca_com_santo:
    print("O nome da cidade começa com 'SANTO'.")
else:
    print("O nome da cidade não começa com 'SANTO'.")








