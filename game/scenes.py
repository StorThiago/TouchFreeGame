import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def _draw_text(surface, text, size, color, center):
    """Helper to draw centered text on a surface."""
    font = pygame.font.SysFont(None, size)
    text_surf = font.render(text, True, color)
    rect = text_surf.get_rect(center=center)
    surface.blit(text_surf, rect)


class Bubble:
    """Simple bubble that can be popped by clicking."""

    def __init__(self):
        self.radius = random.randint(20, 60)
        self.x = random.randint(self.radius, SCREEN_WIDTH - self.radius)
        self.y = random.randint(self.radius, SCREEN_HEIGHT - self.radius)
        self.color = (
            random.randint(100, 255),
            random.randint(100, 255),
            random.randint(100, 255),
        )

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def is_clicked(self, pos):
        dx = pos[0] - self.x
        dy = pos[1] - self.y
        return dx * dx + dy * dy <= self.radius * self.radius


def main_scene():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TouchFreeGame")
    running = True
    clock = pygame.time.Clock()

    # Start screen setup
    start_button = pygame.Rect(0, 0, 200, 60)
    start_button.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
    show_start = True

    bubbles = []
    spawn_timer = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if show_start:
                    if start_button.collidepoint(event.pos):
                        show_start = False
                else:
                    for b in bubbles[:]:
                        if b.is_clicked(event.pos):
                            bubbles.remove(b)
                            break

        if show_start:
            screen.fill((30, 30, 30))
            _draw_text(screen, "TouchFreeGame", 48, (255, 255, 255), (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
            _draw_text(screen, "Logo Escola", 24, (200, 200, 200), (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT - 60))
            _draw_text(screen, "Logo ISCTE", 24, (200, 200, 200), (SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT - 60))
            _draw_text(
                screen,
                "https://github.com/seu-usuario/TouchFreeGame",
                20,
                (100, 100, 255),
                (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30),
            )
            pygame.draw.rect(screen, (70, 70, 200), start_button)
            _draw_text(screen, "Iniciar", 32, (255, 255, 255), start_button.center)
        else:
            screen.fill((50, 50, 80))
            spawn_timer += 1
            if spawn_timer > 60:
                bubbles.append(Bubble())
                spawn_timer = 0
            for b in bubbles:
                b.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
