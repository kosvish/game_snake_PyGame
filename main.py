import random
import pygame

pygame.init()

# Global variables
WIDTH = 800
HEIGHT = 600
FPS = 5

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


run = True

while run:

    clock.tick(FPS)

    screen.fill("blue")

    # drawing food
    pygame.draw.rect(screen, "green", [foodx, foody,
                                       snake_block, snake_block])

    # losing

    if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
        run = False

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
            run = False

    if eating_check(x1, y1, foodx, foody):
        foodx = random.randrange(0, WIDTH - snake_block)
        foody = random.randrange(0, HEIGHT - snake_block)
        length += 1

    pygame.display.update()
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

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
