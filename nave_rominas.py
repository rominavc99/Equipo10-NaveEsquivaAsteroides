from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import math
import sys

from Nave import *
from Asteroide import *
from Satelite import * 
from UFO import *
from Cometa import *
from Planeta import *

#Jugador
nave = Nave()

#Obstaculos
asteroide1 = Asteroide1()
asteroide2 = Asteroide2()
asteroide3 = Asteroide3()
asteroide4 = Asteroide4()
asteroide5 = Asteroide5()
asteroide6 = Asteroide6()
asteroide7 = Asteroide7()
asteroide8 = Asteroide8()

satelite1 = Satelite1()
satelite2 = Satelite2()
satelite3 = Satelite3()

ufo1 = UFO1()
ufo2 = UFO2()
ufo3 = UFO3()

#Decoracion
cometa1 = Cometa1()
cometa2 = Cometa2()
cometa3 = Cometa3()

planeta1 = Planeta1()
planeta2 = Planeta2()

#Tiempo
tiempo = 0.0
tiempoAnterior = 0.0

def actualizar(window):
    global tiempo
    global tiempoAnterior
    global nave
    global asteroide1
    global asteroide2
    global asteroide3
    global asteroide4
    global asteroide5
    global asteroide6
    global asteroide7
    global asteroide8
    global satelite1
    global satelite2
    global satelite3
    global ufo1
    global ufo2
    global ufo3
    global cometa1
    global cometa2
    global cometa3

    #Tiempo
    tiempo = glfw.get_time()
    deltatime = tiempo - tiempoAnterior

    #Movimientos
    nave.actualizar(window, deltatime)

    asteroide1.actualizar(deltatime)
    asteroide2.actualizar(deltatime)
    asteroide3.actualizar(deltatime)
    asteroide4.actualizar(deltatime)
    asteroide5.actualizar(deltatime)
    asteroide6.actualizar(deltatime)
    asteroide7.actualizar(deltatime)
    asteroide8.actualizar(deltatime)

    satelite1.actualizar(deltatime)
    satelite2.actualizar(deltatime)
    satelite3.actualizar(deltatime)

    ufo1.actualizar(deltatime)
    ufo2.actualizar(deltatime)
    ufo3.actualizar(deltatime)

    cometa1.actualizar(deltatime)
    cometa2.actualizar(deltatime)
    cometa3.actualizar(deltatime)

    nave.checar_colision_asteroide(asteroide1, asteroide2, asteroide3, asteroide4, asteroide5, asteroide6, asteroide7, asteroide8)
    if not nave.colisionador:
        nave.checar_colision_satelite(satelite1, satelite2, satelite3)
        if not nave.colisionador:
            nave.checar_colision_ufo(ufo1, ufo2, ufo3)
            if not nave.colisionador:
                nave.checar_colision_borde()

    tiempoAnterior = tiempo

#Dibujo    
def dibujar():
    global nave
    global asteroide1
    global asteroide2
    global asteroide3
    global asteroide4
    global asteroide5
    global asteroide6
    global asteroide7
    global asteroide8
    global satelite1
    global satelite2
    global satelite3
    global ufo1
    global ufo2
    global ufo3
    global cometa1
    global cometa2
    global cometa3
    global planeta1
    global planeta2

    cometa1.dibujar()
    cometa2.dibujar()
    cometa3.dibujar()

    planeta1.dibujar()
    planeta2.dibujar()

    asteroide1.dibujar()
    asteroide2.dibujar()
    asteroide3.dibujar()
    asteroide4.dibujar()
    asteroide5.dibujar()
    asteroide6.dibujar()
    asteroide7.dibujar()
    asteroide8.dibujar()

    satelite1.dibujar()
    satelite2.dibujar()
    satelite3.dibujar()

    ufo1.dibujar()
    ufo2.dibujar()
    ufo3.dibujar()

    nave.dibujar()
    
def key_callback(window, key, scancode, action, mods):
    global nave

    #Escape
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, 1)
    
    if action == glfw.PRESS or action == glfw.REPEAT:
        #MovX
        if key == glfw.KEY_LEFT:
            nave.posX = nave.posX - 0.05
        if key == glfw.KEY_RIGHT:
            nave.posX = nave.posX + 0.05
    
        #MovY
        if key == glfw.KEY_UP:
            nave.posY = nave.posY + 0.05
        if key == glfw.KEY_DOWN:
            nave.posY = nave.posY - 0.05

def main():
    global tiempo
    global tiempoAnterior
    global nave
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

        if nave.colisionador == True:
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