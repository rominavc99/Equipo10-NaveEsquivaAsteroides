from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import math

class Satelite1:
    posX = -0.6
    posY = -0.2
    velocidad = 1.2

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidad * deltatime
        if self.posX > 1.3:
            self.posX = -1.3

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posX,self.posY,0)
        glScalef(0.035,0.035,0.035)
        glRotate(-30,0,0,1)
        glColor3f(0.7,0.7,0.7)
        glBegin(GL_POLYGON)
        glVertex3f(-1.0,0.025,0.0)
        glVertex3f(1.0,0.025,0.0)
        glVertex3f(1.0,-0.025,0.0)
        glVertex3f(-1.0,-0.025,0.0)
        glEnd()
        glColor3f(0.0,0.0,0.7)
        glBegin(GL_POLYGON)
        glVertex3f(-1.0,1.0,0.0)
        glVertex3f(-0.9,1.0,0.0)
        glVertex3f(-0.9,-1.0,0.0)
        glVertex3f(-1.0,-1.0,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f(1.0,-1.0,0.0)
        glVertex3f(0.9,-1.0,0.0)
        glVertex3f(0.9,1.0,0.0)
        glVertex3f(1.0,1.0,0.0)
        glEnd()
        glColor3f(0.9,0.9,0.9)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.3,sin(angulo)*0.3,0.0)
        glEnd()
        glPopMatrix()

class Satelite2:
    posX = 0.0
    posY = -0.2
    velocidad = 1.2

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidad * deltatime
        if self.posX > 1.3:
            self.posX = -1.3

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posX,self.posY,0)
        glScalef(0.035,0.035,0.035)
        glRotate(30,0,0,1)
        glColor3f(0.0,0.0,0.7)
        glBegin(GL_POLYGON)
        glVertex3f(-1.0,0.2,0.0)
        glVertex3f(1.0,0.2,0.0)
        glVertex3f(1.0,-0.2,0.0)
        glVertex3f(-1.0,-0.2,0.0)
        glEnd()
        glPopMatrix()
        glPushMatrix()
        glTranslatef(self.posX,self.posY,0)
        glScalef(0.035,0.035,0.035)
        glRotate(-30,0,0,1)
        glColor3f(0.9,0.9,0.9)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.6,sin(angulo)*0.3,0.0)
        glEnd()
        glPopMatrix()

class Satelite3:
    posX = 0.6
    posY = -0.2
    velocidad = 1.2

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidad * deltatime
        if self.posX > 1.3:
            self.posX = -1.3

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posX,self.posY,0)
        glScalef(0.035,0.035,0.035)
        glRotate(30,0,0,1)
        glColor3f(0.3,0.3,0.3)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.4,sin(angulo)*0.4+0.6,0.0)
        glEnd()
        glColor3f(0.2,0.2,0.2)
        glBegin(GL_TRIANGLE_STRIP)
        for x in range(20):
            x = x + 1
            if x % 3 == 0:
                angulo = (x + 265) * 3.14159 / 180.0
                glVertex3f(cos(angulo)*1.8,sin(angulo)*1.8+0.6,0.0)
            else:
                angulo = (x + 265) * 3.14159 / 180.0
                glVertex3f(cos(angulo)*0.4,sin(angulo)*0.4+0.6,0.0)
        glEnd()
        glPopMatrix()