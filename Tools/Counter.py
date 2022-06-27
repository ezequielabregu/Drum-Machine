import pygame

clock = 0
bang = 0

timer = pygame.time.Clock()

while True:
    clock += 1
    limitedCounter = clock % 1000
    if modulo == 0:
        bang += 1
        print(bang)
    timer.tick(1000)
