
import random

def setup():
    global currentScene,f,f2,RN,img_1,img_2,img_3,img_4,img_5,img_6, imglist, img
    f2 = createFont('Arial', 48, True)
    size(660,690)
    background(0)
    
    img_1 = loadImage("1.jpg")
    img_2 = loadImage("2.jpg")
    img_3 = loadImage("3.jpg")
    img_4 = loadImage("4.jpg")
    img_5 = loadImage("5.jpg")
    img_6 = loadImage("6.jpg")
    
    imglist = [img_1, img_2, img_3, img_4, img_5, img_6]
    
def draw():
    global currentScene,f,RN,f2,img,img_1,img_2,img_3,img_4,img_5,img_6, imglist, img
    
    
    textFont(f2,48)       
    fill(255)
    textAlign(CENTER)
    text("^",330,687)
    
def keyPressed():
    import random
    global currentScene,f,RN,img,img_1,img_2,img_3,img_4,img_5,img_6, imglist, img
    if key == 'r' or key == 'R':
        img = random.choice(imglist)
        image(img,0,0)
