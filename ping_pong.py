import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping-Pong")

white = (255, 255, 255)
black = (0, 0, 0)

ball_radius = 10
paddle_width, paddle_height = 10, 100
ball_velocity = 5
paddle_velocity = 5

ball = pygame.Rect(width // 2, height // 2, ball_radius * 2, ball_radius * 2)
left_paddle = pygame.Rect(10, height // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(width - 20, height // 2 - paddle_height // 2, paddle_width, paddle_height)

ball_dx, ball_dy = ball_velocity, ball_velocity

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_velocity
    if keys[pygame.K_s] and left_paddle.bottom < height:
        left_paddle.y += paddle_velocity
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_velocity
    if keys[pygame.K_DOWN] and right_paddle.bottom < height:
        right_paddle.y += paddle_velocity

    ball.x += ball_dx
    ball.y += ball_dy

    if ball.top <= 0 or ball.bottom >= height:
        ball_dy = -ball_dy

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_dx = -ball_dx

    if ball.left <= 0 or ball.right >= width:
        ball.x, ball.y = width // 2 - ball_radius, height // 2 - ball_radius
        ball_dx, ball_dy = ball_velocity, ball_velocity

    screen.fill(black)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.rect(screen, white, left_paddle)
    pygame.draw.rect(screen, white, right_paddle)
    pygame.draw.aaline(screen, white, (width // 2, 0), (width // 2, height))

    pygame.display.flip()
    pygame.time.Clock().tick(60)
