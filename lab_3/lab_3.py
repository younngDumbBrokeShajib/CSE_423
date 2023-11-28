from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

import math

#first initialize the radius
#then we will add the radius with the center to get the first point

radius=30
speed=1

X,Y=-200,200

class point:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def MidpointCircle(radius, x0, y0):
    d = 1 - radius
    x = 0
    y = radius

    Circlepoints(x, y, x0 ,y0)
    while (x < y):
        if (d < 0):
            #choose E
            d = d + 2*x + 3
            x = x + 1
        else:
            # choose SE
            d = d + 2*x - 2*y + 5
            x = x + 1
            y = y - 1
        Circlepoints(x,y,x0,y0)

def Circlepoints(x, y, x0, y0):

    draw_points(x + x0, y + y0)
    draw_points(y + y0, x + x0)
    draw_points(y + y0, -x + x0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + y0, -x + x0)
    draw_points(-y + y0, x + x0)
    draw_points(-x + x0, y + y0)



def specialKeyListener(key, x, y):
    global speed
    if key=='w':
        print(1)
    if key==GLUT_KEY_LEFT:
        if(speed>1):
            speed=speed-1
        print("Speed decreased")
    if key== GLUT_KEY_RIGHT:		#// up arrow key
        speed+=1
        print("Speed Increased")
    glutPostRedisplay()


def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)
    global radius,X,Y
    MidpointCircle(radius,X,Y)

    glBegin(GL_LINES)
    glVertex2d(180,0)
    glVertex2d(180,180)
    glVertex2d(180,180)
    glVertex2d(0,180)
    glEnd()
    glutSwapBuffers()

def animate():
    global radius,speed
    for i in range(0,10):
        radius=radius+speed


def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance



glutInit()
glutInitWindowSize(500,500)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()
glutDisplayFunc(display)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutMainLoop()	
	#The main loop of OpenGL
