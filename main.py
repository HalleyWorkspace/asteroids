import pygame
from constants import *
import player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0

    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()

    player.Player.containers=(updatable,drawable)
    
    player1=player.Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    

    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color='black')

        
        updatable.update(dt)
        for drawing in drawable:
            drawing.draw(screen)
        


        pygame.display.flip()
        dt=clock.tick(60)/1000


if __name__ == "__main__":
    main()
