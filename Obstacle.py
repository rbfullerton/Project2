import pygame
from random import randint

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'bat':
            fly_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            fly_3 = pygame.image.load('graphics/fly/fly3.png').convert_alpha()
            self.frames = [fly_1, fly_2, fly_3]
            y_pos = 200
        else:
            hand_1 = pygame.image.load('graphics/hand/hand1.png').convert_alpha()
            hand_2 = pygame.image.load('graphics/hand/hand2.png').convert_alpha()
            hand_3 = pygame.image.load('graphics/hand/hand3.png').convert_alpha()
            hand_4 = pygame.image.load('graphics/hand/hand4.png').convert_alpha()
            hand_5 = pygame.image.load('graphics/hand/hand4.png').convert_alpha()
            hand_6 = pygame.image.load('graphics/hand/hand6.png').convert_alpha()
            hand_7 = pygame.image.load('graphics/hand/hand7.png').convert_alpha()
            hand_8 = pygame.image.load('graphics/hand/hand8.png').convert_alpha()
            hand_9 = pygame.image.load('graphics/hand/hand9.png').convert_alpha()
            self.frames = [hand_1, hand_1,hand_1,hand_1,hand_1, hand_2, hand_3, hand_4, hand_5, hand_6, hand_7, hand_8, hand_9, hand_9, hand_9]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
