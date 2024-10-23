import pygame
from pygame.locals import QUIT
import sys

pygame.init()
pygame.font.init()
largura = 740
altura = 480


tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Jogo")

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

#gráfico
fundo = pygame.image.load("graficojogo.jfif")
novo_fundo = pygame.transform.scale(fundo, (largura,altura))
tela.blit(novo_fundo, (0, 0))

jogador = pygame.image.load('jogador-Photoroom.png')
novo_jogador = pygame.transform.scale(jogador, (100,100))
tela.blit(novo_jogador, (600,180))
#mudança de imagens






#cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

#funções

#perguntas/loop
perguntas = [
    {
        "pergunta": "Qual é a capital da França?",
        "opcoes": ["A) Londres", "B) Paris", "C) Berlim", "D) Roma"],
        "resposta": "B"
    },
    {
        "pergunta": "Qual é o maior planeta do Sistema Solar?",
        "opcoes": ["A) Terra", "B) Marte", "C) Júpiter", "D) Saturno"],
        "resposta": "C"
    },
    # Adicione mais perguntas aqui
]

# Função para desenhar o texto na tela
def desenhar_texto(tela, texto, x, y, (255,255,255)):
    text_surface = fonte.render(texto, True, (255,255,255))
    tela.blit(text_surface, (x, y))

# Função principal do jogo
def jogo():
    indice_pergunta = 0
    resposta_correta = False
    mostrar_resultado = False
    tempo_mostrar_resultado = 0

    while True:
        # Preencher a tela com preto
        tela.fill(novo_fundo)

        # Evento de saída
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Captura a resposta do jogador se não estamos mostrando resultado
            if evento.type == pygame.KEYDOWN and not mostrar_resultado:
                if evento.key == pygame.K_a:
                    resposta = "A"
                elif evento.key == pygame.K_b:
                    resposta = "B"
                elif evento.key == pygame.K_c:
                    resposta = "C"
                elif evento.key == pygame.K_d:
                    resposta = "D"
                else:
                    resposta = None

                if resposta:
                    if resposta == perguntas[indice_pergunta]["resposta"]:
                        resposta_correta = True
                    else:
                        resposta_correta = False

                    # Mostrar o resultado por 2 segundos
                    mostrar_resultado = True
                    tempo_mostrar_resultado = pygame.time.get_ticks()

        # Exibir a pergunta e as opções na tela se não estiver mostrando resultado
        if not mostrar_resultado:
            if indice_pergunta < len(perguntas):
                pergunta_atual = perguntas[indice_pergunta]
                desenhar_texto(tela, pergunta_atual["pergunta"], 50, 100)
                for i, opcao in enumerate(pergunta_atual["opcoes"]):
                    desenhar_texto(tela, opcao, 50, 200 + i * 50)
        else:
            # Exibir "Correto" ou "Incorreto" dependendo da resposta
            if resposta_correta:
                desenhar_texto(tela, "Correto!", 350, 300, VERDE)
            else:
                desenhar_texto(tela, "Incorreto!", 350, 300, VERMELHO)

            # Verificar se já se passaram 2 segundos para mudar a pergunta
            if pygame.time.get_ticks() - tempo_mostrar_resultado > 2000:
                mostrar_resultado = False
                indice_pergunta += 1

                # Reinicia o jogo após a última pergunta
                if indice_pergunta >= len(perguntas):
                    indice_pergunta = 0



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
