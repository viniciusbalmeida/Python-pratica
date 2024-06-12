
#ADIÇÃO +  SUBTRAÇÃO - MULTIPLICAÇÃO *  DIVISÃO /  DIVISÃOINTEIRA //   RESTO DA DIVISÃO % POTÊNCIA **

#ORDEM DE PRECEDÊNCIA   1() 2**  3*/ // %  4 +-



#nome = input('Qual é o seu nome?')
#print('Prazer em te conhecer{:=^20}'.format (nome))

n1 = int(input('um valor:'))
n2 = int(input('Outro valor'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('Asoma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end='')
print(' a divisão inteira é {} e a potência é {:.5f}'.format(di, e))
