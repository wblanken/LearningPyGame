#! /usr/bin/env python
"""
Excercise 01:
Create a window that is 320 pixels wide and 200 pixels high.
Add running loop
"""

import pygame

screen = pygame.display.set_mode((320, 200))
running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
