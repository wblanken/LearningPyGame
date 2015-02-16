#! /usr/bin/env python
"""
Excercise 10:
Create a program that upon start-up checks the time of the day 
and sets the brightness of the background color accordingly. 
Use a blue scale. If it is midnight, the screen should be black. 
If it is midday, the screen should be bright blue. 
Any other time the background should be something in between 
corresponding to the brightness outside.
"""

import pygame
import datetime


# Get the current time of day
hour = int(datetime.datetime.now().hour)
print 'The current hour is: ', str(hour)
# Set the blue value based on the time and range (0-255) 
# Where 00:00 is 0 and 12:00 is 255 (step of 21.25)
if hour <= 12:
	blueshift = 0 * 21.25
else:
	blueshift = (12 - (hour - 12)) * 21.25
print blueshift

screen = pygame.display.set_mode((640, 400))
running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	screen.fill((0, 0, blueshift))
	pygame.display.flip()

