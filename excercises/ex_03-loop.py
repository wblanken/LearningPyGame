#! /usr/bin/env python
"""
Excercise 03:
Create a program that asks the users for the width 
and the height and then displays the window.
Add running loop.
"""


import pygame

print "Please specify the height for the program: "
height = raw_input()

print "Please specify the width for the program: "
width = raw_input()

screen = pygame.display.set_mode((int(height), int(width)))
running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
