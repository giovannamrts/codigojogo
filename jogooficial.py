import pygame
from pygame.locals import *
from sys import exit
import time

pygame.init()

tela = pygame.display.set_mode((740, 480))
pygame.display.set_caption('Jogo')

fundo_inicio = pygame.transform.scale(pygame.image.load('telastart.jfif'), (740, 480))
fundo_jogo = pygame.transform.scale(pygame.image.load('graficojogo.jfif'), (740, 480))
botao_inicio = pygame.transform.scale(pygame.image.load('botaostart.jfif'), (150, 50))
botao_inicio_rect = botao_inicio.get_rect(center=(370, 330))
jogador = pygame.transform.scale(pygame.image.load('jogador-Photoroom.png'), (100, 100))

perguntas = [
    {"pergunta": "blabla", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "B"},
    {"pergunta": "blabla", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "B"},
    {"pergunta": "blabla", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "B"},
    {"pergunta": "blabla", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "B"},
]

def mostrar_texto(texto, pos, tamanho=30, cor=(255, 255, 255)):
    fonte = pygame.font.Font(None, tamanho)
    texto_surface = fonte.render(texto, True, cor)
    tela.blit(texto_surface, pos)

def tela_inicial():
    while True:
        tela.blit(fundo_inicio, (0, 0))
        tela.blit(botao_inicio, botao_inicio_rect)

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
            if evento.type == MOUSEBUTTONDOWN and botao_inicio_rect.collidepoint(evento.pos):
                mostrar_texto("O jogo começou!", (250, 100), 50)
                pygame.display.update()
                time.sleep(2)
                return

        pygame.display.update()

def quiz():
    indice, pontos, resultado = 0, 0, ""
    while True:
        tela.blit(fundo_jogo, (0, 0))
        tela.blit(jogador, (600, 180))
        pygame.draw.rect(tela, (255, 165, 0), (10, 330, 720, 150))

        mostrar_texto(perguntas[indice]["pergunta"], (20, 340))
        for i, opcao in enumerate(perguntas[indice]["opcoes"]):
            mostrar_texto(opcao, (20 + i * 150, 400))

        mostrar_texto(f"Pontos: {pontos}", (540, 20))
        mostrar_texto(resultado, (300, 150), 40, (0, 255, 0) if resultado == "Correto!" else (255, 0, 0))

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
            if evento.type == KEYDOWN:
                resposta = {K_a: "A", K_b: "B", K_c: "C", K_d: "D"}.get(evento.key)
                if resposta == perguntas[indice]["resposta"]:
                    pontos += 10
                    resultado = "Correto!"
                else:
                    resultado = "Incorreto!"
                indice = (indice + 1) % len(perguntas)  

        pygame.display.update()

tela_inicial()
quiz()
