import pygame, sys
from settings import W_HEIGHT, W_WIDTH, WHITE, BLACK
from sliders import SLIDERS
from ball import BALL

WIN = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
pygame.display.set_caption('PONG')

sliders = SLIDERS(WIN)
ball = BALL(WIN)

class Game_State:
    def __init__(self):
        self.state = 'pause'

    def main(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys_pressed = pygame.key.get_pressed()


        WIN.fill(BLACK)
        pygame.draw.line(WIN, WHITE, (W_WIDTH/2, 0), (W_WIDTH/2, W_HEIGHT), 5)

        sliders.move(keys_pressed)
        ball.move()

        sliders.keep_in_bounds()
        if ball.check_col(sliders): self.state = 'pause'

        sliders.draw()
        ball.draw()

        pygame.display.flip()


    def pause(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = 'main'
        
        WIN.fill(BLACK)
        pygame.draw.line(WIN, WHITE, (W_WIDTH/2, 0), (W_WIDTH/2, W_HEIGHT), 5)

        sliders.draw()
        ball.draw()

        pygame.display.flip()

    def State_Setter(self):
        if self.state == 'main': self.main()
        if self.state == 'pause': self.pause()

def main():
    gameloop = Game_State()
    clock = pygame.time.Clock()

    while True:
        gameloop.State_Setter()
        clock.tick(60)

if __name__ == '__main__':
    main()