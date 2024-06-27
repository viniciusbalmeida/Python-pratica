
print('========Desafio 31========')

distancia = float(input('Digite a distância da viagem em Km: '))

preco_curta_distancia = 0.50
preco_longa_distancia = 0.45

if distancia <= 200:
    preco = distancia * preco_curta_distancia
else:
    preco = distancia * preco_longa_distancia
print('O preço da passagem para a viagem de {} Km custa R$ {:.2f}'.format(distancia, preco))


#def calcular_preco_passagem():
    #try:
        # Lê a distância da viagem em quilômetros
        #distancia = float(input("Digite a distância da viagem em Km: "))

        # Define os preços por quilômetro
        #preco_curta_distancia = 0.50
        #preco_longa_distancia = 0.45

        # Calcula o preço da passagem com base na distância
        #if distancia <= 200:
            #preco = distancia * preco_curta_distancia
        #else:
            #preco = distancia * preco_longa_distancia

        #print(f"O preço da passagem para uma viagem de {distancia} Km é R$ {preco:.2f}")

    #except ValueError:
        #print("Por favor, insira um valor numérico válido para a distância.")

# Chama a função para calcular o preço da passagem
#calcular_preco_passagem()











