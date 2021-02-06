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
target_Img = pygame.image.load('target.png')

def men(x):
    gameDisplay.blit(menImg, (x,y))
def target(x,y):
    gameDisplay.blit(target_Img, (x,y))

x =  (display_width * 0.5)
y = (display_height * 0.5)
x_target =(display_width * 0.45)
y_target =(display_height * 0.4)
x_change = 0
men_speed = 0
gameDisplay.fill(white)

def target (x,y):
    gameDisplay.blit(x,y)

counter=0
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -5
            elif event.key == pygame.K_d:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_change = 0
        if event.type == pygame.SPACE:
            spawn()  

    x += x_change
    men(x)
    target()
    pygame.display.update()
    clock.tick(60)
    counter+=1/60

pygame.quit()
quit()