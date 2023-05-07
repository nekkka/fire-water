import pygame
import os
import random

os.chdir('C:/Users/ASUS/Desktop/nfac/fire_water') 
pygame.init()
width = 1200
height = 700

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fire and water")


class Fire(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__() 
        self.image = pygame.image.load("fire.png")
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (50, 620)
        self.width = width
        self.height = height
        self.jump_height = 10
        self.jump_velocity = 0
        self.gravity = 0.5
        self.is_jumping = False
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.is_jumping:
            self.rect.move_ip(0, -self.jump_velocity)
            self.jump_velocity -= self.gravity
            if self.rect.bottom >= self.height:
                self.is_jumping = False
                self.jump_velocity = 0
        else:
            if self.rect.left > 30:
                if pressed_keys[pygame.K_LEFT]:
                    self.rect.move_ip(-5, 0)
            if self.rect.right < self.width - 30:        
                if pressed_keys[pygame.K_RIGHT]:
                    self.rect.move_ip(5, 0)
            if self.rect.top > 0:
                if pressed_keys[pygame.K_UP] and not self.is_jumping:
                    self.is_jumping = True
                    self.jump_velocity = self.jump_height

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Water(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__() 
        self.image = pygame.image.load("water.png")
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (50, 620)
        self.width = width
        self.height = height
        self.jump_height = 10
        self.jump_velocity = 0
        self.gravity = 0.5
        self.is_jumping = False
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.is_jumping:
            self.rect.move_ip(0, -self.jump_velocity)
            self.jump_velocity -= self.gravity
            if self.rect.bottom >= self.height:
                self.is_jumping = False
                self.jump_velocity = 0
        else:
            if self.rect.left > 30:
                if pressed_keys[pygame.K_a]:
                    self.rect.move_ip(-5, 0)
            if self.rect.right < self.width - 30:        
                if pressed_keys[pygame.K_d]:
                    self.rect.move_ip(5, 0)
            if self.rect.top > 0:
                if pressed_keys[pygame.K_w] and not self.is_jumping:
                    self.is_jumping = True
                    self.jump_velocity = self.jump_height

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Block:
    def __init__(self, _x=0, _y=0, image_path="block.png"):
        super().__init__()
        self.x = _x
        self.y = _y
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

    def draw(self):
        screen.blit(self.image, (self.x, self.y))



fire_sprite = Fire(width, height)
water_sprite = Water(width, height)
blocks = [Block(x, y) for x in range(0, 1200, 100) for y in range(0, 600, 100)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    oblozhka = pygame.image.load('bg.png')
    oblozhka = pygame.transform.scale(oblozhka, (1200, 700))
    screen.blit(oblozhka, (0 , 0))

    fire_sprite.update()
    water_sprite.update()
    for block in blocks:
            block.draw()

    fire_sprite.draw(screen)
    water_sprite.draw(screen)
    pygame.display.flip()




pygame.quit()