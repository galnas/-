import pygame

pygame.init()

display_width = 1300
display_height = 700

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

white = (255,255,255)
black = (0,0,0)

clock = pygame.time.Clock()
crashed = False
menImg = pygame.image.load('men.png')

def men(x,y):
    gameDisplay.blit(menImg, (x,y))

x =  (display_width * 0.5)
y = (display_height * 0.5)
x_change = 0
car_speed = 0

while not crashed:
    men(x,y)
    pygame.display.update()
    clock.tick(60)
    x += x_change
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

gameDisplay.fill(white)



pygame.quit()
quit()