import random
import pygame
import cv2
import numpy as np

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def _draw_text(surface, text, size, color, center):
    """Helper to draw centered text on a surface."""
    font = pygame.font.SysFont(None, size)
    text_surf = font.render(text, True, color)
    rect = text_surf.get_rect(center=center)
    surface.blit(text_surf, rect)


# class Bubble:
#     """Simple bubble that can be popped by clicking."""

#     def __init__(self):
#         self.radius = random.randint(20, 60)
#         self.x = random.randint(self.radius, SCREEN_WIDTH - self.radius)
#         self.y = random.randint(self.radius, SCREEN_HEIGHT - self.radius)
#         self.color = random.choice([(255, 0, 0), (0, 0, 255)])  # Red or Blue

#     def draw(self, surface):
#         pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

#     def is_clicked(self, pos):
#         dx = pos[0] - self.x
#         dy = pos[1] - self.y
#         return dx * dx + dy * dy <= self.radius * self.radius


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
            screen.fill((0, 0, 0))
            _draw_text(screen, "TouchFreeGame", 48, (255, 255, 255), (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
            _draw_text(screen, "Logo Escola", 24, (200, 200, 200), (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT - 60))
            _draw_text(screen, "Logo ISCTE", 24, (200, 200, 200), (SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT - 60))
            _draw_text(
                screen,
                "github.com/StorThiago/TouchFreeGame",
                20,
                (200, 200, 200),
                (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30),
            )
            pygame.draw.rect(screen, (70, 70, 200), start_button)
            _draw_text(screen, "Iniciar", 32, (255, 255, 255), start_button.center)
        else:
            # screen.fill((255, 255, 255))
            # spawn_timer += 1
            # if spawn_timer > 60:
            #     bubbles.append(Bubble())
            #     spawn_timer = 0
            # for b in bubbles:
            #     b.draw(screen)


            # Dimensões da janela
            width, height = 800, 600

            # Intervalos HSV para cores dos objetos rastreados (ajuste consoante necessário)
            lower_color1 = np.array([0, 100, 100])     # Ex: objeto vermelho/rosa
            upper_color1 = np.array([10, 255, 255])
            lower_color2 = np.array([100, 100, 100])   # Ex: objeto azul
            upper_color2 = np.array([140, 255, 255])

            bubble_radius = 50
            num_bubbles = 7

            def generate_bubbles(n):
                return [
                    {
                        'center': (random.randint(bubble_radius, width - bubble_radius),
                                random.randint(bubble_radius, height - bubble_radius)),
                        'visible': True
                    } for _ in range(n)
                ]

            bubbles = generate_bubbles(num_bubbles)

            def check_collision(center, bubble_center, radius):
                dist = np.linalg.norm(np.array(center) - np.array(bubble_center))
                return dist < radius

            def draw_soap_bubble(frame, center, radius, hue='blue', alpha=0.55):
                # Overlay transparente
                overlay = frame.copy()

                # Gradiente e cor base
                if hue == 'blue':
                    base_color = (255, 160, 80)  # azul claro no padrão BGR
                elif hue == 'red':
                    base_color = (80, 140, 255)  # vermelho claro no padrão BGR
                else:
                    base_color = (255, 255, 255)

                # Desenha camadas concêntricas de fora para dentro (gradiente translúcido)
                for i in range(8, 0, -1):
                    r = int(radius * (i / 8.0))
                    # Intensifica a opacidade no centro, ficando mais translúcido nos extremos
                    a = alpha * (i / 8.0) * 0.8 + 0.18
                    # Gradiente de cor para branco no centro
                    circle_color = [
                        int(base_color[0] + (255-base_color[0])*(i/14.)),
                        int(base_color[1] + (255-base_color[1])*(i/14.)),
                        int(base_color[2] + (255-base_color[2])*(i/14.)),
                    ]
                    bubble_layer = overlay.copy()
                    cv2.circle(bubble_layer, center, r, circle_color, -1)
                    cv2.addWeighted(bubble_layer, a, overlay, 1 - a, 0, overlay)

                # Brilho simulado (mancha branca offset dentro da bolha)
                shine_center = (center[0] - int(radius*0.35), center[1] - int(radius*0.33))
                cv2.circle(overlay, shine_center, int(radius*0.23), (255,255,255), -1)
                cv2.addWeighted(overlay, 0.85, frame, 0.15, 0, frame)

            cap = cv2.VideoCapture(0)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                frame = cv2.resize(frame, (width, height))
                frame = cv2.flip(frame, 1)
                blurred = cv2.GaussianBlur(frame, (11, 11), 0)
                hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
                mask1 = cv2.inRange(hsv, lower_color1, upper_color1)
                mask2 = cv2.inRange(hsv, lower_color2, upper_color2)

                # Deteção dos objetos reais
                for idx, mask in enumerate([mask1, mask2]):
                    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    if contours:
                        largest_contour = max(contours, key=cv2.contourArea)
                        ((x, y), detected_radius) = cv2.minEnclosingCircle(largest_contour)
                        if detected_radius > 12:
                            # marcador diferente para cada mão
                            cor_marcador = (0,255,0) if idx == 0 else (255,0,0)
                            cv2.circle(frame, (int(x), int(y)), int(detected_radius), cor_marcador, 2)
                            for bubble in bubbles:
                                if bubble['visible'] and check_collision((int(x), int(y)), bubble['center'], bubble_radius):
                                    bubble['visible'] = False

                # Esferas com gradiente bola de sabão (azul/vermelha alternadamente)
                for idx, bubble in enumerate(bubbles):
                    if bubble['visible']:
                        hue = 'blue' if idx % 2 == 0 else 'red'
                        draw_soap_bubble(frame, bubble['center'], bubble_radius, hue=hue, alpha=0.58)

                cv2.imshow('TouchFreeGame', frame)
                if cv2.waitKey(1) & 0xFF == 27:
                    break

            cap.release()
            cv2.destroyAllWindows()






        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
