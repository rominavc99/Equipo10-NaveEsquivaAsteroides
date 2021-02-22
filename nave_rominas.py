from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import math
import sys

colisionador = False
#Nave
posX_nave = 0.0
posY_nave = -0.8
velocidad_nave = 0.4

#Decoracion
#cometa1
posX_cometa1 = -1.3
posY_cometa1 = 0.4
velocidadX_cometa1 = 0.75
velocidadY_cometa1 = -0.15
angulo_cometa1 = math.degrees(math.atan(velocidadY_cometa1 / velocidadX_cometa1))
#cometa2
posX_cometa2 = -1.3
posY_cometa2 = 0.2
velocidadX_cometa2 = 0.5
velocidadY_cometa2 = -0.1
angulo_cometa2 = math.degrees(math.atan(velocidadY_cometa2 / velocidadX_cometa2))
#cometa3
posX_cometa3 = -1.3
posY_cometa3 = 0.0
velocidadX_cometa3 = 1.0
velocidadY_cometa3 = -0.2
angulo_cometa3 = math.degrees(math.atan(velocidadY_cometa3 / velocidadX_cometa3))

#obstaculos
#asteroide1
posX_asteroide1 = 0.0
posY_asteroide1 = -0.6
velocidad_asteroide1 = 1.0

#asteroide2
posX_asteroide2 = -0.5
posY_asteroide2 = -0.4
velocidad_asteroide2 = 1.0
#asteroide3
posX_asteroide3 = 0.5
posY_asteroide3 = -0.4
velocidad_asteroide3 = 1.0

#satelite1
posX_satelite1 = -0.6
posY_satelite1 = -0.2
velocidad_satelite1 = 1.2
#satelite2
posX_satelite2 = 0.0
posY_satelite2 = -0.2
velocidad_satelite2 = 1.2
#satelite3
posX_satelite3 = 0.6
posY_satelite3 = -0.2
velocidad_satelite3 = 1.2

#asteroide4
posX_asteroide4 = -0.5
posY_asteroide4 = 0.0
velocidad_asteroide4 = 1.2
#asteroide5
posX_asteroide5 = 0.5
posY_asteroide5 = 0.0
velocidad_asteroide5 = 1.2

#ufo1
posX_ufo1 = 0.0
posY_ufo1 = 0.2
velocidad_ufo1 = 2.0

#asteroide6
posX_asteroide6 = -0.6
posY_asteroide6 = 0.4
velocidad_asteroide6 = 1.5
#asteroide7
posX_asteroide7 = 0.0
posY_asteroide7 = 0.4
velocidad_asteroide7 = 1.5
#asteroide8
posX_asteroide8 = 0.6
posY_asteroide8 = 0.4
velocidad_asteroide8 = 1.5

#ufo2
posX_ufo2 = -0.5
posY_ufo2 = 0.6
velocidad_ufo2 = 2.5
#ufo3
posX_ufo3 = 0.5
posY_ufo3 = 0.6
velocidad_ufo3 = 2.5

#Tiempo
tiempo = 0.0
tiempoAnterior = 0.0

