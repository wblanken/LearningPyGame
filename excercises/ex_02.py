#! /usr/bin/env python


import sys
import pygame

if len(sys.argv) < 3:
	raise Exception("Not enough inputs")

print 'Argument list: ', str(sys.argv)

screen = pygame.display.set_mode((int(sys.argv[1]), int(sys.argv[2])))

while 1:
	pass
