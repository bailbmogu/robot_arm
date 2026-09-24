import pygame
import math

pygame.init()

disp_size = (800, 800) 
ox = disp_size[0] // 2
oy = disp_size[1] - 1
clicked_pos = (0, 0)
screen = pygame.display.set_mode(disp_size)
font = pygame.font.SysFont(None, 32)
clock = pygame.time.Clock()

state = 0
timer = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and state == 0:
            mousepos = event.pos
            print(f"Mouse clicked at {mousepos}")
            clicked_pos = mousepos

            state = 1
            timer = 0
    screen.fill((0, 0, 0))

    if state == 1:
        for i in range(10):

            start = i * 4
            if start <= timer < start + 20:
                t = i / 9
                x = ox + (clicked_pos[0] - ox) * t
                y = oy + (clicked_pos[1] - oy) * t


                pygame.draw.rect(screen, (255, 255, 0), (x - 10, y - 10, 20, 20))
        if timer > 9 * 4 + 20:
            state = 2
            timer = 0

    elif state == 2:
        r = int(5 * 10 * timer / 60)
        if r > 0:


            pygame.draw.circle(screen, (0, 200, 255), clicked_pos, r, 3)
        if timer >= 60:
            state = 3

            timer = 0
    elif state == 3:

        r = int(50 - 4 * 10 * timer / 48)
        if r > 0:
            
            pygame.draw.circle(screen, (255, 100, 255), clicked_pos, r, 3)

        if timer >= 48:


            state = 0
            timer = 0
    timer += 1


    lines = [
        f"jayren",
        f"state: {state}",
        f"clicked x,y = {clicked_pos[0]}, {clicked_pos[1]}"
    ]
    for i, line in enumerate(lines):
        text = font.render(line, True, (0, 255, 0))
        screen.blit(text, (20, 20 + i * 35))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()