def checar_colisiones():
    #global posX_asteroide1
    #global posY_asteroide1
    #global posX_nave
    #global posY_nave
    global colisionador

    #si extremaDerechaCarrito > extremaIzquierdaObstaculo 
    #Y extremaIzquierdaCarrito < extremaIzquierdaObstaculo 
    #Y extremaSuperiorCarrito > extremaInferiorObstaculo
    #Y extremaInferiorCarrito < extremaSuperiorObstaculo
    if posX_nave + 0.0175 > posX_asteroide1 - 0.035 and posX_nave - 0.0175 < posX_asteroide1 + 0.035 and posY_nave + 0.035 > posY_asteroide1 - 0.035 and posY_nave - 0.035 < posY_asteroide1 + 0.035:
        colisionador = True
    elif posX_nave + 0.0175 > posX_asteroide2 - 0.035 and posX_nave - 0.0175 < posX_asteroide2 + 0.035 and posY_nave + 0.035 > posY_asteroide2 - 0.035 and posY_nave - 0.035 < posY_asteroide2 + 0.035:
        colisionador = True
    elif posX_nave + 0.0175 > posX_asteroide3 - 0.035 and posX_nave - 0.0175 < posX_asteroide3 + 0.035 and posY_nave + 0.035 > posY_asteroide3 - 0.035 and posY_nave - 0.035 < posY_asteroide3 + 0.035:
        colisionador = True
    elif posX_nave + 0.0175 > posX_asteroide4 - 0.035 and posX_nave - 0.0175 < posX_asteroide4 + 0.035 and posY_nave + 0.035 > posY_asteroide4 - 0.035 and posY_nave - 0.035 < posY_asteroide4 + 0.035:
        colisionador = True
    elif posX_nave + 0.0175 > posX_asteroide5 - 0.035 and posX_nave - 0.0175 < posX_asteroide5 + 0.035 and posY_nave + 0.035 > posY_asteroide5 - 0.035 and posY_nave - 0.035 < posY_asteroide5 + 0.035:
        colisionador = True
    elif posX_nave + 0.0175 > posX_asteroide6 - 0.035 and posX_nave - 0.0175 < posX_asteroide6 + 0.035 and posY_nave + 0.035 > posY_asteroide6 - 0.035 and posY_nave - 0.035 < posY_asteroide6 + 0.035:
        colisionador = True
    elif posX_nave + 0.0175 > posX_asteroide7 - 0.035 and posX_nave - 0.0175 < posX_asteroide7 + 0.035 and posY_nave + 0.035 > posY_asteroide7 - 0.035 and posY_nave - 0.035 < posY_asteroide7 + 0.035:
        colisionador = True
    elif posX_nave + 0.0175 > posX_asteroide8 - 0.035 and posX_nave - 0.0175 < posX_asteroide8 + 0.035 and posY_nave + 0.035 > posY_asteroide8 - 0.035 and posY_nave - 0.035 < posY_asteroide8 + 0.035:
        colisionador = True
    elif posX_nave + 0.0175 > posX_satelite1 - 0.035 and posX_nave - 0.0175 < posX_satelite1 + 0.035 and posY_nave + 0.035 > posY_satelite1 - 0.035 and posY_nave - 0.035 < posY_satelite1 + 0.035:
        colisionador = True
    elif posX_nave + 0.0175 > posX_satelite2 - 0.035 and posX_nave - 0.0175 < posX_satelite2 + 0.035 and posY_nave + 0.035 > posY_satelite2 - 0.035 and posY_nave - 0.035 < posY_satelite2 + 0.035:
        colisionador = True
    elif posX_nave + 0.0175 > posX_satelite3 - 0.035 and posX_nave - 0.0175 < posX_satelite3 + 0.035 and posY_nave + 0.035 > posY_satelite3 - 0.035 and posY_nave - 0.035 < posY_satelite3 + 0.035:
        colisionador = True
    elif posX_nave + 0.0175 > posX_ufo1 - 0.035 and posX_nave - 0.0175 < posX_ufo1 + 0.035 and posY_nave + 0.035 > posY_ufo1 - 0.0175 and posY_nave - 0.035 < posY_ufo1 + 0.0175:
        colisionador = True
    elif posX_nave + 0.0175 > posX_ufo2 - 0.035 and posX_nave - 0.0175 < posX_ufo2 + 0.035 and posY_nave + 0.035 > posY_ufo2 - 0.0175 and posY_nave - 0.00351 < posY_ufo2 + 0.0175:
        colisionador = True
    elif posX_nave + 0.0175 > posX_ufo3 - 0.035 and posX_nave - 0.0175 < posX_ufo3 + 0.035 and posY_nave + 0.035 > posY_ufo3 - 0.0175 and posY_nave - 0.035 < posY_ufo3 + 0.0175:
        colisionador = True
    elif posX_nave + 0.0175 > - 0.4 and posX_nave - 0.0175 < + 0.4 and posY_nave > 0.8:
        colisionador = True
    else:
        colisionador = False

