#game setup----------------------------------------------------------------------------------------
import pygame
import random

#initalize pygame
pygame.init()

#create screen, title, and background    (width, height)
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snoopy Game")

#load player (Snoopy)
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
        "y": random.randint(0,520)
    })

#sets up scoring and score label font
score = 0
font = pygame.font.Font (None, 40)

#instruction screen--------------------------------------------------------------------------------
running = True
show_instructions = True

while show_instructions:
    for event in pygame.event.get():
        #lets you close window normally
        if event.type == pygame.QUIT:
            show_instructions = False
            running = False
        #if space is pressed, start game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                show_instructions = False
    
    screen.fill("#000000")

    #text set up
    font_large = pygame.font.Font(None, 55)
    font_small = pygame.font.Font(None, 35)

    instructions = [
        "Use the arrow keys to move Snoopy",
        "Move Snoopy's head over candy to collect it and score points",
        "Collect as many as you can in 15 seconds!",
        "Good luck! Press SPACE to start!"
    ]

    #print title (centered)
    title_surface = font_large.render("Snoopy Halloween Candy Hunt Game", True, "#FF8543" )
    title_rect = title_surface.get_rect(center=(400, 85))
    screen.blit(title_surface, title_rect)
    
    #print instructions (centered)
    y=270
    for i in instructions:
        instruction_surface = font_small.render(i, True, "#FFC297")
        instructions_rect = instruction_surface.get_rect(center=(400,y))
        screen.blit(instruction_surface, instructions_rect)
        y+=50

    pygame.display.update()

#get current time in milliseconds
start_time = pygame.time.get_ticks()

#main game loop------------------------------------------------------------------------------------
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
            candy["x"] = random.randint(0,750)
            candy["y"] = random.randint(0,520)
            score+=1

    #background
    screen.fill("#87CEEB")

    #score label
    score_text = font.render(f"Score: {score}", True, "#FBF9F9")

    #calculate remaining time
    seconds_passed = (pygame.time.get_ticks()- start_time) / 1000 #converts to secs
    time_left = max(0, 15-int(seconds_passed))

    time_text = font.render(f"Time remaining: {time_left}", True, "#FF8A3C")
    time_rect = time_text.get_rect(center=(400, 30))
    screen.blit(time_text, time_rect)

    #insert candies, player, and score
    for candy in candies:
        screen.blit(candy["image"], (candy["x"], candy["y"]))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(score_text, (10,10))

    #update player position
    player_x += player_x_change
    player_y += player_y_change

    pygame.display.update()
