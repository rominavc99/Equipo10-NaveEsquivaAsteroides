from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import math

class Cometa1:
    posX = -1.3
    posY = 0.4
    velocidadX = 0.75
    velocidadY = -0.15
    ang = math.degrees(math.atan(velocidadY / velocidadX))

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidadX * deltatime
        self.posY = self.posY + self.velocidadY * deltatime
        if self.posX > 1.3:
            self.posX = -1.3
            self.posY = 0.4

    def dibujar(self):
        glPushMatrix()
        glTranslate(self.posX, self.posY,0.0)
        glRotatef(self.ang,0,0,1)
        glScalef(0.05,0.01,0.0)
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1.0,1.0,1.0)
        glVertex3f(0.5,0.0,0.0)
        for x in range(362):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.0)
            glVertex3f(cos(angulo),sin(angulo),0.0)
        glEnd()
        glPopMatrix()

class Cometa2:
    posX = -1.3
    posY = 0.2
    velocidadX = 0.5
    velocidadY = -0.1
    ang = math.degrees(math.atan(velocidadY / velocidadX))

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidadX * deltatime
        self.posY = self.posY + self.velocidadY * deltatime
        if self.posX > 1.3:
            self.posX = -1.3
            self.posY = 0.2

    def dibujar(self):
        glPushMatrix()
        glTranslate(self.posX, self.posY,0.0)
        glRotatef(self.ang,0,0,1)
        glScalef(0.05,0.01,0.0)
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.2,0.7,1.0)
        glVertex3f(0.5,0.0,0.0)
        for x in range(362):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.0)
            glVertex3f(cos(angulo),sin(angulo),0.0)
        glEnd()
        glPopMatrix()

class Cometa3:
    posX = -1.3
    posY = 0.0
    velocidadX = 1.0
    velocidadY = -0.2
    ang = math.degrees(math.atan(velocidadY / velocidadX))

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidadX * deltatime
        self.posY = self.posY + self.velocidadY * deltatime
        if self.posX > 1.3:
            self.posX = -1.3
            self.posY = 0.0

    def dibujar(self):
        glPushMatrix()
        glTranslate(self.posX, self.posY, 0.0)
        glRotatef(self.ang,0,0,1)
        glScalef(0.05,0.01,0.0)
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1.0,0.2,0.5)
        glVertex3f(0.5,0.0,0.0)
        for x in range(362):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.0)
            glVertex3f(cos(angulo),sin(angulo),0.0)
        glEnd()
        glPopMatrix()