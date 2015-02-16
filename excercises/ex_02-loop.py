#! /usr/bin/env python
"""
Excercise 02:
Create a program where the user can specify the width 
and the height as command line arguments.
Add running loop.
"""


import sys
import pygame

if len(sys.argv) < 3:
	raise Exception("Not enough inputs")

print 'Argument list: ', str(sys.argv)

screen = pygame.display.set_mode((int(sys.argv[1]), int(sys.argv[2])))
running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
