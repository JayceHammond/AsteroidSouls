import pygame as p
from pygame import mixer
import math
import numpy
import random as r
from collider import Collider

class Ship:
    def __init__(self, posx, posy, speed, img, width, height, xDir, yDir):
        self.posx = posx
        self.posy = posy
        self.xDir = xDir
        self.yDir = yDir
        self.img = img
        self.width = width
        self.height = height
        self.speed = speed
        self.name = "Player"
        self.ship = p.image.load(self.img)
        self.col = Collider(self)


    def display(self, screen, mousePos):
        self.ship = p.image.load(self.img)
        self.ship = p.transform.rotate(self.ship, -math.degrees(self.getAngle(mousePos)))
        screen.blit(self.ship, (self.posx, self.posy))

    def update(self, xDir, yDir, obj):
            self.posx = self.posx + self.speed * xDir
            self.posy = self.posy + self.speed * yDir

            self.col.checkCollision(obj, self.xDir)


    def getAngle(self, mousePos):
            # Lock the x-coordinate of the mouse at x = 325
            mouse_x = mousePos[0] # Get the x-coordinate of the mouse
            mouse_y = mousePos[1]  # Get the y-coordinate of the mouse

            # Calculate the angle in radians
            angle = math.atan2(mouse_y - self.posy, mouse_x - self.posx)

            # Convert the angle to degrees and ensure it's within -90 to 90 degrees
            angle_degrees = math.degrees(angle)
            adjusted_angle_degrees = angle_degrees if -90 <= angle_degrees <= 90 else (angle_degrees + 180) % 360 - 180

            # Convert the angle back to radians
            adjusted_angle = math.radians(adjusted_angle_degrees)

            return adjusted_angle

    