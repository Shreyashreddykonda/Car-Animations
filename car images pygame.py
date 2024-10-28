import pygame
from pygame.locals import *
pygame.init()

window = pygame.display.set_mode((600, 600))
image0 = pygame.image.load("C:/Users/dasar/Desktop/th17.jpeg")
image1 = pygame.image.load("C:/Users/dasar/Desktop/th18.jpeg")
image2 = pygame.image.load("C:/Users/dasar/Desktop/th19.jpeg")
image3 = pygame.image.load("C:/Users/dasar/Desktop/th20.jpeg")
image4 = pygame.image.load("C:/Users/dasar/Desktop/th20.jpeg")
image5 = pygame.image.load("C:/Users/dasar/Desktop/th21.jpeg")
image6 = pygame.image.load("C:/Users/dasar/Desktop/th22.jpeg")
image7 = pygame.image.load("C:/Users/dasar/Desktop/th23.jpeg")
image8 = pygame.image.load("C:/Users/dasar/Desktop/th24.jpeg")
image_sprite = [image0, image1, image2, image3, image4, image5, image6, image7, image8]
clock = pygame.time.Clock()
imageindex = 0

run = True
while run:
    clock.tick(3)
    if imageindex >= len(image_sprite):
        imageindex = 0

    image = image_sprite[imageindex]
    x = 150
    if imageindex == 0:
        y = 200
        x = 100
    elif imageindex == 1:
        y = 300
        x = 0
        
    window.blit(image, (x, y))
    pygame.display.update()
    window.fill((0, 0, 0))
    imageindex += 1
    


