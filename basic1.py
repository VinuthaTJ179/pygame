import pygame

#After importing pygame, it has to be initialized
pygame.init()

#To create a window we need width and height
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

player = pygame.Rect((300,250,50,50))

#Game loop
run = True
while run == True:

    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),player)
    #Actions performed based on key pressed(Event handlers)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)

    #Event handling to avoid freezing of the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()

    