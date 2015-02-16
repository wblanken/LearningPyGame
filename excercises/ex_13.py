#! /usr/bin/env python
"""
Excercise 13:
Modify the program to draw the two lines in different colors.
"""

import pygame


width = int(640)
height = int(400)

blue = (0x0, 0x0, 0xff)
red = (0xff, 0x0, 0x0)
green = (0x0, 0xff, 0x0)

lineOneColor = blue
lineTwoColor = red 

topLeft = (0, 0)
topRight = (width, 0)
bottomLeft = (0, height)
bottomRight = (width, height)

screen = pygame.display.set_mode((width, height))
running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	
	screen.fill((0, 0, 0))
	pygame.draw.line(screen, lineOneColor, topLeft, bottomRight)
	pygame.draw.aaline(screen, lineTwoColor, topRight, bottomLeft)
	pygame.display.flip()

