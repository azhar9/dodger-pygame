import pygame
import random


#initializing pygame
pygame.init()

#initializing mixer and loading sound
pygame.mixer.init()
gun_sound = 'gun.mp3'
pygame.mixer.music.load(gun_sound)

#some game constants
displayWidth = 800
displayHeight = 500
gameTitle = "Dodger"

#rgb colors tuples
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#setting the screen width and height
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))

#setting the title
pygame.display.set_caption(gameTitle)

#my game clock
clock = pygame.time.Clock()

#getting the rocket image
rocketImage = pygame.image.load('rocket.png')

#getting the bullet image
bulletImage = pygame.image.load('bullet.png')

#function to display car at (x,y)
def rocket(x,y):
    #it loads the image ar x and y
    gameDisplay.blit(rocketImage,(x,y))
    return

#rocket x and y points
x = displayWidth/2
y = displayHeight - 90

#rocket x change
x_change = 0

#boolean to stop the game is rocket  is crashed
crashed = False

#game score
score = 0

tilex = random.randint(0,displayWidth)
tiley = -600
speed = 0.5

def playGunSound(play):
    if play:
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.stop()
    return

def bullet(rx,ry):
    global  tiley,tilex,speed,displayWidth,crashed,score
    #check if the bullet hit with rocket
    if(tilex >= rx and tilex <= rx+40 or tilex+30 >= rx and tilex+40 <= rx+40):
        if(tiley+40 >= ry):
            crashed = True

    gameDisplay.blit(bulletImage, (tilex,tiley))
    tiley+=speed
    speed = speed+0.005
    if(tiley > displayHeight - 50):
        tiley = 0
        tilex = random.randint(0,displayWidth)
        score+=5
        playGunSound(True)


def updateScore(score):
    myfont = pygame.font.SysFont('Comic Sans MS', 15)
    textsurface = myfont.render(str("Score: ")+str(score), False, white)
    gameDisplay.blit(textsurface, (0, 0))

def game_loop():
    global crashed,x,y,x_change,score

    while not crashed:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                     x_change = -5

                elif event.key == pygame.K_RIGHT:
                    x_change = +5

            #now nothing is pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        #now checking if the x_change is out of width or not
        tx = x
        tx+=x_change

        #chanding the rocket movement
        if(tx >0 and tx < displayWidth-40):
            x+=x_change

        #changing the bg color
        gameDisplay.fill(black)

        #now drawing rocket
        rocket(x,y)

        #now draw the bullet
        bullet(x,y)

        #update score
        updateScore(score)

        #updating the graphics on screen
        pygame.display.update()

        #setting the fps
        clock.tick(60)



def  reset():
    global x_change,crashed,tilex,tiley,speed,score
    x_change = 0
    crashed = False
    tilex = random.randint(0, displayWidth)
    tiley = -200
    speed = 0.5
    score = 0
    return


#starting the game
while True:
    game_loop()
    reset()

pygame.quit()
quit()









