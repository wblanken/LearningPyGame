#! /bin/usr/env python
"""
Excercise 05:
Rewrite the program to do away with the running flag. 
Make sure that the program still jumps out of the event loop 
on the QUIT event.
"""


import pygame

screen = pygame.display.set_mode((640, 400))

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break;
