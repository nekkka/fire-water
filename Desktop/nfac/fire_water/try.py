import pygame
import os
import random

# Set the working directory to the folder containing the game files
os.chdir('C:/Users/ASUS/Desktop/nfac/fire_water')

# Initialize pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

# Set the game window caption
pygame.display.set_caption("Fire and Water")

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Fire(pygame.sprite.Sprite):
    def __init__(self, blocks):
        super().__init__()
        # Load the image for the sprite
        self.image = pygame.image.load("fire.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 80))
        # Set the initial position of the sprite
        self.rect = self.image.get_rect()
        self.rect.center = (50, 620)
        # Set some physics properties for the sprite
        self.jump_height = 10
        self.jump_velocity = 0
        self.gravity = 0.5
        self.is_jumping = False
        # Store a reference to the blocks in the level
        self.blocks = blocks
 
    def update(self):
        # Check which keys are being pressed
        pressed_keys = pygame.key.get_pressed()

        # Update the position of the sprite based on its current state
        if self.is_jumping:
            self.rect.move_ip(0, -self.jump_velocity)
            self.jump_velocity -= self.gravity
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.is_jumping = False
                self.jump_velocity = 0
        else:
            if self.rect.left > 30:
                if pressed_keys[pygame.K_LEFT]:
                    self.rect.move_ip(-5, 0)
            if self.rect.right < SCREEN_WIDTH - 30:        
                if pressed_keys[pygame.K_RIGHT]:
                    self.rect.move_ip(5, 0)
            if self.rect.top > 0:
                if pressed_keys[pygame.K_UP] and not self.is_jumping:
                    self.is_jumping = True
                    self.jump_velocity = self.jump_height

        # Check for collisions with blocks in the level
        for block in self.blocks:
            if self.rect.colliderect(block.rect):
                if self.rect.bottom <= block.rect.top + 10:
                    # Landed on the block
                    self.rect.bottom = block.rect.top
                    self.is_jumping = False
                    self.jump_velocity = 0
                    break
                elif self.rect.top >= block.rect.bottom - 10:
                    # Hit the block from above
                    self.rect.top = block.rect.bottom
                    self.jump_velocity = 0
                    break

    def draw(self, surface):
        # Draw the sprite on the given surface
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

blocks = [Block(x, y) for x in range(25, 500, 50) for y in range(500, 550, 50)]
# Create the sprites and blocks
fire_sprite = Fire(50, 50)
water_sprite = Water(50, 50)


# Start the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    oblozhka = pygame.image.load('bg.png')
    oblozhka = pygame.transform.scale(oblozhka, (1200, 700))
    screen.blit(oblozhka, (0 , 0))

    # Update and draw the sprites and blocks
    fire_sprite.update()
    water_sprite.update()
    for block in blocks:
            block.draw()

    fire_sprite.draw(screen)
    water_sprite.draw(screen)
    pygame.display.flip()

# Quit the game
pygame.quit()