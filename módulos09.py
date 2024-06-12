import lean as lean

#Fatiamento

frase = '   Curso em vídeo Python   '

print(frase[9::2])

#Análise

len(frase)
print(len)

print(frase.count('o'))
print(frase.count('o', 0, 14))
print(frase.find('deo'))
print(frase.find('Androide'))
print('Curso' in frase)
print(frase.upper().replace('Python','Android'.format().upper()))
#print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.lstrip())
print(frase.rstrip())
print(frase.split())
#Jução
print('-'.join(frase))
dividido = frase.split()
print(dividido[2][3])










