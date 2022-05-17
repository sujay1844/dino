import pygame

# Window properties
WIDTH, HEIGHT = 800, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game-lol")

def main():
    # running variable indicates whether the game is running or the user wants to quit
    running = True
    while running:
        # Exiting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()

# This line prevents the main() from being called from another program
if __name__ == "__main__":
    main()