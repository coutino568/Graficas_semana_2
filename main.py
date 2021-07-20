
import random
from gl import Renderer

windoWidth = 1920*1
windowHeight = 1080*1
scale= 1
viewportWidth= windoWidth*scale
viewportHeight= windowHeight *scale
viewportX=0
viewportY=0



myRenderer = Renderer(windoWidth, windowHeight)
myRenderer.glViewPort(viewportX,viewportY,viewportWidth,viewportHeight)



def drawflag():
    for x in range(int(viewportWidth/3)):
        myRenderer.glColor(0,0.47,0.7)
        for y in range(int(viewportHeight)):
            myRenderer.glVertex(viewportX+x, viewportY+y)

    for x in range(int(viewportWidth/3)):
        myRenderer.glColor(0,0.47,0.7)
        for y in range(int(viewportHeight)):
            myRenderer.glVertex(viewportX+x+int(2*viewportWidth/3), viewportY+y)
    
#miwate flag
myRenderer.glColor(0.2,0.8,0.7)


#drawflag()
def abrstractForms():
    originX = windoWidth/2
    originY = windowHeight/2
    destinationX = random.randint(0,windoWidth)
    destinationY = random.randint(0,windowHeight)

    for i in range (20):
        scale = random.random()
        myRenderer.glColor(scale,0.7,0.8)
        sense = random.randint(-1,1)
        strokes= random.randint(20,70)
        for i in range (strokes):        
            myRenderer.glLine(originX,originY,sense*destinationX+(4*i),sense*destinationY-(4*i))
            if (i==49) :

                originX, originY = destinationX,destinationY
                destinationX = random.randint(0,windoWidth)
                destinationY = random.randint(0,windowHeight)



def cube(x,y,density=1):
    paint = myRenderer.glColor(random.random(),0.2,0.8)
    # integer.. the lower , the denser
    density =density

    for i in range (0,100,1):
        if (i%density==0):
            myRenderer.glLine(x,y+i,x-100,y+50+i)
       



    
    #myRenderer.glLine(x,y,x,y+100)
    myRenderer.glColor(random.random(),0.2,0.8)
    for i in range (0,100,1):
        if (i%density==0):
            myRenderer.glLine(x,y+i,x+100,y+50+i)
    #     myRenderer.glLine(x+i,y+(i/2),x+i,y+100+(i/2))

    myRenderer.glColor(random.random(),0.2,0.8)
    for i in range (0,100,1):
        if (i%density==0):
            myRenderer.glLine(x-100+i,y+150-(i/2),x+i,y+200-(i/2))
    
    myRenderer.glLine(x,y,x-100,y+50)
    myRenderer.glLine(x,y+100,x-100,y+150)
    
    myRenderer.glLine(x,y+100,x+100,y+150)

    

    myRenderer.glLine(x,y+200,x+100,y+150)


    cube2(x,y)




def cube2(x,y):
    myRenderer.glColor(random.random(),0.2,0.8)

    myRenderer.glLine(x-100,y+50,x-100,y+150)
    myRenderer.glLine(x,y,x,y+100)

    myRenderer.glLine(x+100,y+50,x+100,y+150)
    
    myRenderer.glLine(x,y,x-100,y+50)
    myRenderer.glLine(x,y+100,x-100,y+150)
    myRenderer.glLine(x,y,x+100,y+50)
    myRenderer.glLine(x,y+100,x+100,y+150)

    myRenderer.glLine(x-100,y+150,x,y+200)
    myRenderer.glLine(x,y+200,x+100,y+150)



def triangle(x0,y0,x1,y1,x2,y2):


    myRenderer.glLine(x0,y0,x1,y1)
    myRenderer.glLine(x1,y1,x2,y2)
    myRenderer.glLine(x0,y0,x2,y2)

     


cube(350,500)
cube(450,650,4)
cube(550,500,2)
cube(750,600,2)
cube(750,600)
cube(750,700)

cube(850,850)
cube(750,800)

def plane():
    myRenderer.glColor(random.random(),0.2,0.8)
    triangle(750,50,700,100,900,200)
    triangle(650,100,700,100,900,200)
    triangle(700,100,700,80,710,90)

plane()


def trapesoide(x,y,width,height):
    myRenderer.glColor(random.random(),0.2,0.8)
    myRenderer.glLine(x,y,x+width,y)
    myRenderer.glLine(x,y,x+(width/3),y+height)
    myRenderer.glLine(x+(2/3)*width,y+height,x+width,y)
    myRenderer.glLine(x+(width/3),y+height,x+(2/3)*width,y+height)




trapesoide(1200,200,700,400)

cube2(1550,600)

#myRenderer.show()
myRenderer.glFinish("output.bmp")