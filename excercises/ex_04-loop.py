#! /usr/bin/env python


import pygame

screen = pygame.display.set_mode((320, 200))

screen = pygame.display.set_mode((640, 400))
running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
