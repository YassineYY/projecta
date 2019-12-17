
import random

def setup():
    global currentScene,f,f2,RN,img_1,img_2,img_3,img_4,img_5,img_6, imglist
    # f = loadFont('Arial')
    # f2 = createFont('Arial', 20, True)
    size(800,800)
    # currentScene = 'cyan'
    # RN = ''
    
    img_1 = loadImage("1.jpg")
    img_2 = loadImage("2.jpg")
    img_3 = loadImage("3.jpg")
    img_4 = loadImage("4.jpg")
    img_5 = loadImage("5.jpg")
    img_6 = loadImage("6.jpg")
    
    imglist = [img_1, img_2, img_3]
    
def draw():
    global currentScene,f,RN,f2,img_1,img_2,img_3,img_4,img_5,img_6, imglist
    background(0)
    
    image(img_1,0,0)
    
    # textFont(f2,20)       
    # fill(255)
    # textAlign(CENTER)
    # text("Press R to randomize a number",265,30)
    # text("The number above is the number of steps you have to take",275,530)
    
    # if currentScene == 'cyan':
    #     CyanWheel.draw()
    # else:
    #     RedWheel.draw()
        
    # textFont(f,200)       
    # fill(255)
    # textAlign(CENTER)
    # text(RN,275,345)
        
# def keyPressed():
#     import random
#     global currentScene,f,RN,img_1,img_2,img_3,img_4,img_5,img_6, imglist
#     if key == 'r' or key == 'R':
#         #image(img_1, 0, 0)
        # if currentScene == 'cyan':
        #     RN = str(random.choice([1,2,3,4,5,6]))
        #     # textFont(f,200)       
        #     # fill(255)
        #     # textAlign(CENTER)
        #     # text(RN,275,345)
        #     currentScene = 'red'
                
        # else:
        #     RN = str(random.choice([1,2,3,4,5,6]))
        #     # textFont(f,200)       
        #     # fill(255)
        #     # textAlign(CENTER)
        #     # text(RN,275,345)
        #     currentScene = 'cyan'
