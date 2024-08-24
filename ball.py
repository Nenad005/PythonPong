import pygame, random

from settings import BLACK, W_HEIGHT, W_WIDTH, WHITE, ball_size, ball_speed

class BALL:
    def __init__(self, win):
        self.body = pygame.Rect(W_WIDTH/2 - ball_size/2, W_HEIGHT/2 - ball_size/2, ball_size, ball_size)
        self.surface = win
        self.vector = [0, 0]
        self.start_vector()
        self.moved = False

    def start_vector(self):
        random.seed()
        if bool(random.choice([True, False])): 
            self.vector[0] = ball_speed
        else : self.vector[0] = -ball_speed 
        self.vector[1] = 0

    def move(self):
        self.body.x += self.vector[0]
        self.body.y += self.vector[1]

    def check_col(self, sliders):

        #TOP AND BOTTOM BOUNDS
        if self.body.y < 0 :
            self.body.y = 0
            self.vector[1] = -self.vector[1]
        if self.body.y > W_HEIGHT - ball_size:
            self.body.y = W_HEIGHT - ball_size
            self.vector[1] = -self.vector[1]

        #LEFT AND RIGHT - END GAME
        if self.body.x <= 0 - ball_size:
            self.draw()
            self.reset()
            sliders.reset()
            return True
        if self.body.x >= W_WIDTH:
            self.draw()
            self.reset()
            sliders.reset()
            return True
        #SLIDERS

        if not self.body.colliderect(sliders.body[0]) and not self.body.colliderect(sliders.body[1]):
            self.moved = False

        #LEFT
        if self.body.colliderect(sliders.body[0]) and not self.moved:
            if self.body.left < sliders.body[0].right:
                self.body.left < sliders.body[0].right
            self.vector[0] = -self.vector[0]
            self.vector[1] = self.random_vector()
            self.moved = True

        #RIGHT
        if self.body.colliderect(sliders.body[1]) and not self.moved:
            if self.body.right > sliders.body[1].left:
                self.body.right > sliders.body[1].left
            self.vector[0] = -self.vector[0]
            self.vector[1] = self.random_vector()
            self.moved = True

        return False

    def reset(self):
        self.body = pygame.Rect(W_WIDTH/2 - ball_size/2, W_HEIGHT/2 - ball_size/2, ball_size, ball_size)
        self.start_vector()

    def random_vector(self):
        random.seed()
        return random.randint(0, int(ball_speed))

    def draw(self):
        #pygame.draw.rect(self.surface, WHITE, self.body)
        pygame.draw.circle(self.surface, WHITE, (self.body.x + ball_size/2, self.body.y + ball_size/2), ball_size/2)