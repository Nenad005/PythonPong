from importlib import import_module
from turtle import right
import pygame
from settings import *


class SLIDERS():
    def __init__(self, win):
        self.body = [[], []]
        self.start_body()
        self.surface = win

    def start_body(self):
        left = pygame.Rect(0 + slider_indent, W_HEIGHT/2 - slider_height/2, slider_width, slider_height)
        right = pygame.Rect(W_WIDTH - slider_width - slider_indent, W_HEIGHT/2 - slider_height/2, slider_width, slider_height)
        self.body = [left, right]

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_w]:
            self.body[0].y -= slider_vel
        if keys_pressed[pygame.K_s]:
            self.body[0].y += slider_vel
        if keys_pressed[pygame.K_UP]:
            self.body[1].y -= slider_vel
        if keys_pressed[pygame.K_DOWN]:
            self.body[1].y += slider_vel

    def keep_in_bounds(self):
        if self.body[0].y < 0:
            self.body[0].y = 0

        elif self.body[0].y > W_HEIGHT - slider_height:
            self.body[0].y = W_HEIGHT - slider_height

        if self.body[1].y < 0:
            self.body[1].y = 0

        elif self.body[1].y > W_HEIGHT - slider_height:
            self.body[1].y = W_HEIGHT - slider_height

    def reset(self):
        self.start_body()

    def draw(self):
        pygame.draw.rect(self.surface, WHITE, self.body[0])
        pygame.draw.rect(self.surface, WHITE, self.body[1])