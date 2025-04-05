import pygame

pygame.init()
#экран
screen=pygame.display.set_mode((800,600))
x,y=400,300
step = 20
red = (255, 0, 0)
radius=25
running=True
while running:
    #управление
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and x - radius - step >=0:
                x-=step
            if event.key==pygame.K_RIGHT and x+radius+step<=800:
                x+=step
            if event.key==pygame.K_DOWN and y+radius+step<=600:
                y+=step
            if event.key==pygame.K_UP and y-radius-step>=0:
                y-=step
    screen.fill((255,255,255))


    pygame.draw.circle(screen, red, (x,y), radius)
    pygame.display.flip()
pygame.quit()

