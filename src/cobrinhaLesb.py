import pygame
import time
import random

# Inicializando o pygame
pygame.init()

# Definindo cores
black = (0, 0, 0)
red = (255, 0, 0)         # Vermelho
orange = (255, 165, 0)    # Laranja
white = (255, 255, 255)   # Branco
light_pink = (255, 182, 193)  # Rosa claro
dark_pink = (255, 105, 180)   # Rosa escuro

# Lista com as cores para a cobrinha
snake_colors = [red, orange, white, light_pink, dark_pink]

# Lista de cores para as comidinhas
food_colors = [(213, 50, 80), (0, 255, 0), (50, 153, 213), (255, 255, 0), (128, 0, 128)]

# Definindo tamanho da tela
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jogo da Cobrinha')

# Definindo o relógio
clock = pygame.time.Clock()

# Definindo tamanho dos blocos da cobra e a velocidade
block_size = 10
snake_speed = 15

# Função para desenhar a cobra
def draw_snake(block_size, snake_list):
    for index, block in enumerate(snake_list):
        color = snake_colors[index % len(snake_colors)]
        pygame.draw.rect(screen, color, [block[0], block[1], block_size, block_size])

# Função principal do jogo
def gameLoop():
    game_over = False
    game_close = False

    # Posição inicial da cobra
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Mudanças na posição
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Posição e cor da comida
    foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
    food_color = random.choice(food_colors)

    while not game_over:

        while game_close:
            screen.fill(black)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("Você perdeu! Aperte Espaço para continuar ou Q para sair", True, white)
            screen.blit(message, [screen_width / 6, screen_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Se a cobra sair dos limites da tela, o jogo acaba
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        # Desenhar a comida
        pygame.draw.rect(screen, food_color, [foodx, foody, block_size, block_size])

        # Adicionando um novo bloco na cobra
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Verificando colisão com a própria cobra
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        pygame.display.update()

        # Se a cobra comer a comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
            food_color = random.choice(food_colors)  # Nova cor para a próxima comida
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