def actualizar(window):
    global tiempo
    global tiempoAnterior
    
    #nave
    global posX_nave
    global posY_nave
    global velocidad_nave

    #asteroides
    global posX_asteroide1
    global velocidad_asteroide1
    global posX_asteroide2
    global velocidad_asteroide2
    global posX_asteroide3
    global velocidad_asteroide3
    global posX_asteroide4
    global velocidad_asteroide4
    global posX_asteroide5
    global velocidad_asteroide5
    global posX_asteroide6
    global velocidad_asteroide6
    global posX_asteroide7
    global velocidad_asteroide7
    global posX_asteroide8
    global velocidad_asteroide8
    #satelites
    global posX_satelite1
    global velocidad_satelite1
    global posX_satelite2
    global velocidad_satelite2
    global posX_satelite3
    global velocidad_satelite3
    #ufos
    global posX_ufo1
    global velocidad_ufo1
    global posX_ufo2
    global velocidad_ufo2
    global posX_ufo3
    global velocidad_ufo3
    #cometas
    global posX_cometa1
    global posY_cometa1
    global velocidadX_cometa1
    global velocidadY_cometa1
    global angulo_cometa1
    global posX_cometa2
    global posY_cometa2
    global velocidadX_cometa2
    global velocidadY_cometa2
    global posX_cometa3
    global posY_cometa3
    global velocidadX_cometa3
    global velocidadY_cometa3

    #Tiempo
    tiempo = glfw.get_time()
    deltatime = tiempo - tiempoAnterior
    movimiento = velocidad_nave * deltatime

    #Movimientos
    posX_asteroide1 = posX_asteroide1 + velocidad_asteroide1 * deltatime
    if posX_asteroide1 > 1.3:
        posX_asteroide1 = -1.3
    posX_asteroide2 = posX_asteroide2 + velocidad_asteroide2 * deltatime
    if posX_asteroide2 > 1.3:
        posX_asteroide2 = -1.3
    posX_asteroide3 = posX_asteroide3 + velocidad_asteroide3 * deltatime
    if posX_asteroide3 > 1.3:
        posX_asteroide3 = -1.3
    posX_asteroide4 = posX_asteroide4 + velocidad_asteroide4 * deltatime
    if posX_asteroide4 > 1.3:
        posX_asteroide4 = -1.3
    posX_asteroide5 = posX_asteroide5 + velocidad_asteroide5 * deltatime
    if posX_asteroide5 > 1.3:
        posX_asteroide5 = -1.3
    posX_asteroide6 = posX_asteroide6 + velocidad_asteroide6 * deltatime
    if posX_asteroide6 > 1.3:
        posX_asteroide6 = -1.3
    posX_asteroide7 = posX_asteroide7 + velocidad_asteroide7 * deltatime
    if posX_asteroide7 > 1.3:
        posX_asteroide7 = -1.3
    posX_asteroide8 = posX_asteroide8 + velocidad_asteroide8 * deltatime
    if posX_asteroide8 > 1.3:
        posX_asteroide8 = -1.3

    posX_satelite1 = posX_satelite1 + velocidad_satelite1 * deltatime
    if posX_satelite1 > 1.3:
        posX_satelite1 = -1.3
    posX_satelite2 = posX_satelite2 + velocidad_satelite2 * deltatime
    if posX_satelite2 > 1.3:
        posX_satelite2 = -1.3
    posX_satelite3 = posX_satelite3 + velocidad_satelite3 * deltatime
    if posX_satelite3 > 1.3:
        posX_satelite3 = -1.3

    posX_ufo1 = posX_ufo1 + velocidad_ufo1 * deltatime
    if posX_ufo1 > 1.3:
        posX_ufo1 = -1.3
    posX_ufo2 = posX_ufo2 + velocidad_ufo2 * deltatime
    if posX_ufo2 > 1.3:
        posX_ufo2 = -1.3
    posX_ufo3 = posX_ufo3 + velocidad_ufo1 * deltatime
    if posX_ufo3 > 1.3:
        posX_ufo3 = -1.3

    posX_cometa1 = posX_cometa1 + velocidadX_cometa1 * deltatime
    posY_cometa1 = posY_cometa1 + velocidadY_cometa1 * deltatime
    if posX_cometa1 > 1.3:
        posX_cometa1 = -1.3
        posY_cometa1 = 0.4
    posX_cometa2 = posX_cometa2 + velocidadX_cometa2 * deltatime
    posY_cometa2 = posY_cometa2 + velocidadY_cometa2 * deltatime
    if posX_cometa2 > 1.3:
        posX_cometa2 = -1.3
        posY_cometa2 = 0.2
    posX_cometa3 = posX_cometa3 + velocidadX_cometa3 * deltatime
    posY_cometa3 = posY_cometa3 + velocidadY_cometa3 * deltatime
    if posX_cometa3 > 1.3:
        posX_cometa3 = -1.3
        posY_cometa3 = 0.0

    estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)

    if estado_tecla_izquierda == glfw.PRESS:
        posX_nave = posX_nave - velocidad_nave * deltatime
    if estado_tecla_derecha == glfw.PRESS:
        posX_nave = posX_nave + velocidad_nave * deltatime
    if estado_tecla_abajo == glfw.PRESS:
        posY_nave = posY_nave - velocidad_nave * deltatime
    if estado_tecla_arriba == glfw.PRESS:
        posY_nave = posY_nave + velocidad_nave * deltatime

    tiempoAnterior = tiempo
    checar_colisiones()

