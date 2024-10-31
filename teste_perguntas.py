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
jogador = pygame.transform.scale(pygame.image.load('jogador-Photoroom.png'), (100, 120))
botao_rect = botao_inicio.get_rect(center=(370, 330))
jogador_rect = jogador.get_rect(center=(600, 230))

sprite_sheet = pygame.image.load('com-effects-1--unscreen-ezgif.com-gif-to-sprite-converter.png')

# Dividir a sprite sheet em 5 colunas e 18 linhas
quadro_largura = sprite_sheet.get_width() // 5
quadro_altura = sprite_sheet.get_height() // 10
quadros_bola = []

# Extrair e redimensionar cada quadro
for j in range(10):  # 18 linhas
    for i in range(5):  # 5 colunas
        quadro = sprite_sheet.subsurface((i * quadro_largura, j * quadro_altura, quadro_largura, quadro_altura))
        quadro_redimensionado = pygame.transform.scale(quadro, (700, 300))  # Redimensiona para o tamanho do fundo
        quadros_bola.append(quadro_redimensionado)

perguntas = [{"pergunta": " Qual é o valor de (-2/4)^4", "opcoes": ["A) 4/2", "B)16/81", "C) 0,5", "D) 0"], "resposta": "B"},
            {"pergunta": "A soma das raizes quadrada de 1024 + 625 ", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "D"},
            {"pergunta": "O resultado de 7^4 . 7^9 é: ", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "D"},
            {"pergunta": "Qual o resultado da soma dos ângulos internos de um triângulo?", "opcoes": ["A) 180°", "B) 90°", "C)30°", "D)60°"], "resposta": "A"},
            {"pergunta": "O que representa o seno em um triângulo retângulo? ", "opcoes": ["A)cateto oposto/hipotenusa", "B)CA/CO", "C) Hipotenusa", "D) Nenhuma das Anteriores"], "resposta": "A"},
            {"pergunta": "A formula da lei dos senos e cossenos é: a/senA = b/senB = c/senC; a² + b² + c² - 2.b.c. cos a", "opcoes": ["A) Verdadeiro", "B) Falso", ], "resposta": "A"},
            {"pergunta": "A soma da raiz quadrada ", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "D"},
            {"pergunta": " Qual é o valor de (-2/4)^4", "opcoes": ["A) 4/2", "B)16/81", "C) 0,5", "D) 0"], "resposta": "B"},
            {"pergunta": "Sendo A = {0,11,12,13,14} e B = {11,12}, a intercecção e união das duas é igual:", "opcoes": ["A) Intersecção: {0,11,12,13,14}; União: {11,12}", "B)Intersecção e União: {0}", "C)Intersecção: {0}; União:{0,11,12,13,14} ", "D) Intersecção: {11,12}; União: {0,11,12,13,14}"], "resposta": "D"},
            {"pergunta": "O resultado de 4x + 2 = 10 é: ", "opcoes": ["A) 2,5", "B)10/4", "C)2", "D)0"], "resposta": "C"},
            {"pergunta": "O resultado da inequação 2(x + 3) > 3(1-x) é: ", "opcoes": ["A) 0.6", "B)5/3", "C)3/5", "D)-3/5"], "resposta": "D"},
            {"pergunta": "A soma da raiz quadrada ", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "D"},
            {"pergunta": "A soma da raiz quadrada ", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "D"},
            {"pergunta": "A soma da raiz quadrada ", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "D"},
            {"pergunta": "A soma da raiz quadrada ", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "D"},
            {"pergunta": "A soma da raiz quadrada ", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "D"},
            {"pergunta": "A soma da raiz quadrada ", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "D"},
            {"pergunta": "A soma da raiz quadrada ", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "D"},
            {"pergunta": "A soma da raiz quadrada ", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "D"},
            {"pergunta": "A soma da raiz quadrada ", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "D"},


]

def texto(msg, pos, tam=30, cor=(0, 0, 0)):
    tela.blit(pygame.font.Font(None, tam).render(msg, True, cor), pos)

def contagem_regressiva():
    for contador in range(3, 0, -1):
        tela.blit(fundo_jogo, (0, 0))
        texto(f"O jogo vai começar em {contador}...", (210, 140), 50, (0, 0, 0))
        pygame.display.update()
        time.sleep(1)

def animacao_bola():
    x, y = 0, 0  # Posição da animação (ajustado para cobrir a tela inteira)
    for quadro in quadros_bola:
        tela.blit(fundo_jogo, (0, 0))
        tela.blit(jogador, jogador_rect)
        tela.blit(quadro, (x, y))  # Exibe cada quadro da bola em sequência
        pygame.display.update()
        time.sleep(0.05)  # Intervalo entre quadros para criar efeito de animação


def jogo():
    while True:
        tela.blit(fundo_inicio, (0, 0))
        tela.blit(botao_inicio, botao_rect)
        if any(e.type == MOUSEBUTTONDOWN and botao_rect.collidepoint(e.pos) for e in pygame.event.get() if e.type != QUIT):
            contagem_regressiva()
            break
        pygame.display.update()

    indice, pontos, resultado, nivel, acertos_consecutivos, erros_consecutivos = 0, 0, "", 1, 0, 0
    while True:
        if erros_consecutivos >= 5:  # Fim de jogo por 5 erros consecutivos
            tela.fill((0, 0, 0))
            texto("Fim de Jogo", (300, 200), 50, (255, 0, 0))
            texto("Você cometeu 5 erros consecutivos!", (180, 260), 40, (255, 255, 0))
            texto(f"Pontuação final: {pontos}", (270, 320), 40, (255, 255, 0))
            texto(f"Nível alcançado: {nivel}", (270, 360), 40, (255, 255, 0))
            pygame.display.update()
            time.sleep(3)
            return

        tela.blit(fundo_jogo, (0, 0))
        tela.blit(jogador, jogador_rect)
        pygame.draw.rect(tela, (255, 165, 0), (10, 330, 720, 150))
        texto(perguntas[indice]["pergunta"], (20, 340))
        for i, opcao in enumerate(perguntas[indice]["opcoes"]):
            texto(opcao, (20 + i * 150, 400))
        texto(f"Pontos: {pontos}", (540, 20))
        texto(f"Nível: {nivel}", (540, 60))
        texto(resultado, (300, 150), 40, (0, 255, 0) if resultado == "Correto!" else (255, 0, 0))

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit(), exit()
            elif evento.type == KEYDOWN:
                resposta = {K_a: "A", K_b: "B", K_c: "C", K_d: "D"}.get(evento.key)
                if resposta == perguntas[indice]["resposta"]:
                    pontos += 10
                    resultado = "Correto!"
                    acertos_consecutivos += 1
                    erros_consecutivos = 0
                    if acertos_consecutivos == 5:  # Alcançou 5 acertos consecutivos
                        nivel += 1
                        acertos_consecutivos = 0
                    animacao_bola()

                else:
                    resultado = "Incorreto!"
                    acertos_consecutivos = 0
                    erros_consecutivos += 1
                indice = (indice + 1) % len(perguntas)  # Continua para próxima pergunta
        pygame.display.update()

jogo()
