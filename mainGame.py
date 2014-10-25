__author__ = 'Wilson Koder'

# Created by Wilson Koder on the 23rd of October 2014
# Inspired by Boxes ;)
# In real life I can't wink.

import pymunk
import pygame
import pymunk.pygame_util
import sys

white = 255, 255, 255
green = 0, 255, 0
blue = 0, 0, 255

pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("PyBoxes v0.3")
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0.0, -900.0)

circle_count = 0
rad = 14
elasticity = 0.8

running = True

def create_circle(position):
    mass = 1
    inertia = pymunk.moment_for_circle(mass, 0, rad)
    body = pymunk.Body(mass, inertia)
    body.position = position
    #body.position = position
    shape = pymunk.Circle(body, rad)
    shape.elasticity = elasticity
    space.add(body, shape)
    return shape


def create_line(Space):
    body = pymunk.Body()
    body.position = (400, 600)
    line_shape = pymunk.Segment(body, (-400, -500), (400, -500), 15)
    line_shape.elasticity = 0.5
    Space.add(line_shape)
    return line_shape

line = create_line(space)
line.color = blue
circles = []

while running:
    for event in pygame.event.get():  # go through every event that frame.

        if event.type == pygame.QUIT:
            running = False  # if the user tries to quit the app, set running to false in order to exit the loop

        if event.type == pygame.KEYDOWN:  # check for keyboard input
            if event.key == pygame.K_c:  # clear the screen
                space.remove(circles)
                circles = []
            if event.key == pygame.K_w:  # increase size of ball
                rad += 5
            if event.key == pygame.K_s:  # decrease size of ball
                #must check if above 5 so it doesnt throw an error if you go below 0 :p
                if rad > 5:
                    rad -= 5
                else:
                    print("rad is too low to decrease even more.")
            if event.key == pygame.K_UP:
                elasticity += 0.25
            if event.key == pygame.K_DOWN:
                if elasticity > 0.5:
                    elasticity -= 0.25
                else:
                    print("e is to low to decrease even more.")

        if event.type == pygame.MOUSEBUTTONDOWN: # check if the mouse is clicked
            pos = pygame.mouse.get_pos()  # get the mouse pos
            real_pos = pymunk.pygame_util.to_pygame(pos, screen)
            new_circle = create_circle(real_pos)  # create a circle object
            circles.append(new_circle)  # add it to the list

    screen.fill(white)  # clear the screen

    space.step(1 / 60.0)  # step

    pymunk.pygame_util.draw(screen, line)  # draw the floor, couldn't get it working with normal pygame, so using util's

    for circle in circles:
        p_circle = int(circle.body.position.x), 600-int(circle.body.position.y)  # render each circle in the list
        pygame.draw.circle(screen, blue, p_circle, int(circle.radius), 2)  # render each circle in the list

    pygame.display.flip()  # draw everything
    clock.tick(60)  # limit fps :)

sys.exit()  # quit if the user is no longer running the application.

