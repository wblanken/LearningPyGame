#! /usr/bin/env python
"""
Excercise 04:
Write a program that calls pygame.display.set_mode 
twice with different sizes.
Add running loop
"""


import pygame

screen = pygame.display.set_mode((320, 200))

screen = pygame.display.set_mode((640, 400))
running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
