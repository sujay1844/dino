import pygame
import os

# Window properties
WIDTH, HEIGHT = 1500, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game-lol")
FPS = 60

# Colours
WHITE = (255, 255, 255)

# Dino
class Dino:
    def __init__(self, counter):
        n = self.counter
        if n % 5 == 0 & n % 2 == 0:
            self.img = pygame.image.load(
                os.path.join("Assests", "Dino", "DinoRun1.png"))
        elif n % 5 == 0 & n % 2 != 0: 
            self.img = pygame.image.load(
                os.path.join("Assests", "Dino", "DinoRun2.png"))
        else:
            self.img = pygame.image.load(
                os.path.join("Assests", "Dino", "DinoRun1.png"))

def main():
    
    clock = pygame.time.Clock()

    # running variable indicates whether the game is running or the user wants to quit
    running = True
    i = 0
    while running:
        clock.tick(FPS)

        # Exiting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Filling the background with a colour
        WINDOW.fill(WHITE)
        
        # Display the dino
        WINDOW.blit(Dino(i), (50, 300))
    
        # Update the game every frame
        pygame.display.update()
        
        if i == 60:
            i = 0
        else:
            i+=1
        
    pygame.quit()

# This line prevents the main() from being called from another program
if __name__ == "__main__":
    main()