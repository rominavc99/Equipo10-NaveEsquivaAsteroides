from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import math
class UFO1:
    posX = 0.0
    posY = 0.2
    velocidad = 2.0

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidad * deltatime
        if self.posX > 1.3:
            self.posX = -1.3

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posX,self.posY,0)
        glScalef(0.035,0.035,0.035)
        glColor3f(0.7,0.8,1.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.5,sin(angulo)*0.5,0.0)
        glEnd()
        glColor3f(0.6,0.6,0.6)
        glBegin(GL_QUADS)
        glVertex3f(-0.5,0.0,0.0)
        glVertex3f(0.5,0.0,0.0)
        glVertex3f(1.0,-0.5,0.0)
        glVertex3f(-1.0,-0.5,0.0)
        glEnd()
        glColor3f(1.0,0.0,0.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.1,sin(angulo)*0.1-0.25,0.0)
        glEnd()
        glColor3f(1.0,0.0,0.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.1-0.4,sin(angulo)*0.1-0.25,0.0)
        glEnd()
        glColor3f(1.0,0.0,0.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.1+0.4,sin(angulo)*0.1-0.25,0.0)
        glEnd()
        glPopMatrix()

class UFO2:
    posX = -0.5
    posY = 0.6
    velocidad = 2.5

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidad * deltatime
        if self.posX > 1.3:
            self.posX = -1.3

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posX,self.posY,0)
        glScalef(0.035,0.035,0.035)
        glColor3f(0.9,0.9,1.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.5,sin(angulo)*0.5,0.0)
        glEnd()
        glColor3f(0.6,0.6,0.6)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo),sin(angulo)*0.1-0.25,0.0)
        glEnd()
        glColor3f(0.0,0.0,1.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.1,sin(angulo)*0.1-0.25,0.0)
        glEnd()
        glColor3f(0.0,0.0,1.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.1-0.4,sin(angulo)*0.1-0.25,0.0)
        glEnd()
        glColor3f(0.0,0.0,1.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.1+0.4,sin(angulo)*0.1-0.25,0.0)
        glEnd()
        glPopMatrix()

class UFO3:
    posX = 0.5
    posY = 0.6
    velocidad = 2.5

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidad * deltatime
        if self.posX > 1.3:
            self.posX = -1.3

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posX,self.posY,0)
        glScalef(0.035,0.035,0.035)
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.0,1.0,0.0)
        glVertex3f(0.0,0.0,0.0)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.0)
            glVertex3f(cos(angulo),sin(angulo)*0.5,0.0)
        glEnd()
        glColor3f(0.2,0.2,0.2)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.5,sin(angulo)*0.3,0.0)
        glEnd()
        glColor3f(0.2,0.2,0.2)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo),sin(angulo)*0.2,0.0)
        glEnd()
        glColor3f(0.0,1.0,0.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.1,sin(angulo)*0.1,0.0)
        glEnd()
        glColor3f(0.0,1.0,0.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.1-0.4,sin(angulo)*0.1,0.0)
        glEnd()
        glColor3f(0.0,1.0,0.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.1+0.4,sin(angulo)*0.1,0.0)
        glEnd()
        glPopMatrix()