#! /bin/usr/env python


import pygame

screen = pygame.display.set_mode((640, 400))

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break;
