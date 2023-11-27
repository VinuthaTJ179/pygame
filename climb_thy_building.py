import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set the dimensions of your screen
screen_width = 1920
screen_height = 1080

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Text and Image Animation")

# Load the image
splash_image = pygame.image.load("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\cityskyline.png")
second_screen_image = pygame.image.load("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\sunnyday.png")
# Set the initial position of the image
x, y = 0, 0

# Define a font and initial text
font = pygame.font.Font("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\pixelmix.ttf", 60)  # None uses the default system font
text_color = (255, 255, 255)  # White, in (R, G, B) format
text = "Hello, Pygame!"
text_surface = font.render('', True, text_color)

# Calculate the position to place the text at the center of the screen
text_x = 610
text_y = 500

#*********************************************************************************
SPLASH_SCREEN = 0
SECOND_SCREEN = 1
current_state = SPLASH_SCREEN

# Timer to control the splash screen duration
transition_duration = 7000  # Duration of the transition in milliseconds (7 seconds)
start_time = pygame.time.get_ticks()
alpha = 255  # Initial alpha value for fading (fully opaque)
fade_speed = 2  

#*********************************************************************************



# Initialize variables for the animation
animation_text = "Climb thy building"
animation_speed = 5  # Number of letters displayed per second
current_letter_index = 0
time_last_letter_displayed = time.time()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    if current_state == SPLASH_SCREEN:
        # Clear the screen
        screen.fill((0, 0, 0))  # Black background
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= transition_duration:
            current_state = SECOND_SCREEN
        # Blit (draw) the image onto the screen
        screen.blit(splash_image, (x, y))

        # Calculate the time since the last letter was displayed
        time_now = time.time()
        time_since_last_display = time_now - time_last_letter_displayed

        # Display the letters one by one with the defined animation speed
        if current_letter_index < len(animation_text) and time_since_last_display >= 1 / animation_speed:
           text_surface = font.render(animation_text[:current_letter_index + 1], True, text_color)
           time_last_letter_displayed = time_now
           current_letter_index += 1

        # Blit (draw) the text surface at the center of the screen
        screen.blit(text_surface, (text_x, text_y))
    elif current_state == SECOND_SCREEN:
        # Clear the screen
        screen.fill((0, 0, 0))  # Black background

        # Blit (draw) the second screen image
        screen.blit(second_screen_image, (x, y))
    
        if alpha > 0:
            overlay = pygame.Surface((screen_width, screen_height))
            overlay.set_alpha(alpha)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            alpha = max(0, alpha - fade_speed)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
