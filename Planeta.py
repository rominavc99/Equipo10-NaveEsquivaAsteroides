from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import math

class Planeta1:
    def dibujar(self):
        #atmosfera
        glPushMatrix()
        glTranslate(0.0,-1.775,0.0)
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.0,0.0,1.0)
        glVertex3f(0.0,0.0,0.0)
        for x in range(361):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.0)
            glVertex3f(cos(angulo)*1.4,sin(angulo)*1.4,0.0)
        glEnd()
        glPopMatrix()
        #planeta
        glPushMatrix()
        glTranslate(0.0,-1.775,0.0)
        glColor3f(0.0,0.0,0.5)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo),sin(angulo),0.0)
        glEnd()
        glPopMatrix()

class Planeta2:
    def dibujar(self):
        #atmosfera
        glPushMatrix()
        glTranslate(0.0,1.775,0.0)
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1.0,0.0,0.0)
        glVertex3f(0.0,0.0,0.0)
        for x in range(361):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.0)
            glVertex3f(cos(angulo)*1.4,sin(angulo)*1.4,0.0)
        glEnd()
        glPopMatrix()
        #planeta
        glPushMatrix()
        glTranslate(0.0,1.775,0.0)
        glColor3f(0.5,0.0,0.)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo),sin(angulo),0.0)
        glEnd()
        glPopMatrix()