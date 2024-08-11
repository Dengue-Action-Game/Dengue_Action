import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 1280
altura = 720

tela = pygame.display.set_mode((largura, altura))
titulo  = pygame.display.set_caption('Dengue Action')

bg = pygame.image.load("assets/BG.jpg")
player = pygame.image.load("assets/bola.png")

def desenhar():
    tela.blit(bg, (0,0))
    tela.blit(player, (0,670))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()