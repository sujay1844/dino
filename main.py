import pygame

#
WIDTH, HEIGHT = 800, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def main():

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
    
    pygame.quit()

if __name__ == "__main__":
    main()