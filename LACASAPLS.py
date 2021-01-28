from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *


#Una casa que contenga:
#techo
#una ventana
#una puerta con manija
#Cielo
#Pasto
#3 nubes
#Sol con rayos
#1 arbol
#    glColor3f(0.0, 0.7, 1.5)

# glColor3f(.5,0,5)
#glColor3f(2.5,2,0)


def Casita():

    
    #pasto
    glColor3f(0.0, 0.7, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(-1.0,-0.6,0.0)
    glVertex3f(1.0,-0.05,0.0)
    glVertex3f(1.0,-1.5,0.0)
    glVertex3f(-1.0,-1.0,0.0)
    glEnd()
 
    #casa
    glColor3f(0.2,0,0.1)
    glBegin(GL_QUADS)
    glVertex3f(-0.4,-0.5,0.0)
    glVertex3f(0.4,-0.5,0.0)
    glVertex3f(0.4,0.2,0.0)
    glVertex3f(-0.4,0.2,0.0)
    glEnd()

    #pintura

    glColor3f(0.6,0.25,0.1)
    glBegin(GL_QUADS)
    glVertex3f(-0.2,-0.5,0.0)
    glVertex3f(0.2,-0.5,0.0)
    glVertex3f(0.4,0.2,0.0)
    glVertex3f(-0.4,0.2,0.0)
    glEnd()


    

    #puerta
    glColor3f(0.1, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(-0.1,-0.5,0.0)
    glVertex3f(0.2,-0.5,0.0)
    glVertex3f(0.2,-0.2,0.0)
    glVertex3f(-0.1,-0.2,0.0)
    glEnd()

    #Manija
    glColor3f(20, 0.01, 0.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.05 + 0.13 ,sin (angulo) *0.04 - 0.4,0.0)
    glEnd()

    #Ventana
    glColor3f(0.7,1,5)
    glBegin(GL_QUADS)
    glVertex3f(0.0,-0.1,0.0)
    glVertex3f(0.25,-0.1,0.0)
    glVertex3f(0.25,0.1,0.0)
    glVertex3f(0.0,0.1,0.0)
    glEnd()

    glColor3f(0.2,1,5)
    glBegin(GL_QUADS)
    glVertex3f(0.01,-0.1,0.0)
    glVertex3f(0.23,-0.1,0.0)
    glVertex3f(0.23,0.1,0.0)
    glVertex3f(0.01,0.1,0.0)
    glEnd()


    
    

 
def Techo():
    glColor3f(0.5,0.2,0.1)
    glBegin(GL_TRIANGLES)
    glVertex3f(-.7,0.2,0.0)
    glVertex3f(0.0,0.5,0.0)
    glVertex3f(.7,0.2,0.0)
    glEnd()

    
    
def Nubes1():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 - 0.1 ,sin(angulo) * 0.07 + 0.75,0.0)
    glEnd()
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 - 0.2 ,sin(angulo) * 0.05 + 0.72,0.0)
    glEnd()
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 - 0.02 ,sin(angulo) * 0.05 + 0.72,0)
    glEnd()

def Nubes2():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 + 0.3 ,sin(angulo) * 0.06 + 0.42,0.0)
    glEnd()
    
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 + 0.4 ,sin(angulo) * 0.04 + 0.4,0.0)
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 + 0.22 ,sin(angulo) * 0.04 + 0.4,0.0)
    glEnd()

def Nubes3():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 + 0.6 ,sin(angulo) * 0.05 + 0.65 ,0.0)
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 + 0.5 ,sin(angulo) * 0.05 + 0.62 ,0.0)
    glEnd()

def Sol():
    glColor3f(2,2.2,0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 - 0.70 ,sin(angulo) * 0.13 + 0.7,0.0)
    glEnd()

def Rayos():
    glBegin(GL_TRIANGLES)
    glColor3f(0.9,0.8,0.05)
    glVertex3f(-0.95,0.7,0.0)
    glVertex3f(-0.7,0.9,0.0)
    glVertex3f(-0.45,0.7,0.0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.9,0.8,0.05)
    glVertex3f(-0.82,0.9,0.0)
    glVertex3f(-0.52,0.85,0.0)
    glVertex3f(-0.55,0.5,0.0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.9,0.8,0.05)
    glVertex3f(-0.95,0.7,0.0)
    glVertex3f(-0.7,0.45,0.0)
    glVertex3f(-0.45,0.7,0.0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.9,0.8,0.05)
    glVertex3f(-0.82,0.9,0.0)
    glVertex3f(-0.9,0.55,0.0)
    glVertex3f(-0.55,0.5,0.0)
    glEnd()

def Arbol():

    #tronco exdi
    glColor3f(0.7,0.3,0.1)
    glBegin(GL_QUADS)
    
    glVertex3f(-0.7,-0.4,0.0)
    glVertex3f(-0.5,-0.6,0.0)
    glVertex3f(-0.5,-0.2,0.0)
    glVertex3f(-0.7,-0.2,0.0)
    glEnd()

    glColor3f(0.7,0.3,0.1)
    glBegin(GL_QUADS)
    glVertex3f(-0.7,-0.6,0.0)
    glVertex3f(-0.5,-0.6,0.0)
    glVertex3f(-0.5,-0.2,0.0)
    glVertex3f(-0.7,-0.2,0.0)
    glEnd()

    glColor3f(0.0, 0.7, 0.0)
    glBegin(GL_POLYGON)   

    #casa exdi
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 - 0.5 ,sin(angulo) * 0.15 - 0.15,0.0)
    glEnd()

    glColor3f(0.0, 0.7, 0.0)
    glBegin(GL_POLYGON)                     
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.7 ,sin(angulo) * 0.15 - 0.1,0.0)
    glEnd()

    glColor3f(0.0, 0.7, 0.0)
    glBegin(GL_POLYGON)                     
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 - 0.75 ,sin(angulo) * 0.15 + 0.07 ,0.0)
    glEnd()
    
    glColor3f(0.0, 0.7, 0.0)
    glBegin(GL_POLYGON)                     
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 - 0.6 ,sin(angulo) * 0.15 + 0.07 ,0.0)
    glEnd()

    glColor3f(0.0, 0.7, 0.0)
    glBegin(GL_POLYGON)                     
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.05 - 0.6 ,sin(angulo) * 0.15 + 0.07 ,0.0)
    glEnd()




def dibujar():
      
    Arbol()
    Casita()
    Techo()
    Nubes1()
    Nubes2()
    Nubes3()
    Rayos()
    Sol()
    
    
    #dibujarTriangulos()
    #dibujarPuntos()
    #dibujarLineas()
    #dibujarLineasContinuas()
    #dibujarCicloLinea()
    #dibujarRectangulos()


def main():
    #inicia glfw
    ancho = 600
    alto = 600
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(ancho,alto,"Mi ventana", None, None)

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

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,ancho,alto)
        #Establece color de borrado
        glClearColor(0.0,0.7,1,5)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

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
