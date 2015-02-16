#! /usr/bin/env python
"""
Excercise 09:
Create a program that asks the user to specify the values for red, green
and blue. Validate the range (0-255) and then use these for the background
"""

import pygame


print 'Please specify a red color value: '
red = int(raw_input())
if red < 0 or red > 255:
	raise Exception("Red value is out of range")

print 'Please specify a blue color value: '
blue = int(raw_input())
if blue < 0 or blue > 255:
	raise Exception("Blue value is out of range")

print 'Please specify a green color value: '
green = int(raw_input())
if green < 0 or green > 255:
	raise Exception("Green value is out of range")

screen = pygame.display.set_mode((640, 400))
running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	screen.fill((red, blue, green))
	pygame.display.flip()

