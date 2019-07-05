# TO DO : Remplacer le rectangle par une image de Riem
# Créer les bruitages ainsi que les events qui les fera trigger
# Corriger la variable path pour qu'elle s'adapte à toutes les machines

import os
import time
import pygame
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
path = os.path.dirname(os.path.realpath(__file__))
screenWidth = 1000
screenHeight = 600
win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Les aventures de Riem")

class Personnage:
    x = 300
    y = 300
    width = 50
    height = 50
    velocity = 10
    isJump = False
    jumpCount = 10
    color = (255,255,255)

run = True

personnage1 = Personnage()
personnage1.velocity = 20
personnage1.x = 0
personnage1.y = 0
personnage1.color = (255,0,0)
personnage2 = Personnage()
personnage2.color = (0,255,0)

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and personnage1.x > personnage1.velocity:
        personnage1.x -= personnage1.velocity

    if keys[pygame.K_RIGHT] and personnage1.x < screenWidth - personnage1.width - personnage1.velocity:
        personnage1.x += personnage1.velocity

    if keys[pygame.K_UP] and personnage1.y > personnage1.velocity:
        personnage1.y -= personnage1.velocity

    if keys[pygame.K_DOWN] and personnage1.y < screenHeight - personnage1.height - personnage1.velocity:
        personnage1.y += personnage1.velocity

    if keys[pygame.K_a] and personnage2.x > personnage2.velocity:
        personnage2.x -= personnage2.velocity

    if keys[pygame.K_d] and personnage2.x < screenWidth - personnage2.width - personnage2.velocity:
        personnage2.x += personnage2.velocity

    if keys[pygame.K_w] and personnage2.y > personnage2.velocity:
        personnage2.y -= personnage2.velocity

    if keys[pygame.K_s] and personnage2.y < screenHeight - personnage2.height - personnage2.velocity:
        personnage2.y += personnage2.velocity

    if abs((personnage1.x+25) - (personnage2.x+25)) < 50 and abs((personnage1.y+25) - (personnage2.y+25)) < 50:
        personnage1.color = (0,0,0)
        personnage1.x = 9999
        personnage1.y = 9999
        pygame.mixer.music.load(path + "/Son/game_over.OGG")
        pygame.mixer.music.play()

    win.fill((0))
    pygame.draw.rect(win, personnage1.color, (personnage1.x, personnage1.y, personnage1.width, personnage1.height))
    pygame.draw.rect(win, personnage2.color, (personnage2.x, personnage2.y, personnage2.width, personnage2.height))
    pygame.display.update()

pygame.quit()