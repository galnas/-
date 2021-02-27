import pygame
import random

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
target_Img = pygame.image.load('target.png')

def men(x):
    gameDisplay.blit(menImg, (x,y))
def target(x1,y2):
    gameDisplay.blit(target_Img, (x1,y1))

x =  (display_width * 0.5)
y = (display_height * 0.5)

x1 = (display_width * 0.9)
y1= (display_height * 0.1)
x_change = 0
x1_change = 0
y1_change = 0
men_speed = 0
target_speed = 0
spawn = x1 = random.randint(0,1300)
       

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_SPACE:
                spawn = True

            if event.key == pygame.K_a:
                x_change = -5
            elif event.key == pygame.K_d:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_change = 0

        
    if spawn == True:
         
        x1 = random.randint(0,1300)
        y1 = random.randint(0,100)
        spawn = False

    x += x_change
    gameDisplay.fill(white)
    men(x)
    target (x1,y1)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()