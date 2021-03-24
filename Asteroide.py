from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import math

class Asteroide1:
    posX = 0.0
    posY = -0.6
    velocidad = 1.0

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidad * deltatime
        if self.posX > 1.3:
            self.posX = -1.3

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posX,self.posY,0)
        glScalef(0.035,0.035,0.035)
        glColor3f(0.5,0.5,0.5)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.85-0.4,sin(angulo)*0.85-0.4,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.75+0.4,sin(angulo)*0.75+0.4,0.0)
        glEnd()
        glPopMatrix()

class Asteroide2:
    posX = -0.5
    posY = -0.4
    velocidad = 1.0

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidad * deltatime
        if self.posX > 1.3:
            self.posX = -1.3

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posX,self.posY,0)
        glScalef(0.035,0.035,0.035)
        glColor3f(0.3,0.3,0.3)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.85-0.3,sin(angulo)*0.7+0.3,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.75+0.3,sin(angulo)*0.75-0.3,0.0)
        glEnd()
        glPopMatrix()

class Asteroide3:
    posX = 0.5
    posY = -0.4
    velocidad = 1.0

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidad * deltatime
        if self.posX > 1.3:
            self.posX = -1.3

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posX,self.posY,0)
        glScalef(0.035,0.035,0.035)
        glColor3f(0.5,0.5,0.5)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo),sin(angulo)*0.77,0.0)
        glEnd()
        glPopMatrix()

class Asteroide4:
    posX = -0.5
    posY = 0.0
    velocidad = 1.2

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidad * deltatime
        if self.posX > 1.3:
            self.posX = -1.3

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posX,self.posY,0)
        glScalef(0.035,0.035,0.035)
        glColor3f(0.3,0.3,0.3)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.85,sin(angulo)*0.85-0.4,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.75,sin(angulo)*0.75+0.4,0.0)
        glEnd()
        glPopMatrix()

class Asteroide5:
    posX = 0.5
    posY = 0.0
    velocidad = 1.2

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidad * deltatime
        if self.posX > 1.3:
            self.posX = -1.3

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posX,self.posY,0)
        glScalef(0.035,0.035,0.035)
        glRotate(45,0,0,1)
        glColor3f(0.5,0.5,0.5)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo),sin(angulo)*0.6,0.0)
        glEnd()
        glPopMatrix()

class Asteroide6:
    posX = -0.6
    posY = 0.4
    velocidad = 1.5

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidad * deltatime
        if self.posX > 1.3:
            self.posX = -1.3

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posX,self.posY,0)
        glScalef(0.035,0.035,0.035)
        glColor3f(0.3,0.3,0.3)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.85-0.4,sin(angulo)*0.7,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.75+0.4,sin(angulo)*0.7,0.0)
        glEnd()
        glPopMatrix()

class Asteroide7:
    posX = 0.0
    posY = 0.4
    velocidad = 1.5

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidad * deltatime
        if self.posX > 1.3:
            self.posX = -1.3

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posX,self.posY,0)
        glScalef(0.035,0.035,0.035)
        glRotatef(-45,0,0,1)
        glColor3f(0.5,0.5,0.5)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.75+0.4,sin(angulo)*0.55,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.75-0.4,sin(angulo)*0.75,0.0)
        glEnd()
        glPopMatrix()

class Asteroide8:
    posX = 0.6
    posY = 0.4
    velocidad = 1.5

    def actualizar(self, deltatime):
        self.posX = self.posX + self.velocidad * deltatime
        if self.posX > 1.3:
            self.posX = -1.3

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posX,self.posY,0)
        glScalef(0.035,0.035,0.035)
        glColor3f(0.3,0.3,0.3)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.75,sin(angulo)*0.65-0.3,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo),sin(angulo)*0.85+0.3,0.0)
        glEnd()
        glPopMatrix()