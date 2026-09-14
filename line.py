import pygame

pygame.init()

disp_size = (800,800)

ox = disp_size[0]//2
oy = disp_size[1]-1

pygame.draw.line(pygame.display.set_mode((800, 800)),(255,0,0), (50,50), (500,500), 10)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse clicked at {event.pos}")
pygame.quit()