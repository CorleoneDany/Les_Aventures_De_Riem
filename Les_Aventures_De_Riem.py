# TO DO : Remplacer le rectangle par une image de Riem
# Débuguer le saut (le saut ne fonctionne qu'une fois puis plus rien)
# Créer la classe des ennermis ainsi que la fonction pour les faire spawn
# Créer des animations de run et de jump
# Créer la fonction qui fera avancer le personnage vers la gauche (ou ennemis vers la droite)
# Créer la fonction de mort
# Créer la fonction de scoring
# Créer les bruitages ainsi que les events qui les fera trigger

import pygame
pygame.init()

screenWidth = 500
screenHeight = 500
win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Les aventures de Riem")

class personnage:
    x = 300
    y = 300
    width = 40
    height = 60
    velocity = 15
    isJump = False
    jumpCount = 10

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and personnage.x > personnage.velocity:
        personnage.x -= personnage.velocity

    if keys[pygame.K_RIGHT] and personnage.x < screenWidth - personnage.width - personnage.velocity:
        personnage.x += personnage.velocity

    if not(personnage.isJump):
        if keys[pygame.K_UP] and personnage.y > personnage.velocity:
            personnage.y -= personnage.velocity

        if keys[pygame.K_DOWN] and personnage.y < screenHeight - personnage.height - personnage.velocity:
            personnage.y += personnage.velocity

        if keys[pygame.K_SPACE]:
            personnage.isJump = True

    else:
        if personnage.jumpCount >= -10:
            neg = 1
            if personnage.jumpCount <0:
                neg = -1
            personnage.y -= (personnage.jumpCount ** 2) * 0.5 * neg
            personnage.jumpCount -= 1
        else:
            personnage.isJump = False
            jumpCount = 10

    win.fill((0))
    pygame.draw.rect(win, (255,0,255), (personnage.x, personnage.y, personnage.width, personnage.height))
    pygame.display.update()

pygame.quit()