#Dibujo

def dibujarCometas():
    global posX_cometa1
    global posY_cometa1
    global angulo_cometa1
    global posX_cometa2
    global posY_cometa2
    global angulo_cometa2
    global posX_cometa3
    global posY_cometa3
    global angulo_cometa3

    #cometa1
    glPushMatrix()
    glTranslate(posX_cometa1,posY_cometa1,0.0)
    glRotatef(angulo_cometa1,0,0,1)
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

    #cometa2
    glPushMatrix()
    glTranslate(posX_cometa2,posY_cometa2,0.0)
    glRotatef(angulo_cometa2,0,0,1)
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

    #cometa3
    glPushMatrix()
    glTranslate(posX_cometa3,posY_cometa3,0.0)
    glRotatef(angulo_cometa3,0,0,1)
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
   
def dibujarPlanetas():
    #atmosfera1
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
    #planeta1
    glPushMatrix()
    glTranslate(0.0,-1.775,0.0)
    glColor3f(0.0,0.0,0.5)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo),0.0)
    glEnd()
    glPopMatrix()

    #atmosfera2
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
    #planeta2
    glPushMatrix()
    glTranslate(0.0,1.775,0.0)
    glColor3f(0.5,0.0,0.)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo),0.0)
    glEnd()
    glPopMatrix()

def dibujarNave():
    global posX_nave
    global posY_nave
    glPushMatrix()
    glTranslate(posX_nave, posY_nave, 0)
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

def dibujarSatelites():
    global posX_satelite1
    global posY_satelite1
    global posX_satelite2
    global posY_satelite2
    global posX_satelite3
    global posY_satelite3

    #Satelite1
    glPushMatrix()
    glTranslatef(posX_satelite1,posY_satelite1,0)
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

    #Satelite2
    glPushMatrix()
    glTranslatef(posX_satelite2,posY_satelite2,0)
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
    glTranslatef(posX_satelite2,posY_satelite2,0)
    glScalef(0.035,0.035,0.035)
    glRotate(-30,0,0,1)
    glColor3f(0.9,0.9,0.9)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.6,sin(angulo)*0.3,0.0)
    glEnd()
    glPopMatrix()

    #Satelite3
    glPushMatrix()
    glTranslatef(posX_satelite3,posY_satelite3,0)
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
    
