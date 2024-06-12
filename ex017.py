import math
print('========Desafio 17========')

co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = math.hypot(co, ca)
print('A hipotesusa  vai medir {:.2f}'.format(hi))
