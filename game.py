import pygame
import time
import random
import os

pygame.init()

gray = (119, 118, 110)
black = (0, 0, 0)

green = (0, 200, 0)
bright_green = (0, 255, 0)

red = (250, 0, 0)
bright_red = (255, 0, 0)

blue = (0, 0, 200)
bright_blue = (0, 0, 255)

display_width = 800
display_height = 600

pause = False

gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("car game")

clock = pygame.time.Clock()

carimg = pygame.image.load('Images/car1.jpg')
yellow_strip = pygame.image.load('Images/yellow.jpg')
white_strip = pygame.image.load('Images/strip.jpg')
backgroundpic = pygame.image.load('Images/grass.jpg')

introduction = pygame.image.load('Images/background3.jpg')
intro_background = pygame.image.load('Images/background4.jpg')

car_width = 56


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gamedisplays, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "intro":
                introductions()
            elif action == "menu":
                intro_loop()
            elif action == "pause":
                paused()
    else:
        pygame.draw.rect(gamedisplays, ic, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = (int(x + (w / 2)), int(y + (h / 2)))
    gamedisplays.blit(textsurf, textrect)


#######today start from introduction function

def introductions():
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gamedisplays.blit(intro_background, (0, 0))
        largetext = pygame.font.Font("freesansbold.ttf", 80)
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        mediumtext = pygame.font.Font("freesansbold.ttf", 40)
        textSurf, textRect = text_objects("CAR GAME", smalltext)
        textRect.center = (300, 200)
        TextSurf, TextRect = text_objects("Intro", largetext)
        TextRect.center = (400, 100)
        gamedisplays.blit(textSurf, textRect)
        gamedisplays.blit(TextSurf, TextRect)
        stextSurf, stextRect = text_objects("Arrow Left : Left Turn", smalltext)
        stextRect.center = (150, 400)

        htextSurf, htextRect = text_objects("Arrow Right : Right Turn", smalltext)
        htextRect.center = (150, 450)

        atextSurf, atextRect = text_objects("A : Accelerator", smalltext)
        atextRect.center = (150, 500)

        rtextSurf, rtextRect = text_objects("P : Pause", smalltext)
        rtextRect.center = (150, 550)

        ptextSurf, ptextRect = text_objects("B : Brake", smalltext)
        ptextRect.center = (300, 350)

        ctextSurf, ctextRect = text_objects("Control Panal", mediumtext)
        ctextRect.center = (350, 300)

        gamedisplays.blit(stextSurf, stextRect)
        gamedisplays.blit(rtextSurf, rtextRect)
        gamedisplays.blit(ptextSurf, ptextRect)
        gamedisplays.blit(atextSurf, atextRect)
        gamedisplays.blit(htextSurf, htextRect)
        gamedisplays.blit(ctextSurf, ctextRect)
        button("Back", 600, 450, 100, 50, blue, bright_blue, "menu")
        pygame.display.update()
        clock.tick(30)


def paused():
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.blit(instruction_background,(0,0))
            largetext=pygame.font.Font("C:\Windows\Fonts\Times.ttf",115)
            TextSurf,TextRect=text_objects("PAUSED",largetext)
            TextRect.center=(int(display_width/2),int(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            button("CONTINUE",150,450,150,50,green,bright_green,"unpause")
            button("RESTART",350,450,150,50,blue,bright_blue,"play")
            button("MAIN MENU",550,450,200,50,red,bright_red,"menu")
            pygame.display.update()
            clock.tick(30)


def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gamedisplays.blit(intro_background, (0, 0))
        largetext = pygame.font.Font("freesansbold.ttf", 115)
        TextSurf, TextRect = text_objects("CAR GAME", largetext)
        TextRect.center = (400, 100)
        gamedisplays.blit(TextSurf, TextRect)
        button("START", 150, 520, 100, 50, green, bright_green, "play")
        button("QUIT", 550, 520, 100, 50, red, bright_red, "quit")
        button("INSTRACTION", 300, 520, 100, 50, blue, bright_blue, "intro")
        pygame.display.update()
        clock.tick(50)


def score_system(passed, score):
    font = pygame.font.Font("freesansbold.ttf", 25)
    text = font.render("passed " + str(passed), True, black)
    score = font.render("score " + str(score), True, black)
    gamedisplays.blit(text, (0, 50))
    gamedisplays.blit(score, (0, 30))


def obstacle(obs_startx, obs_starty, obs):
    if obs == 0:
        obs_pic = pygame.image.load('Images/car2.jpg')
    elif obs == 1:
        obs_pic = pygame.image.load('Images/car4.jpg')
    elif obs == 2:
        obs_pic = pygame.image.load('Images/car5.jpg')
    elif obs == 3:
        obs_pic = pygame.image.load('Images/car6.jpg')
    gamedisplays.blit(obs_pic, (obs_startx, obs_starty))


def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = (int(display_width / 2), int(display_height / 2))
    gamedisplays.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display("WASTED")


def background():
    gamedisplays.blit(backgroundpic, (0, 0))
    gamedisplays.blit(backgroundpic, (0, 200))
    gamedisplays.blit(backgroundpic, (0, 400))

    gamedisplays.blit(backgroundpic, (720, 0))
    gamedisplays.blit(backgroundpic, (720, 200))
    gamedisplays.blit(backgroundpic, (720, 400))

    gamedisplays.blit(yellow_strip, (80, 200))
    gamedisplays.blit(yellow_strip, (80, 0))
    gamedisplays.blit(yellow_strip, (80, 400))

    gamedisplays.blit(yellow_strip, (683, 0))
    gamedisplays.blit(yellow_strip, (683, 200))
    gamedisplays.blit(yellow_strip, (683, 400))

    gamedisplays.blit(white_strip, (400, 200))
    gamedisplays.blit(white_strip, (400, 0))
    gamedisplays.blit(white_strip, (400, 400))
    gamedisplays.blit(white_strip, (400, 100))
    gamedisplays.blit(white_strip, (400, 300))
    gamedisplays.blit(white_strip, (400, 500))


def car(x, y):
    gamedisplays.blit(carimg, (int(x), int(y)))


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.65)
    x_change = 0

    obstacle_speed = 9
    obs = 0
    y_change = 0
    obs_startx = random.randrange(200, display_width - 200)
    obs_starty = -750
    obs_width = 113
    obs_height = 250

    passed = 0
    level = 1
    score = 0

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = 5
                if event.key == pygame.K_RIGHT:
                    x_change = -5
                if event.key == pygame.K_SPACE:
                    obstacle_speed += 2
                if event.key == pygame.K_b:
                    obstacle_speed -= 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x = x - x_change

        gamedisplays.fill(gray)

        background()

        obs_starty -= int(obstacle_speed / 4)
        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obstacle_speed

        car(x, y)

        score_system(passed, score)

        if x > 690 - car_width or x < 100:
            crash()
        if x > display_width - (car_width + 100) or x < 100:
            crash()
        if obs_starty > display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(170, (display_width - 170))
            obs = random.randrange(0, 4)
            passed = passed + 1
            score = passed * 10
            if int(passed % 10) == 0:
                level = level + 1
                obstacle_speed += 3
                largetext = pygame.font.Font("freesansbold.ttf", 80)
                textsurf, textrect = text_objects("Level " + str(level), largetext)
                textrect.center = (int(display_width / 2), int(display_height / 2))
                gamedisplays.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if y < obs_starty + obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x + car_width > obs_startx and x + car_width < obs_startx + obs_width:
                crash()
        button("Pause",650,0,150,50,blue,bright_blue,"pause")
        pygame.display.update()
        clock.tick(60)


intro_loop()
game_loop()
pygame.quit()
quit()
