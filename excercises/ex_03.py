#! /usr/bin/env python
"""
Excercise 03:
Create a program that asks the users for the width 
and the height and then displays the window.
"""


import pygame

print "Please specify the height for the program: "
height = raw_input()

print "Please specify the width for the program: "
width = raw_input()

screen = pygame.display.set_mode((int(height), int(width)))

while 1:
	pass
