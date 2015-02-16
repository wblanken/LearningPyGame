#! /usr/bin/env python
"""
Excercise 07:
Create a window with a red background color.
"""


import pygame

screen = pygame.display.set_mode((640, 400))
running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	screen.fill((255, 0, 0))
	pygame.display.flip()

