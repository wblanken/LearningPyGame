#! /usr/bin/env python
"""
Excercise 11:
Use variables for width and height
"""

import pygame


width = int(640)
height = int(400)

screen = pygame.display.set_mode((width, height))
running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	
	screen.fill((0, 0, 0))
	pygame.draw.line(screen, (0, 0, 255), (0, 0), (width, height))
	pygame.draw.aaline(screen, (0, 0, 255), (width, 0), (0, height))
	pygame.display.flip()

