import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BALL_SIZE = 20
PLAYER_SIZE = 50
FPS = 60

# Colors
WHITE = (255,255,255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini PING PONG Game")

# Set up the clock
clock = pygame.time.Clock()

# Initial positions
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
player1_x, player1_y = 50, HEIGHT // 2 - PLAYER_SIZE // 2
player2_x, player2_y = WIDTH - 50 - PLAYER_SIZE, HEIGHT // 2 - PLAYER_SIZE // 2

# Initial speeds
ball_speed_x, ball_speed_y = 3, 3
player_speed = 7

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= player_speed
    if keys[pygame.K_s] and player1_y < HEIGHT - PLAYER_SIZE:
        player1_y += player_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= player_speed
    if keys[pygame.K_DOWN] and player2_y < HEIGHT - PLAYER_SIZE:
        player2_y += player_speed

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collisions with walls
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_speed_y = -ball_speed_y

    # Ball collisions with players
    if (
        player1_x < ball_x < player1_x + PLAYER_SIZE
        and player1_y < ball_y < player1_y + PLAYER_SIZE
    ) or (
        player2_x < ball_x < player2_x + PLAYER_SIZE
        and player2_y < ball_y < player2_y + PLAYER_SIZE
    ):
        ball_speed_x = -ball_speed_x

    # Scoring
    if ball_x < 0 or ball_x > WIDTH:
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player1_x, player1_y, PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.rect(screen, RED, (player2_x, player2_y, PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.ellipse(screen, BLACK, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    clock.tick(FPS)