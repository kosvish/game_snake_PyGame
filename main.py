import random
import pygame
from os import path

pygame.init()

# Global variables
WIDTH = 800
HEIGHT = 600
FPS = 5

music_dir = path.join(path.dirname(__file__), 'music')

pygame.mixer.music.load(path.join(music_dir, 'main_music.mp3'))
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)

am = pygame.mixer.Sound(path.join(music_dir, 'eat_food.mp3'))
am.set_volume(0.5)

# Game Settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

# Snake cords

snake_list = []

x1 = WIDTH / 2
y1 = HEIGHT / 2

# checkout changes cords

x1_change = 0

y1_change = 0

length = 1

# Snake Size

snake_block = 30
snake_step = 30

# food cords

foodx = random.randrange(0, WIDTH - snake_block)
foody = random.randrange(0, HEIGHT - snake_block)


def eating_check(xcor, ycor, foodx, foody):
    if foodx - snake_block <= xcor <= foodx + snake_block:
        if foody - snake_block <= ycor <= foody + snake_block:
            return True
    else:
        return False


def create_mes(msg, color, x, y, font_name, size):
    font_style = pygame.font.SysFont(font_name, size)
    mes = font_style.render(msg, True, color)
    screen.blit(mes, [x, y])


def game_loop():
    # snake variables

    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0
    length = 1
    snake_list = []
    snake_head = [x1, y1]

    # food variables
    foodx = random.randrange(0, WIDTH - snake_block)
    foody = random.randrange(0, HEIGHT - snake_block)

    run = True

    game_close = False

    while run:
        while game_close:
            screen.fill("red")
            create_mes('''Вы проиграли!''', "black", 200, 200,
                       "chalkduster.ttf", 70)

            create_mes(f'Ваш счёт: {length - 1}', "black", 20, 400, "times", 35)

            create_mes('''Нажмите Q для выхода или С для повторной игры''', "white", 10, 300,
                       "times", 35)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    game_close = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                        game_close = False

                    if event.key == pygame.K_c:
                        game_loop()

            if x1 >= WIDTH or x1 <= 0 or y1 >= HEIGHT or y1 <= 0:
                game_close = True

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    game_close = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                        game_close = False

                    if event.key == pygame.K_c:
                        game_loop()

        clock.tick(FPS)

        screen.fill("blue")

        # drawing food
        pygame.draw.rect(screen, "green", [foodx, foody,
                                           snake_block, snake_block])

        create_mes(f'Текущий счёт: {length - 1}', 'grey', 0, 0, "comicsans", 25)

        pygame.display.update()

        # losing

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        # change cords

        x1 += x1_change
        y1 += y1_change

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length:
            del snake_list[0]

        for x in snake_list:
            pygame.draw.rect(screen, "black", [x[0], x[1],
                                               snake_block, snake_block])

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        if eating_check(x1, y1, foodx, foody):
            foodx = random.randrange(0, WIDTH - snake_block)
            foody = random.randrange(0, HEIGHT - snake_block)
            length += 1
            am.play()

        pygame.display.update()
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_step
                    y1_change = 0

                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_step
                    y1_change = 0

                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_step

                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_step

    pygame.quit()
    quit()


game_loop()
