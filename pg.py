import random
import pygame

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating the game window
screenwidth = 900
screenheight = 600
gamewindow = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("My Game")

# Game-specific variables
exitgame = False
gameover = False
velocity_x = 0
velocity_y = 0
snake_size = 10
snake_x = 45
snake_y = 55
fps = 40
score = 0
food_size = 10
init_velocity = 5

food_x = random.randint(10, int(screenwidth / 2))
food_y = random.randint(10, int(screenheight / 2))

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

# Functions
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])

def plot_snake(gamewindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])

snk_list = []
snk_length = 1

# Game loop
while not exitgame:
    if gameover:
        gamewindow.fill(white)
        text_screen("Game Over! Press Enter to Restart", red, screenwidth // 4, screenheight // 3)
        pygame.display.update()

        # Handling restart after game over
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitgame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Resetting variables for new game
                    gameover = False
                    snake_x = 45
                    snake_y = 55
                    velocity_x = 0
                    velocity_y = 0
                    snk_list = []
                    snk_length = 1
                    score = 0
                    food_x = random.randint(10, int(screenwidth / 2))
                    food_y = random.randint(10, int(screenheight / 2))

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitgame = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and velocity_x != -init_velocity:
                    velocity_x = init_velocity
                    velocity_y = 0

                if event.key == pygame.K_LEFT and velocity_x != init_velocity:
                    velocity_x = -init_velocity
                    velocity_y = 0

                if event.key == pygame.K_UP and velocity_y != init_velocity:
                    velocity_y = -init_velocity
                    velocity_x = 0

                if event.key == pygame.K_DOWN and velocity_y != -init_velocity:
                    velocity_y = init_velocity
                    velocity_x = 0

        snake_x += velocity_x
        snake_y += velocity_y

        # Check for food collision
        if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
            score += 1
            print("Score:", score * 10)
            food_x = random.randint(10, int(screenwidth / 2))
            food_y = random.randint(10, int(screenheight / 2))
            snk_length += 5

        # Game over conditions
        if snake_x < 0 or snake_x > screenwidth or snake_y < 0 or snake_y > screenheight:
            gameover = True

        # Adding head position to snake body
        head = []
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)

        if len(snk_list) > snk_length:
            del snk_list[0]

        # Check for self-collision
        if head in snk_list[:-1]:
            gameover = True

        gamewindow.fill(white)
        text_screen("Score: " + str(score * 10), red, 5, 5)
        pygame.draw.rect(gamewindow, red, [food_x, food_y, food_size, food_size])
        plot_snake(gamewindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

pygame.quit()
quit()
