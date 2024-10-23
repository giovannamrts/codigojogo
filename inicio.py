import pygame
from pygame.locals import *
from sys import exit

pygame.init()

tela = pygame.display.set_mode((740, 480))
pygame.display.set_caption('Jogo')

backgroun_start = pygame.image.load(telastart.jpeg')
start_button = pygame.image.load('botãostart.png')
button_rect = start_button.get_rect(center=(740 // 2, 480 // 2))

def start_game():
    print("O jogo começou!")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                if button_rect.collidepoint(event.pos):  # Verifica se o clique foi dentro do botão
                    start_game()  # Chama a função para iniciar o jogo


    pygame.draw.rect()
    pygame.display.update()





