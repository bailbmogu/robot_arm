import pygame
import math

pygame.init()

disp_size = (800, 800) 
ox = disp_size[0] // 2
oy = disp_size[1] - 1
arm_length = 150

a1 = math.pi / 2
clicked_pos = (0, 0)

has_clicked = False
screen = pygame.display.set_mode(disp_size)
font = pygame.font.SysFont(None, 32)

def draw_arm(a1_rad):
    end_x = ox - arm_length * math.cos(a1_rad)
    end_y = oy - arm_length * math.sin(a1_rad)
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 0, 0), (ox, oy), (end_x, end_y), 10)
    if has_clicked:
        pygame.draw.line(screen, (0, 255, 0), (clicked_pos[0] - 10, clicked_pos[1] - 10), (clicked_pos[0] + 10, clicked_pos[1] + 10), 3)
        pygame.draw.line(screen, (0, 255, 0), (clicked_pos[0] - 10, clicked_pos[1] + 10), (clicked_pos[0] + 10, clicked_pos[1] - 10), 3)
    a1_deg = math.degrees(a1_rad)
    lines = [
        f"jayren",
        f"a1: {a1_deg:.0f}",
        f"clicked x,y = {clicked_pos[0]}, {clicked_pos[1]}",
        f"arm x,y = {end_x:.0f}, {end_y:.0f}",
        f"arm length: {arm_length}"
    ]
    for i, line in enumerate(lines):
        text = font.render(line, True, (0, 255, 0))
        screen.blit(text, (20, 20 + i * 35))
    pygame.display.flip()

draw_arm(a1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = event.pos
            print(f"Mouse clicked at {mousepos}")
            clicked_pos = mousepos
            has_clicked = True

            dx = mousepos[0] - ox
            dy = mousepos[1] - oy
            a1 = math.atan2(-dy, -dx)
            a1_deg = math.degrees(a1)
            print(f"a1: {a1_deg} degrees")

            draw_arm(a1)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                arm_length += 10
                draw_arm(a1)
            if event.key == pygame.K_DOWN:
                arm_length = max(10, arm_length - 10)
                draw_arm(a1)

pygame.quit()