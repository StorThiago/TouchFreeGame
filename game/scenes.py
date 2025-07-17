import pygame


def main_scene():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("TouchFreeGame")
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((30, 30, 30))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
