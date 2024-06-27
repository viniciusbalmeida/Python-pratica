print('========Desafio 29========')


def ler_velocidade():
    try:
        # Lê a velocidade do carro do usuário
        velocidade = float(input("Digite a velocidade do carro em km/h: "))

        # Define o limite de velocidade
        limite_velocidade = 80.0
        multa_por_km = 7.00

        # Verifica se a velocidade ultrapassa o limite
        if velocidade > limite_velocidade:
            excesso = velocidade - limite_velocidade
            multa = excesso * multa_por_km
            print(f"Você foi multado! A velocidade é {velocidade} km/h, que é {excesso:.2f} km/h acima do limite.")
            print(f"O valor da multa é R$ {multa:.2f}")
        else:
            print(f"A velocidade do carro é {velocidade} km/h. Você está dentro do limite de velocidade.")

    except ValueError:
        print("Por favor, insira um número válido.")


# Chama a função para ler a velocidade
ler_velocidade()











