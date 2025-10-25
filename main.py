import pygame

#initalize pygame
pygame.init()

#create screen and title
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snoopy Game")

#game loop, keeps window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
