import pygame
import os
import time
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
        self.jump_height = 10
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
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)




class Water(pygame.sprite.Sprite):
    def __init__(self, width, height, blocks):
        super().__init__() 
        self.image = pygame.image.load("water.png")
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (90, 620)
        self.width = width
        self.height = height
        self.jump_height = 10
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




class Lava(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('zhizha.png')
		self.image = pygame.transform.scale(img, (60, 60))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
                
# class Platform(pygame.sprite.Sprite):
# 	def __init__(self, x, y):
# 		pygame.sprite.Sprite.__init__(self)
# 		img = pygame.image.load('platform.png')
# 		self.image = pygame.transform.scale(img, (60, 60))
# 		self.rect = self.image.get_rect()
# 		self.rect.x = x
# 		self.rect.y = y
                


class Platform:
    def __init__(self, _x=0, _y=0, image_path="platform.png"):
        super().__init__()
        self.x = _x
        self.y = _y
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Lever(pygame.sprite.Sprite):
    def __init__(self, x, y, up_blocks):
        super().__init__() 
        self.image_off = pygame.image.load("rychag_off.png")
        self.image_off = pygame.transform.scale(self.image_off, (40, 40))
        self.image_on = pygame.image.load("rychag_on.png")
        self.image_on = pygame.transform.scale(self.image_on, (40, 40))
        self.image = self.image_off
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.up_blocks = up_blocks
        # self.down_blocks = down_blocks
        self.is_on = False

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.colliderect(all_sprites.rect):
            self.is_on = True

        if self.is_on:
            self.image = self.image_on
            for block in self.up_blocks:
                block.rect.move_ip(0, -5)
            # for block in self.down_blocks:
            #     block.rect.move_ip(0, 5)
        else:
            self.image = self.image_off

    def draw(self, surface):
        surface.blit(self.image, self.rect)

                

def over_the_game(): # game over screen
    end = pygame.image.load('over.png')
    end = pygame.transform.scale(end, (1200, 700))
    screen.blit(end, (0 , 0))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()





prepatsv = [Block(x, y) for x in range(25, 500, 40) for y in range(510, 550, 40)]
pr = [Block(x, y) for x in range(610, 790, 40) for y in range(410, 450, 40)]
p3 = [Block(x, y) for x in range(0, 440, 40) for y in range(210, 250, 40)]
p2 = [Block(x, y) for x in range(600, 640, 40) for y in range(560, 600, 40)]
blup = [Block(x, y) for x in range(900, 980, 40) for y in range(330, 370, 40)]
pol = [Block(x, y) for x in range(0, width, 40) for y in range(height-50, height, 40)]
blocks=[]
blocks.extend(prepatsv)
blocks.extend(pol)
blocks.extend(pr)
blocks.extend(p2)
blocks.extend(blup)
blocks.extend(p3)


up_blocks=[]
platfff = [Platform(x, y) for x in range(430, 480, 50) for y in range(460, 470, 50)]
up_blocks.extend(platfff)
blocks.extend(platfff)

rychag = Lever(950, 310, up_blocks)

fire_sprite = Fire(width, height, blocks)
water_sprite = Water(width, height, blocks)
all_sprites = pygame.sprite.Group()
all_sprites.add(fire_sprite)
all_sprites.add(water_sprite)


liquid = Lava(145, 465)
lq2 = Lava(670, 360)
liquid_group = pygame.sprite.Group()
liquid_group.add(liquid)
liquid_group.add(lq2)



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


    for pl in up_blocks:
            pl.draw()

    fire_sprite.draw(screen)
    water_sprite.draw(screen)
    liquid_group.draw(screen)
    rychag.draw(screen)
    pygame.display.flip()
    if pygame.sprite.spritecollideany(fire_sprite, liquid_group):
        over_the_game()
    if pygame.sprite.spritecollideany(water_sprite, liquid_group):
        over_the_game()



pygame.quit()