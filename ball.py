import pygame
import math
import settings as stn


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, mouse_x, mouse_y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image=pygame.Surface((40,40))
        self.image.fill(stn.BLACK)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 15
        self.angle = math.atan2(y - mouse_y, x - mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        
    def update(self):
        self.rect.x -= int(self.x_vel)
        self.rect.y -= int(self.y_vel)
        
        
        # pygame.draw.circle(display, (0, 0, 0), (self.x, self.y), 5)
        