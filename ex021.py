import pygame
print('========Desafio 21========')


# Inicializa o mixer do Pygame
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load('ANALAGA, João Gustavo u0026 Murilo (Lençol Dobrado) bydb.mp3')

# Inicia a reprodução do arquivo
pygame.mixer.music.play()

# Aguarda até que a música termine
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)










