import pygame

#initalize pygame
pygame.init()

#create screen, title, and background    (width, height)
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snoopy Game")

#player, snoopy
player_image = pygame.image.load("snoopy_pumpkin.png")
player_image = pygame.transform.smoothscale(player_image, (100,120))
player_x = 350
player_y = 480

#game loop, keeps window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(player_image, (player_x, player_y))
    pygame.display.update()
    
    screen.fill("#87CEEB")
