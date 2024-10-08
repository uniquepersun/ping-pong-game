import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 20
PADDLE_SPEED = 10
BALL_SPEED_X, BALL_SPEED_Y = 7, 7

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pong-pong")

def draw_objects(left_paddle, right_paddle, ball):
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()

    left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
    
    ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y
    left_paddle_speed, right_paddle_speed = 0, 0
    left_score, right_score = 0, 0
    font = pygame.font.SysFont(None, 55)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += PADDLE_SPEED
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += PADDLE_SPEED

        ball.x += ball_dx
        ball.y += ball_dy

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_dy = -ball_dy

        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_dx = -ball_dx

        if ball.left <= 0:
            right_score += 1
            ball.x = WIDTH // 2 - BALL_SIZE // 2
            ball.y = HEIGHT // 2 - BALL_SIZE // 2
            ball_dx = -BALL_SPEED_X
            ball_dy = BALL_SPEED_Y

        if ball.right >= WIDTH:
            left_score += 1
            ball.x = WIDTH // 2 - BALL_SIZE // 2
            ball.y = HEIGHT // 2 - BALL_SIZE // 2
            ball_dx = BALL_SPEED_X
            ball_dy = BALL_SPEED_Y

        draw_objects(left_paddle, right_paddle, ball)

        score_display = font.render(f"{left_score}  {right_score}", True, WHITE)
        screen.blit(score_display, (WIDTH // 2 - score_display.get_width() // 2, 20))
        pygame.display.flip()

        clock.tick(60)  

    pygame.quit()


if __name__ == "__main__":
    main()
