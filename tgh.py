import pygame
from pygame.locals import QUIT, KEYDOWN, K_a, K_b, K_c, K_d

# Inicializar Pygame
pygame.init()
tela = pygame.display.set_mode((740, 480))
pygame.display.set_caption("Jogo")
fundo = pygame.transform.scale(pygame.image.load("graficojogo.jfif"), (740, 480))
jogador = pygame.transform.scale(pygame.image.load('jogador-Photoroom.png'), (100, 100))

# Perguntas
perguntas = [
   {"pergunta": "Qual é a capital da França?", "opcoes": ["A) Londres", "B) Paris", "C) Berlim", "D) Roma"], "resposta": "B"},
   {"pergunta": "Qual é a capital da França?", "opcoes": ["A) Londres", "B) Paris", "C) Berlim", "D) Roma"], "resposta": "B"},
   {"pergunta": "Qual é o maior planeta?", "opcoes": ["A) Terra", "B) Marte", "C) Júpiter", "D) Saturno"], "resposta": "C"},
]
indice, pontos, resultado = 0, 0, ""

# Função principal
def jogo():
    global indice, pontos, resultado
    while True:
        tela.blit(fundo, (0, 0))
        tela.blit(jogador, (600, 180))

        for event in pygame.event.get():
            if event.type == QUIT: pygame.quit(); exit()
            if event.type == KEYDOWN:
                resposta = {K_a: "A", K_b: "B", K_c: "C", K_d: "D"}.get(event.key)
                if resposta == perguntas[indice]["resposta"]: pontos += 10; resultado = "Correto!"
                else: resultado = "Incorreto!"
                indice = (indice + 1) % len(perguntas)

        pygame.draw.rect(tela, (255, 165, 0), (10, 330, 720, 150))
        tela.blit(pygame.font.SysFont(None, 30).render(perguntas[indice]["pergunta"], True, (0, 0, 0)), (20, 340))
        for i, opcao in enumerate(perguntas[indice]["opcoes"]):
            tela.blit(pygame.font.SysFont(None, 30).render(opcao, True, (0, 0, 0)), (20 + i * 150, 400))

        tela.blit(pygame.font.SysFont(None, 40).render(f"Pontos: {pontos}", True, (0, 0, 0)), (540, 20))
        tela.blit(pygame.font.SysFont(None, 40).render(resultado, True, (0, 255, 0) if resultado == "Correto!" else (255, 0, 0)), (300, 150))
        pygame.display.update()

# Iniciar o jogo
jogo()
