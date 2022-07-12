import pygame
import random
from pygame import mixer



pygame.init()



window_height = 700
window_width = 500

my_font = pygame.font.SysFont('Comic Sans MS', 30)

my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Game Over!', False, (0, 0, 0))
game_window = pygame.display.set_mode((window_height,window_width))
pygame.display.set_caption("Snake")
pygame.display.update()

w,h = pygame.display.get_surface().get_size();



def printText(text,xpos,ypos,color):
    text_surface = my_font.render(text, False, color)
    game_window.blit(text_surface, (xpos, ypos))

def mainMenu():
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_RETURN):
                    gameLoop()
                elif (event.key == pygame.K_ESCAPE):
                    pygame.quit()
                elif (event.key == pygame.K_a):
                    aboutLoop(1)

        game_window.fill(pygame.Color(0,0,0))
        printText("Snake Game", w / 2 - 100, h / 2 - 50 , pygame.Color(255, 255, 255))
        printText(f"Press Enter to Start Game",w/2 - 100,h/2,pygame.Color(255,255,255))
        printText("Press A for about", w / 2 - 100, h / 2 + 50, pygame.Color(255, 255, 255))
        printText("Press Esc to Quit", w / 2 - 100, h / 2 + 100,pygame.Color(255,255,255))

        pygame.display.update()

def gameOverLoop(highScore):

    highScoreFile = open("HighScore", "r")

    if(int(highScoreFile.readline()) < highScore):
        highScoreFile = open("HighScore","w")
        highScoreFile.write(str(highScore))
        highScoreFile.close()

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    pygame.quit()
                elif (event.key == pygame.K_SPACE):
                    gameLoop()
                elif (event.key == pygame.K_m):
                    mainMenu()

        game_window.fill(pygame.Color(0,0,0))
        printText(f"Your score is {highScore}",w/2,h/2,pygame.Color(255,255,255))
        printText("Press Space to restart", w / 2, h / 2 + 100,pygame.Color(255,255,255))
        printText("Press Esc to quit", w / 2, h / 2 + 150,pygame.Color(255,255,255))
        printText("Press M for Main Menu", w / 2, h / 2 + 200, pygame.Color(255, 255, 255))
        pygame.display.update()

def aboutLoop(score):
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_b):
                    mainMenu()


        game_window.fill(pygame.Color(0,0,0))
        printText("Made in Pygame", w / 2 - 50, h / 2 - 50, pygame.Color(255, 255, 255))
        printText("Developer - ", w / 2 - 50, h / 2, pygame.Color(255, 255, 255))
        printText("twitter@shubhamjain207", w / 2 - 50, h / 2 + 50, pygame.Color(255, 255, 255))
        printText("Press B for back", w / 2 - 50, h / 2 + 100,pygame.Color(255,255,255))
        pygame.display.update()


def gameLoop():

    highScoreRead = open("HighScore","r")
    highScore = highScoreRead.readline()


    fps = 60

    player_position_x = 100
    player_position_y = 100
    player_velocity_x = 0
    player_velocity_y = 0
    player_speed = 3

    food_position_x = random.randint(50,w - 20)
    food_position_y = random.randint(50,h - 20)
    food_radius = 10

    score = 0

    snakelength = 1

    game_clock = pygame.time.Clock()

    snakeList = []
    snakeList.append([player_position_x, player_position_y])

    while True:
        for event in pygame.event.get():

            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_UP):
                    player_velocity_y=-player_speed
                    player_velocity_x =0
                elif(event.key == pygame.K_DOWN):
                    player_velocity_y=player_speed
                    player_velocity_x = 0
                elif (event.key == pygame.K_LEFT):
                    player_velocity_x=-player_speed
                    player_velocity_y = 0
                elif (event.key == pygame.K_RIGHT):
                    player_velocity_x=player_speed
                    player_velocity_y = 0
                elif(event.key == pygame.K_ESCAPE):
                    pygame.quit()


        player_position_y += player_velocity_y
        player_position_x += player_velocity_x

        if(player_position_x + 10 >= food_position_x - 15 and player_position_x + 10 <= food_position_x + 15 and player_position_y + 10 >= food_position_y - 15 and player_position_y + 10 <= food_position_y + 15):
            food_position_x = random.randint(50, 500)
            food_position_y = random.randint(50, 500)
            score+=10
            snakelength+=5
            mixer.music.load("foodpick.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play()

        snakeList.append([player_position_x, player_position_y])

        if(len(snakeList)>snakelength):
            del snakeList[0]

        if(player_position_x + 20 > w or player_position_y + 20 > h or player_position_x < 0 or player_position_y - 20 < 0 or [player_position_x,player_position_y] in snakeList[:-1]):
            mixer.music.load("d.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            gameOverLoop(score)





        game_window.fill(pygame.Color(0,0,0))


        for x,y in snakeList:
            pygame.draw.rect(game_window, pygame.Color(0, 255, 100),(x,y,20,20))

        printText(f"Score = {score}",w-200,0,pygame.Color(255,255,255))
        printText(f"High Score = {highScore}",10,0,pygame.Color(255,255,255))
        pygame.draw.circle(game_window,pygame.Color(255,0,0),(food_position_x,food_position_y),food_radius)
        pygame.display.update()

        game_clock.tick(fps)


mainMenu()


