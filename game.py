import pygame
import os
clock = pygame.time.Clock()
pygame.init()
base_dir = os.path.abspath(__file__)
asset_dir = os.path.join(os.path.dirname(__file__), "assets")
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
scr_width, scr_height = screen.get_size()
background = pygame.image.load( os.path.join(asset_dir, "background.png")).convert()
background = pygame.transform.scale(background,(scr_width,scr_height))
keys = pygame.key.get_pressed()
pygame.font.Font(None, 60)
mouse_x, mouse_y = pygame.mouse.get_pos()

class Player():
    def __init__(self):
        self.x = mouse_x
        self.y = mouse_y
        self.hitbox = pygame.rect.Rect(self.x, self.y, pygame.mouse.get_cursor().size)
        
    def update(self):
        
        
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False
    mouse_x, mouse_y = pygame.mouse.get_pos()

pygame.quit()
        
