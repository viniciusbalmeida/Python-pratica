print('========Desafio 11========')

print('Saiba quantos litros de tinta precisará para pintar sua parede'.upper())

largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))
area = largura * altura
print('Sua parede tem a dimenssão de {}m x {}m e a sua área é de  {:.2f}m²'.format(largura, altura, area))
tinta = area / 2
print('Você precisará de {:.2f}l de tinta para pitar essa parede!'.format(tinta))












