#! /usr/bin/env python
"""
Excercise 14:
Draw centered horizontal and vertical lines
"""

import pygame


width = int(640)
height = int(400)

blue = (0x0, 0x0, 0xff)
red = (0xff, 0x0, 0x0)
green = (0x0, 0xff, 0x0)

lineOneColor = blue
lineTwoColor = red 

lineOneLeft = (0, height / 2)
lineOneRight = (width, height / 2)
lineTwoLeft = (width / 2, 0)
lineTwoRight = (width / 2, height)

screen = pygame.display.set_mode((width, height))
running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	
	screen.fill((0, 0, 0))
	pygame.draw.line(screen, lineOneColor, lineOneLeft, lineOneRight)
	pygame.draw.aaline(screen, lineTwoColor, lineTwoRight, lineTwoLeft)
	pygame.display.flip()

