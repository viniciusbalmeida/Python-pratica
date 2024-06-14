

print('========Desafio 23========')


numero = int(input('Coloque qualquer número inteiro de 0 a 9999 :'))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centen: {}'.format(centena))
print('Milhar: {}'.format(milhar))


#num = int(input('Informe um número: '))
#n = str(num)
#print('Analisando o número {}'.format(num))
#print('Unidade:{}'.format(n[3]))
#print('Dezena:{}'.format(n[2]))
#print('Centena:{}'.format(n[1]))
#print('Milhar:{}'.format(n[0]))



