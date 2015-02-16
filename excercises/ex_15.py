# !/bin/usr/env python
"""
Excercise 15:
Program that draws 4 lines, each a different color, and takes in the 
width and height as arguments.
"""
import pygame


black = (0x0, 0x0, 0x0)
red = (0xff, 0x0, 0x0)
green = (0x0, 0xff, 0x0)
blue = (0x0, 0x0, 0xff)
yellow = (0xff, 0x0, 0xff)

print 'Input the width: '
width = int(raw_input())

print 'Input the height: '
height = int(raw_input())

lineOneColor = blue
lineOneLeft = (0, 0)
lineOneRight = (width, height)

lineTwoColor = red
lineTwoLeft = (0, height)
lineTwoRight = (width, 0)

lineThreeColor = green
lineThreeLeft = (width / 2, 0)
lineThreeRight = (width / 2, height)

lineFourColor = yellow
lineFourLeft = (0, height / 2)
lineFourRight = ( width, height / 2)

screen = pygame.display.set_mode((width, height))

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break;
	
	screen.fill(black)
	pygame.draw.line(screen, lineOneColor, lineOneLeft, lineOneRight)
	pygame.draw.line(screen, lineTwoColor, lineTwoLeft, lineTwoRight)
	pygame.draw.aaline(screen, lineThreeColor, lineThreeLeft, lineThreeRight)
	pygame.draw.aaline(screen, lineFourColor, lineFourLeft, lineFourRight)
	pygame.display.flip()