def dibujarUfos():
    global posX_ufo1
    global posY_ufo1
    global posX_ufo2
    global posY_ufo2
    global posX_ufo3
    global posY_ufo3

    #UFO1
    glPushMatrix()
    glTranslatef(posX_ufo1,posY_ufo1,0)
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

    #UFO2
    glPushMatrix()
    glTranslatef(posX_ufo2,posY_ufo2,0)
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
    
    #UFO3
    glPushMatrix()
    glTranslatef(posX_ufo3,posY_ufo3,0)
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

def dibujarAsteroides():
    global posX_asteroide1
    global posY_asteroide1
    global posX_asteroide2
    global posY_asteroide2
    global posX_asteroide3
    global posY_asteroide3
    global posX_asteroide4
    global posY_asteroide4
    global posX_asteroide5
    global posY_asteroide5
    global posX_asteroide6
    global posY_asteroide6
    global posX_asteroide7
    global posY_asteroide7
    global posX_asteroide8
    global posY_asteroide8

    #Asteroide1
    glPushMatrix()
    glTranslatef(posX_asteroide1,posY_asteroide1,0)
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

    #Asteroide2
    glPushMatrix()
    glTranslatef(posX_asteroide2,posY_asteroide2,0)
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

    #Asteroide3
    glPushMatrix()
    glTranslatef(posX_asteroide3,posY_asteroide3,0)
    glScalef(0.035,0.035,0.035)
    glColor3f(0.5,0.5,0.5)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo)*0.77,0.0)
    glEnd()
    glPopMatrix()

    #Asteroide4
    glPushMatrix()
    glTranslatef(posX_asteroide4,posY_asteroide4,0)
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

    #Asteroide5
    glPushMatrix()
    glTranslatef(posX_asteroide5,posY_asteroide5,0)
    glScalef(0.035,0.035,0.035)
    glRotate(45,0,0,1)
    glColor3f(0.5,0.5,0.5)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo)*0.6,0.0)
    glEnd()
    glPopMatrix()

    #Asteroide6
    glPushMatrix()
    glTranslatef(posX_asteroide6,posY_asteroide6,0)
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

    #Asteroide7
    glPushMatrix()
    glTranslatef(posX_asteroide7,posY_asteroide7,0)
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

    #Asteroide8
    glPushMatrix()
    glTranslatef(posX_asteroide8,posY_asteroide8,0)
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

def dibujar():
    dibujarCometas()
    dibujarPlanetas()
    dibujarAsteroides()
    dibujarSatelites()
    dibujarUfos()
    dibujarNave()

def key_callback(window, key, scancode, action, mods):
    global posX_nave
    global posY_nave
    
    #Escape
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, 1)
    
    if action == glfw.PRESS or action == glfw.REPEAT:
        #MovX
        if key == glfw.KEY_LEFT:
            posX_triangle = posX_triangle - 0.05
        if key == glfw.KEY_RIGHT:
            posX_triangle = posX_triangle + 0.05
    
        #MovY
        if key == glfw.KEY_UP:
            posY_triangle = posY_triangle + 0.05
        if key == glfw.KEY_DOWN:
            posY_triangle = posY_triangle - 0.05

def main():
    global tiempo
    global tiempoAnterior
    global colisionador
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(1000,1000,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    #Establecer callback de evento de teclado
    #glfw.set_key_callback(window, key_callback)
    tiempo = glfw.get_time()
    tiempoAnterior = glfw.get_time()
    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,1000,1000)
        #Establece color de borrado
        glClearColor(0.0,0.0,0.0,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Actualizar valores de la app
        actualizar(window)
        #Dibujar
        dibujar()

        if colisionador == True:
            sys.exit()
        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()