import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Quiz de Basquete')

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonte
font = pygame.font.Font(None, 36)

# Perguntas e respostas
questions = [
    {
        'question': 'Qual jogador é conhecido como "King James"?',
        'options': ['Michael Jordan', 'LeBron James', 'Kobe Bryant', 'Larry Bird'],
        'answer': 'LeBron James'
    },
    {
        'question': 'Qual time tem mais títulos da NBA?',
        'options': ['Los Angeles Lakers', 'Boston Celtics', 'Chicago Bulls', 'Miami Heat'],
        'answer': 'Boston Celtics'
    }
]

# Variáveis do jogo
current_question = 0
team_turn = 0
teams = ['Time A', 'Time B']
score = [0, 0]
waiting_for_answer = False

def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

def reset_game():
    global current_question, team_turn, waiting_for_answer
    current_question = 0
    team_turn = 0
    waiting_for_answer = False
    score[0] = 0
    score[1] = 0

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and waiting_for_answer:
            if event.key == pygame.K_1:
                player_answer = questions[current_question]['options'][0]
            elif event.key == pygame.K_2:
                player_answer = questions[current_question]['options'][1]
            elif event.key == pygame.K_3:
                player_answer = questions[current_question]['options'][2]
            elif event.key == pygame.K_4:
                player_answer = questions[current_question]['options'][3]

            if player_answer == questions[current_question]['answer']:
                score[team_turn] += 1
                result_text = f"{teams[team_turn]} acertou a cesta!"
            else:
                result_text = f"{teams[team_turn]} errou a cesta!"

            team_turn = (team_turn + 1) % 2
            current_question += 1
            waiting_for_answer = False

        if event.type == pygame.KEYDOWN and not waiting_for_answer:
            if event.key == pygame.K_SPACE and current_question < len(questions):
                waiting_for_answer = True
                result_text = ""

    # Limpar tela
    screen.fill(WHITE)

    # Desenhar perguntas e opções
    if current_question < len(questions):
        draw_text(questions[current_question]['question'], 20, 50)
        for i, option in enumerate(questions[current_question]['options']):
            draw_text(f"{i + 1}. {option}", 20, 100 + i * 40)

    # Exibir resultado
    if result_text:
        draw_text(result_text, 20, 300)

    # Exibir pontuação
    draw_text(f"{teams[0]}: {score[0]}", 20, 500)
    draw_text(f"{teams[1]}: {score[1]}", 20, 550)

    # Atualizar tela
    pygame.display.flip()

    # Aguardar próximo evento
    if not waiting_for_answer and current_question >= len(questions):
        draw_text("Fim de Jogo! Pressione R para reiniciar", 20, 400)
        pygame.display.flip()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            reset_game()
