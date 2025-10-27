#game setup----------------------------------------------------------------------------------------
import pygame
import random

#initalize pygame
pygame.init()

#create screen, title, and background    (width, height)
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snoopy Game")

#load player
player_image = pygame.image.load("snoopy_pumpkin.png")
player_image = pygame.transform.smoothscale(player_image, (95,130))
player_x = 350
player_y = 480

#player movement variables
player_x_change = 0
player_y_change = 0

#load candies
candy_images = [
    pygame.image.load("candy_pumpkin.png"),
    pygame.image.load("candycorn.png"),
    pygame.image.load("lollipop.png")
]
#resizes them all to be the same size
for i in range(len(candy_images)):
    candy_images[i] = pygame.transform.scale(candy_images[i],(50,50))

#chooses random coordinates and candy
candies = []
for candy_img in candy_images:
    candies.append({
        "image": candy_img,
        "x": random.randint(0,750),
        "y": random.randint(0,550)
    })

#sets up scoring
score = 0
font = pygame.font.Font (None, 40)

#score label
score_text = font.render(f"Score: {score}", True, "#FBF9F9")

#main game loop, also keeps window open --------------------------------------------------------
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

    #keep player inside window bounds
    if player_x < -20:
        player_x = -20
    elif player_x > 720:
        player_x = 720
    if player_y < -20:
        player_y = -20
    elif player_y > 490:
        player_y = 490

    #check for candy collisions 
    for candy in candies:
        if abs(player_x - candy["x"]) < 50 and abs(player_y - candy["y"]) < 50:
            score+=1
            candy["x"] = random.randint(0,750)
            candy["y"] = random.randint(0,550)

    #background
    screen.fill("#87CEEB")

    #insert candies and player
    for candy in candies:
        screen.blit(candy["image"], (candy["x"], candy["y"]))
    
    screen.blit(player_image, (player_x, player_y))

    #update player position
    player_x += player_x_change
    player_y += player_y_change

    pygame.display.update()