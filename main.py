import pygame

#initalize pygame
pygame.init()

#create screen, title, and background    (width, height)
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snoopy Game")

#player, snoopy
player_image = pygame.image.load("snoopy_pumpkin.png")
player_image = pygame.transform.smoothscale(player_image, (95,130))
player_x = 350
player_y = 480

#player movement variables
player_x_change = 0
player_y_change = 0

#game loop, also keeps window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #check which keys have been pressed
    keys = pygame.key.get_pressed()

    #arrow key movement functionality when pressed
    #horizontal movement
    if keys[pygame.K_LEFT]:
        player_x-=3
    if keys[pygame.K_RIGHT]:
        player_x+=3
        
    #vertical movement
    if keys[pygame.K_UP]:
        player_y-=3
    if keys[pygame.K_DOWN]:
        player_y+=3

    #update player position
    player_x += player_x_change
    player_y += player_y_change

    #keep player inside window bounds
    if player_x < -20:
        player_x = -20
    elif player_x > 720:
        player_x = 720
    if player_y < -20:
        player_y = -20
    elif player_y > 490:
        player_y = 490

    screen.blit(player_image, (player_x, player_y))
    pygame.display.update()
    
    screen.fill("#87CEEB")