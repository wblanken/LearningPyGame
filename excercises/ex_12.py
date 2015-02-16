#! /usr/bin/env python
"""
Excercise 12:
Improve the program further by declaring variables called linecolor, topleft, bottomright and so on. Modify the program to make use of the variables.
"""

import pygame


width = int(640)
height = int(400)

blue = (0x0, 0x0, 0xff)
lineColor = blue

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
	pygame.draw.line(screen, lineColor, topLeft, bottomRight)
	pygame.draw.aaline(screen, lineColor, topRight, bottomLeft)
	pygame.display.flip()

