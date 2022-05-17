import pygame

# Window properties
WIDTH, HEIGHT = 800, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game-lol")
FPS = 60

# Colours
WHITE = (255, 255, 255)

def main():
    
    clock = pygame.time.Clock()

    # running variable indicates whether the game is running or the user wants to quit
    running = True
    while running:
        clock.tick(FPS)

        # Exiting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Filling the background with a colour
        WINDOW.fill(WHITE)
        
        # Update the game every frame
        pygame.display.update()

    
    pygame.quit()

# This line prevents the main() from being called from another program
if __name__ == "__main__":
    main()