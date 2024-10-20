from idlelib import window

import pygame
from pygame.locals import QUIT

pygame.init()
largura = 740
altura = 480


tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Jogo")

#gráfico
fundo = pygame.image.load("graficojogo.jfif")
novo_fundo = pygame.transform.scale(fundo, (largura,altura))
tela.blit(novo_fundo, (0, 0))


#cores

#funções

#perguntas/loop

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

