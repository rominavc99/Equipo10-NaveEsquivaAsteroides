from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import math

class Nave:
    posX = 0.0
    posY = -0.8
    velocidad = 0.4

    colisionador = False

    def actualizar(self, window, deltatime):
        estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)
        estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
        estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
        estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)

        if estado_tecla_izquierda == glfw.PRESS:
            self.posX = self.posX - self.velocidad * deltatime
        if estado_tecla_derecha == glfw.PRESS:
            self.posX = self.posX + self.velocidad * deltatime
        if estado_tecla_abajo == glfw.PRESS:
            self.posY = self.posY - self.velocidad * deltatime
        if estado_tecla_arriba == glfw.PRESS:
            self.posY = self.posY + self.velocidad * deltatime

    def checar_colision_asteroide(self, asteroide1, asteroide2, asteroide3, asteroide4, asteroide5, asteroide6, asteroide7, asteroide8):
        if self.posX + 0.0175 > asteroide1.posX - 0.035 and self.posX - 0.0175 < asteroide1.posX + 0.035 and self.posY + 0.035 > asteroide1.posY - 0.035 and self.posY - 0.035 < asteroide1.posY + 0.035:
            self.colisionador = True
        elif self.posX + 0.0175 > asteroide2.posX - 0.035 and self.posX - 0.0175 < asteroide2.posX + 0.035 and self.posY + 0.035 > asteroide2.posY - 0.035 and self.posY - 0.035 < asteroide2.posY + 0.035:
            self.colisionador = True
        elif self.posX + 0.0175 > asteroide3.posX - 0.035 and self.posX - 0.0175 < asteroide3.posX + 0.035 and self.posY + 0.035 > asteroide3.posY - 0.035 and self.posY - 0.035 < asteroide3.posY + 0.035:
            self.colisionador = True
        elif self.posX + 0.0175 > asteroide4.posX - 0.035 and self.posX - 0.0175 < asteroide4.posX + 0.035 and self.posY + 0.035 > asteroide4.posY - 0.035 and self.posY - 0.035 < asteroide4.posY + 0.035:
            self.colisionador = True
        elif self.posX + 0.0175 > asteroide5.posX - 0.035 and self.posX - 0.0175 < asteroide5.posX + 0.035 and self.posY + 0.035 > asteroide5.posY - 0.035 and self.posY - 0.035 < asteroide5.posY + 0.035:
            self.colisionador = True
        elif self.posX + 0.0175 > asteroide6.posX - 0.035 and self.posX - 0.0175 < asteroide6.posX + 0.035 and self.posY + 0.035 > asteroide6.posY - 0.035 and self.posY - 0.035 < asteroide6.posY + 0.035:
            self.colisionador = True
        elif self.posX + 0.0175 > asteroide7.posX - 0.035 and self.posX - 0.0175 < asteroide7.posX + 0.035 and self.posY + 0.035 > asteroide7.posY - 0.035 and self.posY - 0.035 < asteroide7.posY + 0.035:
            self.colisionador = True
        elif self.posX + 0.0175 > asteroide8.posX - 0.035 and self.posX - 0.0175 < asteroide8.posX + 0.035 and self.posY + 0.035 > asteroide8.posY - 0.035 and self.posY - 0.035 < asteroide8.posY + 0.035:
            self.colisionador = True
        else:
            self.colisionador = False

    def checar_colision_satelite(self, satelite1, satelite2, satelite3):
        if self.posX + 0.0175 > satelite1.posX - 0.035 and self.posX - 0.0175 < satelite1.posX + 0.035 and self.posY + 0.035 > satelite1.posY - 0.035 and self.posY - 0.035 < satelite1.posY + 0.035:
            self.colisionador = True
        elif self.posX + 0.0175 > satelite2.posX - 0.035 and self.posX - 0.0175 < satelite2.posX + 0.035 and self.posY + 0.035 > satelite2.posY - 0.035 and self.posY - 0.035 < satelite2.posY + 0.035:
            self.colisionador = True
        elif self.posX + 0.0175 > satelite3.posX - 0.035 and self.posX - 0.0175 < satelite3.posX + 0.035 and self.posY + 0.035 > satelite3.posY - 0.035 and self.posY - 0.035 < satelite3.posY + 0.035:
            self.colisionador = True
        else:
            self.colisionador = False

    def checar_colision_ufo(self, ufo1, ufo2, ufo3):
        if self.posX + 0.0175 > ufo1.posX - 0.035 and self.posX - 0.0175 < ufo1.posX + 0.035 and self.posY + 0.035 > ufo1.posY - 0.0175 and self.posY - 0.035 < ufo1.posY + 0.0175:
            self.colisionador = True
        elif self.posX + 0.0175 > ufo2.posX - 0.035 and self.posX - 0.0175 < ufo2.posX + 0.035 and self.posY + 0.035 > ufo2.posY - 0.0175 and self.posY - 0.035 < ufo2.posY + 0.0175:
            self.colisionador = True
        elif self.posX + 0.0175 > ufo3.posX - 0.035 and self.posX - 0.0175 < ufo3.posX + 0.035 and self.posY + 0.035 > ufo3.posY - 0.0175 and self.posY - 0.035 < ufo3.posY + 0.0175:
            self.colisionador = True
        else:
            self.colisionador = False
    
    def checar_colision_borde(self):
        if self.posX > 1.0:
            self.colisionador = True
        elif self.posX < -1.0:
            self.colisionador = True
        elif self.posY > 0.8:
            self.colisionador = True
        elif self.posY < -0.9:
            self.colisionador = True
        else:
            self.colisionador = False

    def dibujar(self):
        glPushMatrix()
        glTranslate(self.posX, self.posY, 0)
        glScalef(0.035,0.035,0.035)
        glColor3f(1.0,1.0,1.0)
        glBegin(GL_POLYGON)
        glVertex3f(0.0,1.0,0.0)
        glVertex3f(0.4,0.4,0.0)
        glVertex3f(0.4,-0.4,0)
        glVertex3f(-0.4,-0.4,0)
        glVertex3f(-0.4,0.4,0.0)
        glEnd()
        glColor3f(0.8,0.0,0.0)
        glBegin(GL_TRIANGLES)
        glVertex3f(-0.4,-0.2,0.0)
        glVertex3f(0.0,-0.4,0.0)
        glVertex3f(-0.6,-1.0,0.0)
        glVertex3f(0.4,-0.2,0.0)
        glVertex3f(0.0,-0.4,0.0)
        glVertex3f(0.6,-1.0,0.0)
        glEnd()
        glColor3f(0.7,0.9,1.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.3,sin(angulo)*0.3+0.3,0.0)
        glEnd()
        glColor3f(1.0,1.0,1.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.3,sin(angulo)*0.3+0.1,0.0)
        glEnd()
        glPopMatrix()