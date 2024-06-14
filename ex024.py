print('========Desafio 24========')

cidade_maiuscula = input('Em qual cidade você nasceu ? :').strip()

cidade_maiuscula = cidade_maiuscula.upper()

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



#cid = input('Em qual cidade você nasceu? ').strip()
#print(cid[:5].upper() == 'SANTO')
#print(cid[:5].upper() == 'SANTA')




