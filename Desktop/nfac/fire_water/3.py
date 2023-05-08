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
    def __init__(self, width, height, blocks):
        super().__init__() 
        self.image = pygame.image.load("fire.png")
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (50, 620)
        self.width = width
        self.height = height
        self.jump_height = 11
        self.jump_velocity = 0
        self.gravity = 0.5
        self.is_jumping = False
        self.blocks = blocks  # добавить список блоков
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.is_jumping:
            if pressed_keys[pygame.K_LEFT] and self.rect.left > 30:
                self.rect.move_ip(-5, -self.jump_velocity)
            elif pressed_keys[pygame.K_RIGHT] and self.rect.right < self.width - 30:
                self.rect.move_ip(5, -self.jump_velocity)
            else:
                self.rect.move_ip(0, -self.jump_velocity)
            self.jump_velocity -= self.gravity
            if self.rect.bottom >= self.height:
                self.is_jumping = False
                self.jump_velocity = 0
        else:
            if self.rect.left > 30 and pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
            if self.rect.right < self.width - 30 and pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
            if self.rect.top > 0 and pressed_keys[pygame.K_UP] and not self.is_jumping:
                self.is_jumping = True
                self.jump_velocity = self.jump_height

        # добавить проверку столкновения с блоками
        for block in self.blocks:
            if block.rect.colliderect(self.rect.x + 5, self.rect.y, self.rect.width, self.rect.height):
                self.rect.move_ip(-5, 0)
            if block.rect.colliderect(self.rect.x - 5, self.rect.y, self.rect.width, self.rect.height):
                self.rect.move_ip(5, 0)
            if block.rect.colliderect(self.rect.x, self.rect.y + 5, self.rect.width, self.rect.height):
                self.is_jumping = False
                self.rect.move_ip(0, -5)
                self.jump_velocity = 0
            if block.rect.colliderect(self.rect.x, self.rect.y - 5, self.rect.width, self.rect.height):
                self.rect.move_ip(0, 5)
                self.jump_velocity = 0


            # for block in self.blocks:
            #     if hasattr(block, "rect") and block.rect.colliderect(self.rect.x + 5, self.rect.y, self.rect.width, self.rect.height):
            #         self.rect.move_ip(-5, 0)
            #     if hasattr(block, "rect") and block.rect.colliderect(self.rect.x - 5, self.rect.y, self.rect.width, self.rect.height):
            #         self.rect.move_ip(5, 0)
            #     if hasattr(block, "rect") and block.rect.colliderect(self.rect.x, self.rect.y + 5, self.rect.width, self.rect.height):
            #         self.is_jumping = False
            #         self.rect.move_ip(0, -5)
            #         self.jump_velocity = 0
            #     if hasattr(block, "rect") and block.rect.colliderect(self.rect.x, self.rect.y - 5, self.rect.width, self.rect.height):
            #         self.rect.move_ip(0, 5)
            #         self.jump_velocity = 0
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)




class Water(pygame.sprite.Sprite):
    def __init__(self, width, height, blocks):
        super().__init__() 
        self.image = pygame.image.load("water.png")
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (50, 620)
        self.width = width
        self.height = height
        self.jump_height = 11
        self.jump_velocity = 0
        self.gravity = 0.5
        self.is_jumping = False
        self.blocks = blocks  # добавить список блоков
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.is_jumping:
            if pressed_keys[pygame.K_a] and self.rect.left > 30:
                self.rect.move_ip(-5, -self.jump_velocity)
            elif pressed_keys[pygame.K_d] and self.rect.right < self.width - 30:
                self.rect.move_ip(5, -self.jump_velocity)
            else:
                self.rect.move_ip(0, -self.jump_velocity)
            self.jump_velocity -= self.gravity
            if self.rect.bottom >= self.height:
                self.is_jumping = False
                self.jump_velocity = 0
        else:
            if self.rect.left > 30 and pressed_keys[pygame.K_a]:
                self.rect.move_ip(-5, 0)
            if self.rect.right < self.width - 30 and pressed_keys[pygame.K_d]:
                self.rect.move_ip(5, 0)
            if self.rect.top > 0 and pressed_keys[pygame.K_w] and not self.is_jumping:
                self.is_jumping = True
                self.jump_velocity = self.jump_height

        # добавить проверку столкновения с блоками
        for block in self.blocks:
            if block.rect.colliderect(self.rect.x + 5, self.rect.y, self.rect.width, self.rect.height):
                self.rect.move_ip(-5, 0)
            if block.rect.colliderect(self.rect.x - 5, self.rect.y, self.rect.width, self.rect.height):
                self.rect.move_ip(5, 0)
            if block.rect.colliderect(self.rect.x, self.rect.y + 5, self.rect.width, self.rect.height):
                self.is_jumping = False
                self.rect.move_ip(0, -5)
                self.jump_velocity = 0
            if block.rect.colliderect(self.rect.x, self.rect.y - 5, self.rect.width, self.rect.height):
                self.rect.move_ip(0, 5)
                self.jump_velocity = 0
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)



class Block:
    def __init__(self, _x=0, _y=0, image_path="block.png"):
        super().__init__()
        self.x = _x
        self.y = _y
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


prepatsv = [Block(x, y) for x in range(25, 500, 40) for y in range(530, 570, 40)]
pol = [Block(x, y) for x in range(0, width, 40) for y in range(height-50, height, 40)]
blocks=[]
blocks.extend(prepatsv)
blocks.extend(pol)


fire_sprite = Fire(width, height, blocks)
water_sprite = Water(width, height, blocks)


# blocks = [Block(x, y) for x in range(25, 500, 50) for y in range(500, 550, 50)]

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
    for i in prepatsv:
            i.draw()

    fire_sprite.draw(screen)
    water_sprite.draw(screen)
    pygame.display.flip()



pygame.quit()