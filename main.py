import pygame
from pygame import mixer

pygame.init()
# dimensions
WITH = 1400
HEIGHT = 800
# colores
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
green = (0, 255, 0)
gold = (212, 175, 55)
tickness1 = 1


screen = pygame.display.set_mode([WITH, HEIGHT])                        #create screen
pygame.display.set_caption('Beat Maker')
label_font = pygame.font.Font('Roboto-Bold.ttf', 32)

fps = 60                                                                        # Frame rate
timer = pygame.time.Clock()                                                     # MASTER CLOCK
instruments = 6
beats = 8
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]

def draw_grid(clicks):
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT], tickness1)           # left box-Arguments (x, y, with, height, tick)
    botton_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WITH, 200], tickness1)
    boxes = []                                                                  # steps
    colors = [gray, white, gray]
    hi_hat_text = label_font.render('Hi Hat', True, white)                      # hit hat text
    screen.blit(hi_hat_text, (30, 30))                                          # display hit hat text
    snare_text = label_font.render('Snare', True, white)  # texto hit hat
    screen.blit(snare_text, (30, 130))
    kick_text = label_font.render('Kick', True, white)  # texto hit hat
    screen.blit(kick_text, (30, 230))
    crash_text = label_font.render('crash', True, white)  # texto hit hat
    screen.blit(crash_text, (30, 330))
    clap_text = label_font.render('Clap', True, white)  # texto hit hat
    screen.blit(clap_text, (30, 430))
    tom_text = label_font.render('Tom', True, white)  # texto hit hat
    screen.blit(tom_text, (30, 530))

    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, i * 100), (200, i * 100), tickness1)     #surface, color, start position (x, y), end position, with

    for i in range(beats):
        for j in range(instruments):
            if clicks[j][i] == -1:
                color = gray
            else:
                color = green
            rect = pygame.draw.rect(screen, color,
                                    [i * ((WITH - 200) // beats) + 200,     # initial position (x axis)
                                    (j * 100 + 5),                              # initial position (y axis)
                                    ((WITH - 200)) // beats - 10,                # with
                                    ((HEIGHT - 200) // instruments) - 10],       # high
                                    0, 3)

            pygame.draw.rect(screen, gold,
                                    [i * ((WITH - 200) // beats) + 200,  # initial position (x axis)
                                    (j * 100),  # initial position (y axis)
                                    ((WITH - 200)) // beats,  # with
                                    ((HEIGHT - 200) // instruments)],  # high
                                    5, 5)

            pygame.draw.rect(screen, black,
                                [i * ((WITH - 200) // beats) + 200,  # initial position (x axis)
                                (j * 100),  # initial position (y axis)
                                ((WITH - 200)) // beats,  # with
                                ((HEIGHT - 200) // instruments)],  # high
                                5, 5)

            boxes.append((rect, (i, j)))                                    #ESTO NO LO ENTIENDO
    return boxes


run = True                                                                  # start the game

while run:
    timer.tick(fps)
    screen.fill(black)                                                          # meanwhile the game is ON, fill the screen
    draw_grid(clicked)
    boxes = draw_grid(clicked)

    for event in pygame.event.get():                                            # check if someone is pressing a key, mouse, etc (every event)
        if event.type == pygame.QUIT:                                           # if some quit, stop the game
            run = False                                                         # stop the game
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range (len(boxes)):
                if boxes[i][0].collidepoint(event.pos):                                    # chekea si lo hace dentro del mouse
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1
    pygame.display.flip()
pygame.quit()