import pygame
import random
import os

# Window properties
WIDTH, HEIGHT = 1200, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chrome Dino")
FPS = 60

# Colours
WHITE = (255, 255, 255)

# Dino
# class Dino():
    # def __init__(self, counter):
        # n = counter
        # if n % 5 == 0 & n % 2 == 0:
            # self.img = pygame.image.load(
                # os.path.join("Assests", "Dino", "DinoRun1.png"))
        # elif n % 5 == 0 & n % 2 != 0: 
            # self.img = pygame.image.load(
                # os.path.join("Assests", "Dino", "DinoRun2.png"))
        # if n % 2 == 0:
            # self.img = pygame.image.load(
                # os.path.join("Assets", "Dino", "DinoRun2.png"))
        # else:
            # self.img = pygame.image.load(
                # os.path.join("Assets", "Dino", "DinoRun1.png"))

def main():
    
    clock = pygame.time.Clock()

    # running variable indicates whether the game is running or the user wants to quit
    running = True
    i = 0
    j = 0
    fps = 0
    obs_flag = False

    while running:
        clock.tick(FPS)

        # Exiting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Filling the background with a colour
        WINDOW.fill(WHITE)

        # Rate at which the Dino animates
        dino_rate = 14
        if i == dino_rate:
            i = 0
        else:
            i+=1
        
        # Display the dino
        if i < (dino_rate/2):
            dino = pygame.image.load(
                os.path.join("Assets", "Dino", "DinoRun2.png")
                )
        else:
            dino = pygame.image.load(
                os.path.join("Assets", "Dino", "DinoRun1.png")
                )
        # dino = Dino(i)
        WINDOW.blit(dino, (50, 300))

        # Display obstacles
        # obstacle_img = os.path.join("Assets", "Cactus", "SmallCactus1.png")
        # obstacle_img = os.path.join(obstacle_img, random.choice(os.listdir(obstacle_img)))

        # obstacle = pygame.image.load(obstacle_img)

        # Rate at which obstacles appear
        obs_rate = 100 # every 5 seconds
        if j == obs_rate:
            j = 0

            # Choosing a random obstacle
            obstacle_img = os.path.join("Assets", "Cactus")
            obstacle_img = os.path.join(obstacle_img, random.choice(os.listdir(obstacle_img)))

            obstacle = pygame.image.load(obstacle_img)
            # obs_flag = False
            obs_flag = True
        else:
            j+=1

        if obs_flag:
            WINDOW.blit(obstacle, (WIDTH-3*fps, 300))
        # WINDOW.blit(obstacle, (500, 300))
    
        # Update the game every frame
        pygame.display.update()
        if fps == WIDTH:
            fps = 0
        else:
            fps+=1
        
        
    pygame.quit()

# This line prevents the main() from being called from another program
if __name__ == "__main__":
    main()
