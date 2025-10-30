'''
To add:
-More decoration and design to end screen
-More decoration to welcome screen
'''
#game setup----------------------------------------------------------------------------------------
import pygame
import random

#initalize pygame
pygame.init()

#create screen, title, and background    (width, height)
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snoopy Candy Hunt Game")

#load player (Snoopy)
player_image = pygame.image.load("snoopy_pumpkin.png")
player_image = pygame.transform.smoothscale(player_image, (95,130))
player_x = 350
player_y = 480

#load candies
candy_images = [
    pygame.image.load("candy_pumpkin.png"),
    pygame.image.load("candycorn.png"),
    pygame.image.load("lollipop.png")
]

#resizes them all to be the same size
for i in range(len(candy_images)):
    candy_images[i] = pygame.transform.scale(candy_images[i],(55,55))

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
high_score = 0
font = pygame.font.Font (None, 40)

#instruction screen and end page decorations (loades them in)
broom_snoopy = pygame.image.load("snoopy_on_broom.png")
broom_snoopy = pygame.transform.smoothscale(broom_snoopy, (400,400))

pumpkin_ghost = pygame.image.load("pumpkin_ghost.png")
pumpkin_ghost = pygame.transform.smoothscale(pumpkin_ghost, (700,200))


#game active loop----------------------------------------------------------------------------------------------------------------
game_active = True
while game_active:

    #instruction screen----------------------------------------------------------------------------
    running = True
    show_instructions = True
    show_endscreen = False

    while show_instructions:
        for event in pygame.event.get():
            #lets you close window normally
            if event.type == pygame.QUIT:
                show_instructions = False
                running = False
                game_active = False
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
            "Touch candy with Snoopy's head to collect it and earn points",
            "Grab as much candy as you can in 15 seconds!",
            "",
            "Good luck! Press SPACE to start!"
        ]

        #print title (centered)
        title_surface = font_large.render("Snoopy Halloween Candy Hunt Game", True, "#FF8543" )
        title_rect = title_surface.get_rect(center=(400, 85))
        screen.blit(title_surface, title_rect)
        
        #print instructions (centered)
        y=190
        for i in instructions:
            instruction_surface = font_small.render(i, True, "#FFC297")
            instructions_rect = instruction_surface.get_rect(center=(400,y))
            screen.blit(instruction_surface, instructions_rect)
            y+=50

        #add image of snoopy on broom
        broom_rect = broom_snoopy.get_rect(center=(115, 490))
        screen.blit(broom_snoopy, broom_rect)

        pygame.display.update()

    #get current time in milliseconds
    start_time = pygame.time.get_ticks()

    #main game-------------------------------------------------------------------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_active = False

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
        score_text = font.render(f"Score: {score}", True, "#D97431")

        #calculate remaining time
        seconds_passed = (pygame.time.get_ticks()- start_time) / 1000 #converts to secs
        time_left = max(0, 15-int(seconds_passed))

        #display remaining time
        time_text = font.render(f"Time remaining: {time_left}", True, "#D97431")
        time_rect = time_text.get_rect(center=(400, 30))
        screen.blit(time_text, time_rect)
        if time_left == 0:
            running = False
            show_endscreen = True

        #display high score
        high_score_text = font_small.render(f"High Score: {high_score}", True, "#D97431")
        screen.blit(high_score_text, high_score_text.get_rect(center=(90, 580)))

        #insert candies, player, and score
        for candy in candies:
            screen.blit(candy["image"], (candy["x"], candy["y"]))
        screen.blit(player_image, (player_x, player_y))
        screen.blit(score_text, (10,10))
       
        pygame.display.update()

    #end screen------------------------------------------------------------------------------------
    while show_endscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show_endscreen = False 
                game_active = False
            elif event.type == pygame.KEYDOWN:
                #restart the game
                if event.key == pygame.K_SPACE:
                    score = 0
                    player_x, player_y = 350, 480
                    start_time = pygame.time.get_ticks()
                    show_endscreen = False
        
        screen.fill("#FFAE75")

        #high score
        if score > high_score:
            high_score = score

        #print text (centered)
        game_over_text = font_large.render("Time's Up! Great Job :)", True, "#000000" )
        score_text = font_small.render(f"Final Score: {score}", True, "#000000" )
        high_score_text2 = font_small.render(f"High Score: {high_score}", True, "#000000")
        play_again_text = font_small.render(f"Want to beat your high score? Press SPACE to play again!", True, "#000000")
        
        screen.blit(game_over_text, game_over_text.get_rect(center=(400, 180)))
        screen.blit(score_text, score_text.get_rect(center=(400,270)))
        screen.blit(high_score_text2, high_score_text2.get_rect(center=(400,420)))
        screen.blit(play_again_text, play_again_text.get_rect(center=(400,500)))

        #end screen decorations
        pumpkin_rect = pumpkin_ghost.get_rect(center=(400, 40))
        screen.blit(pumpkin_ghost, pumpkin_rect)

        pygame.display.update()