# !/bin/usr/env python
"""
Excercise 16:
Draw more complex pattern
Once you have solved it for the upper left hand corner, 
repeat it so that the same pattern is drawn in all four corners of the screen. 
You should be able to draw all in all corners with a single loop 
and four calls to pygame.draw.line.
"""
import pygame


width = 400
height = 400

black = (0x0, 0x0, 0x0)
red = (0xff, 0x0, 0x0)
green = (0x0, 0xff, 0x0)
blue = (0x0, 0x0, 0xff)
yellow = (0xff, 0x0, 0xff)
grey = (0x77, 0x77, 0x77)

lineColor = red

screen = pygame.display.set_mode((width, height))

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break;
	
	screen.fill(black)
	for i in range(0, height + 25, 25):
		pygame.draw.line(screen, lineColor, (0, 0 + i), (abs(width - i), 0))
		pygame.draw.line(screen, lineColor, (width, 0 + i), (abs(width - i), height))
		pygame.draw.line(screen, lineColor, (width, abs(height - i)), (abs(width - i),  0))
		pygame.draw.line(screen, lineColor, (0, abs(height - i)), (abs(width -i), height))
	pygame.display.flip()
