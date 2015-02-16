#! /usr/bin/env python
"""
Excercise 18:
Add a vertical line as well
"""
import pygame


x = 0
y = 0
xdir = 1
ydir = 1
running = 1
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
linecolor = 255, 0, 0
linecolor2 = 0, 255, 0
bgcolor = 0, 0, 0

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	
	screen.fill(bgcolor)
	pygame.draw.line(screen, linecolor, (0, y), (width - 1, y))
	pygame.draw.line(screen, linecolor2, (x, 0), (x, height - 1))
	
	x += xdir
	if x == 0 or x == width-1:
		xdir *= -1
	y += ydir
	if y == 0 or y == height-1:
		ydir *= -1

	pygame.display.flip()
