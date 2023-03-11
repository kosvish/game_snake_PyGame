import random
import pygame
from os import path

pygame.init()

# Global variables
WIDTH = 800
HEIGHT = 600
FPS = 5

pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# music and img dir
music_dir = path.join(path.dirname(__file__), 'music')
img_dir = path.join(path.dirname(__file__), 'img')

# img variables
bg = pygame.image.load(path.join(img_dir, 'grass.jpg')).convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
bg_rect = bg.get_rect()

food_img = [
    pygame.image.load(path.join(img_dir, 'bread.png')).convert(),
    pygame.image.load(path.join(img_dir, 'cake.png')).convert(),
    pygame.image.load(path.join(img_dir, 'crab_meat.png')).convert(),
    pygame.image.load(path.join(img_dir, 'sushi.png')).convert(),
]

head_images = [
    pygame.image.load(path.join(img_dir, "HeadR.png")).convert(),
    pygame.image.load(path.join(img_dir, "HeadL.png")).convert(),
    pygame.image.load(path.join(img_dir, "HeadB.png")).convert(),
    pygame.image.load(path.join(img_dir, "HeadT.png")).convert(),
]

tail_images = [
    pygame.image.load(path.join(img_dir, "TaleR.png")).convert(),
    pygame.image.load(path.join(img_dir, "TaleL.png")).convert(),
    pygame.image.load(path.join(img_dir, "TaleB.png")).convert(),
    pygame.image.load(path.join(img_dir, "TaleT.png")).convert(),
]

body_images = [
    pygame.image.load(path.join(img_dir, "Body.png")).convert(),
    pygame.image.load(path.join(img_dir, "BodyUD.png")).convert(),
]

game_over_img = pygame.image.load(path.join(img_dir, "LoseScreen.png"))
game_over_img = pygame.transform.scale(game_over_img, (WIDTH, HEIGHT))
game_over_img_rect = game_over_img.get_rect()

# music variables
pygame.mixer.music.load(path.join(music_dir, 'main_music.mp3'))
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)

am = pygame.mixer.Sound(path.join(music_dir, 'eat_food.mp3'))
am.set_volume(0.5)

# Snake cords

snake_list = []

x1 = WIDTH / 2
y1 = HEIGHT / 2

# checkout changes cords

x1_change = 0

y1_change = 0

length = 2

# Snake Size

snake_block = 50
snake_step = 30

# food cords

foodx = random.randrange(0, WIDTH - snake_block)
foody = random.randrange(0, HEIGHT - snake_block)

# message



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


def draw_head(i, snake_list):
    snake_head_img = head_images[i]
    snake_head = pygame.transform.scale(snake_head_img, (snake_block, snake_block))
    snake_head.set_colorkey("white")
    snake_head_rect = snake_head.get_rect(x=snake_list[-1][0], y=snake_list[-1][1])
    screen.blit(snake_head, snake_head_rect)


def draw_tail(i, snake_list):
    snake_tail_img = tail_images[i]
    snake_tail = pygame.transform.scale(snake_tail_img, (snake_block, snake_block))
    snake_tail.set_colorkey("white")
    snake_tail_rect = snake_tail.get_rect(x=snake_list[0][0], y=snake_list[0][1])
    screen.blit(snake_tail, snake_tail_rect)


def game_loop():
    # snake variables

    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0
    length = 2
    snake_head = [x1, y1]

    # food variables
    foodx = random.randrange(0, WIDTH - snake_block)
    foody = random.randrange(0, HEIGHT - snake_block)

    food = pygame.transform.scale(random.choice(food_img), (50, 50))
    food.set_colorkey("black")
    food_rect = food.get_rect(x=foodx, y=foody)

    run = True

    game_close = False

    i = 0

    a = 0

    while run:
        while game_close:
            screen.blit(game_over_img, game_over_img_rect)

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

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                        game_close = False

                    if event.key == pygame.K_c:
                        game_loop()

        clock.tick(FPS)

        screen.fill("blue")
        screen.blit(bg, bg_rect)

        # drawing food

        screen.blit(food, food_rect)

        # pygame.draw.rect(screen, "green", [foodx, foody,
        #                                    snake_block, snake_block])

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
        draw_head(i, snake_list)
        draw_tail(i, snake_list)

        if len(snake_list) + 1 > length:
            del snake_list[0]

        for x in snake_list:
            if a == 0:
                snake_img = pygame.image.load(path.join(img_dir, 'Body.png')).convert()
                snake = pygame.transform.scale(snake_img, (snake_block, snake_block))
                snake.set_colorkey("white")
                screen.blit(snake, (x[0], x[1]))
            elif a == 1:
                snake_img = pygame.image.load(path.join(img_dir, 'BodyUD.png')).convert()
                snake = pygame.transform.scale(snake_img, (snake_block, snake_block))
                snake.set_colorkey("white")
                screen.blit(snake, (x[0], x[1]))

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        if eating_check(x1, y1, foodx, foody):
            foodx = random.randrange(0, WIDTH - snake_block)
            foody = random.randrange(0, HEIGHT - snake_block)
            food = pygame.transform.scale(random.choice(food_img), (30, 30))
            food.set_colorkey("black")
            food_rect = food.get_rect(x=foodx, y=foody)
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
                    i = 1
                    a = 0

                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_step
                    y1_change = 0
                    i = 0
                    a = 0

                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_step
                    i = 3
                    a = 1

                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_step
                    i = 2
                    a = 1
    pygame.quit()
    quit()


game_loop()
