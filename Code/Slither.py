import random
import pygame

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

'''
    Initializing the colors used
'''

red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 155, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake and Apple")
pygame.display.update()


# Bringing all the images in the game
# USER HAS TO CHANGE THE PATH OF THE IMAGES


icon = pygame.image.load('C:/Users/1/PycharmProjects/HELLO/snakehead.png')
pygame.display.set_icon(icon)
img = pygame.image.load('C:/Users/1/PycharmProjects/HELLO/snakehead.png')
Apple = pygame.image.load('C:/Users/1/PycharmProjects/HELLO/Apple.png')
Snake = pygame.image.load('C:/Users/1/PycharmProjects/HELLO/Snake.jpg')
Applede = pygame.image.load('C:/Users/1/PycharmProjects/HELLO/Applede.jpg')


# Bringing all the sounds in the game
# USER HAS TO CHANGE THE PATH OF THE IMAGES


applecutsound = pygame.mixer.Sound('C:/Users/1/PycharmProjects/HELLO/applecut.wav')
music = pygame.mixer.music.load('C:/Users/1/PycharmProjects/HELLO/music.mp3')
gameoversound = pygame.mixer.Sound('C:/Users/1/PycharmProjects/HELLO/gameover.wav')


'''
    Initializing the font and types
'''


font = pygame.font.SysFont('comicaansms', 15)
smallfont = pygame.font.SysFont('comicaansms', 25)
medfont = pygame.font.SysFont('comicaansms', 50)
largefont = pygame.font.SysFont('comicaansms', 65)

clock = pygame.time.Clock()
applethickness = 30


'''
    Function to calculate and update the score
'''


def score(scored):
    text = smallfont.render("Score: " + str(scored), True, black)
    gameDisplay.blit(text, [0, 0])


'''
    Function to handle the pause condition        
'''


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                   # If the cross button is pressed
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:                 # c to continue
                    pygame.mixer.music.unpause()
                    paused = False
                elif event.key == pygame.K_q:               # q to quit
                    pygame.quit()
                    quit()
        message_on_screen("Paused", black, -100, 'large')
        message_on_screen("Press C to continue or Q to quit", blue, 10, 'med')
        pygame.display.update()
        clock.tick(15)


'''
    Function for the beginning screen of the game
'''


def game_intro():
    pygame.mixer.music.play()
    intro = True
    while intro:

        gameDisplay.fill(white)

        maintext = largefont.render("Welcome to", True, green)
        gameDisplay.blit(maintext, (50, 180))
        gameDisplay.blit(Snake, (300, 140))
        maintext = largefont.render("and", True, green)
        gameDisplay.blit(maintext, (410, 180))
        gameDisplay.blit(Applede, (500, 130))
        maintext = largefont.render("game", True, green)
        gameDisplay.blit(maintext, (660, 180))
        message_on_screen("You have to eat apple and get longer and longer",
                          black,
                          -10,
                          'small')
        message_on_screen("If you run into yourself, or the edges you die",
                          black,
                          10,
                          'small')
        message_on_screen("Press C To play  Q to quit  P to pause",
                          green,
                          150,
                          'med')
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:                   # If the cross button is pressed
                intro = False
                break

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_c:                 # c to continue
                    Game_loop()
                elif event.key == pygame.K_q:               # q to quit
                    intro = False
                    break

        clock.tick(15)


def apple(appleX, appleY):
    head = Apple
    gameDisplay.blit(head, (appleX, appleY))


'''
    Function to continuously change the coordinates of apple
'''


def getapplexy():
    appleX = round(random.randint(0, display_width - applethickness))
    appleY = round(random.randint(0, display_height - applethickness))
    return appleX, appleY


'''
    Function to print all the parts of snake
'''


def snake(block_size, snakelist, direction):
    if direction == 'right':
        head = pygame.transform.rotate(img, 270)
    elif direction == 'left':
        head = pygame.transform.rotate(img, 90)
    elif direction == 'north':
        head = img
    elif direction == 'south':
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

    for xny in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [xny[0], xny[1], block_size, block_size])


'''
    Function to center the text
'''


def text_objects(text, color, fonttype):
    if fonttype == 'small':
        textSurface = smallfont.render(text, True, color)
        return textSurface, textSurface.get_rect()

    elif fonttype == 'med':
        textSurface = medfont.render(text, True, color)
        return textSurface, textSurface.get_rect()

    elif fonttype == 'large':
        textSurface = largefont.render(text, True, color)
        return textSurface, textSurface.get_rect()


'''
    Function to print text on screen
'''


def message_on_screen(msg, color, y_displace=0, fonttype='small'):
    textSurf, textRect = text_objects(msg, color, fonttype)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


'''
    The main game loop
'''


def Game_loop():
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 10
    lead_y_change = 0
    block_size = 20
    fps = 60
    scored = 0

    snakelist = []
    snakelength = 1
    direction = 'right'

    appleX, appleY = getapplexy()

    gameexit = True
    gameover = False

    while gameexit:
        '''
            To handle if the game is in a Gameover condition
        '''
        while gameover:

            gameDisplay.fill(white)
            message_on_screen("GAME OVER", red, -50, 'large')
            message_on_screen("Press c to play again or q to quit", (21, 32, 54), 50, 'med')

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:               # If the cross button is pressed
                    gameover = False
                    gameexit = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_c:             # c to continue
                        pygame.mixer.music.unpause()
                        Game_loop()

                    elif event.key == pygame.K_q:           # q to quit
                        gameover = False
                        gameexit = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:                   # If the cross button is pressed
                gameexit = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:             # To make the snake go right
                    lead_x_change = block_size / 2
                    lead_y_change = 0
                    direction = "right"
                elif event.key == pygame.K_LEFT:            # To make the snake go left
                    lead_x_change = -block_size / 2
                    lead_y_change = 0
                    direction = "left"
                elif event.key == pygame.K_UP:              # To make the snake go up
                    lead_y_change = -block_size / 2
                    lead_x_change = 0
                    direction = "north"
                elif event.key == pygame.K_DOWN:            # To make the snake go down
                    lead_y_change = block_size / 2
                    lead_x_change = 0
                    direction = "south"
                elif event.key == pygame.K_p:               # p tp pause the game
                    pygame.mixer.music.pause()
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameover = True
            pygame.mixer.music.pause()
            gameoversound.play()

        lead_x += lead_x_change                             # To change the snake's head position
        lead_y += lead_y_change

        gameDisplay.fill(white)
        apple(appleX, appleY)

        snakehead = [lead_x, lead_y]                        # List containing the parts of snake according to its length
        snakelist.append(snakehead)
        if len(snakelist) > snakelength:
            del snakelist[0]

        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:                    # If the snake runs into itself
                pygame.mixer.music.pause()
                gameoversound.play()
                gameover = True

        snake(block_size, snakelist, direction)
        score(scored)
        pygame.display.update()

        # To change the position of apple after the snake eats it

        if (appleX < lead_x < appleX + applethickness or appleX < lead_x + block_size < appleX + applethickness) and (
                appleY < lead_y < appleY + applethickness or appleY < lead_y + block_size < appleY + applethickness):
            applecutsound.play()
            appleX, appleY = getapplexy()
            snakelength += 1
            scored += 1
        clock.tick(fps)

    pygame.quit()
    quit()

    # Function to start the game


game_intro()
