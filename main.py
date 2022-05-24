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


def main():

    clock = pygame.time.Clock()

    # running variable indicates whether the game is running or the user wants to quit
    running = True
    dino_timer = 0
    obstacle_timer = 0
    speed = 0
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
        if dino_timer == dino_rate:
            dino_timer = 0
        else:
            dino_timer += 1

        # Display the dino
        if dino_timer < (dino_rate/2):
            dino = pygame.image.load(
                os.path.join("Assets", "Dino", "DinoRun2.png")
            )
        else:
            dino = pygame.image.load(
                os.path.join("Assets", "Dino", "DinoRun1.png")
            )
        WINDOW.blit(dino, (50, 300))

        # Display obstacles

        # Rate at which obstacles appear
        obs_rate = 100  # every 5 seconds
        if obstacle_timer == obs_rate:
            obstacle_timer = 0

            # Choosing a random obstacle
            obstacle_img = os.path.join("Assets", "Cactus")
            obstacle_img = os.path.join(
                obstacle_img, random.choice(os.listdir(obstacle_img)))

            obstacle = pygame.image.load(obstacle_img)

            # obs_flag makes sure that an obstacle is not displayed in the first obs_rate frames
            obs_flag = True
        else:
            obstacle_timer += 1

        if obs_flag:
            WINDOW.blit(obstacle, (WIDTH-3*speed, 300))

        # Update the game every frame
        pygame.display.update()
        if speed == WIDTH:
            speed = 0
        else:
            speed += 1

    pygame.quit()


# This line prevents the main() from being called from another program
if __name__ == "__main__":
    main()
