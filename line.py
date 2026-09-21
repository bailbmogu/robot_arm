import pygame
import math

pygame.init()

disp_size = (800, 800) 
ox = disp_size[0] // 2
oy = disp_size[1] - 1
arm_length = 150
current_angle = -math.pi / 2
screen = pygame.display.set_mode(disp_size)

def draw_arm(angle_rad):
    end_x = ox + arm_length * math.cos(angle_rad)
    end_y = oy + arm_length * math.sin(angle_rad)
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 0, 0), (ox, oy), (end_x, end_y), 10)
    pygame.display.flip()

draw_arm(current_angle)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = event.pos
            print(f"Mouse clicked at {mousepos}")

            dx = mousepos[0] - ox
            dy = mousepos[1] - oy
            current_angle = math.atan2(dy, dx)
            angle_deg = math.degrees(current_angle)
            print(f"Angle: {angle_deg} degrees")

            draw_arm(current_angle)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                arm_length += 10
                draw_arm(current_angle)
            if event.key == pygame.K_DOWN:
                arm_length = max(10, arm_length - 10)
                draw_arm(current_angle)

pygame.quit()