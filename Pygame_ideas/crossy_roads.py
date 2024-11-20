import pygame as p

class Dog(p.sprite.Sprite):#inheriting dog from sprite module
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = HEIGHT / 2
        self.vel = 4
        self.width = 100
        self.height = 50

        #IMAGES NEED TO UPDATE
        #DOG 1 right
        self.dog1 = p.image.load('dog1.png') # update to file name
        #DOG 2 left
        self.dog2 = p.image.load('dog2.png') # update to file name
        #set width and height for dog image 1
        self.dog1 = p.transform.scale(self.dog1, (self.width, self.height))
        #set width and hieght for dog image 2
        self.dog2 = p.transform.scale(self.dog2, (self.width, self.height))

WIDTH = 640
HEIGHT = 480

p.init()#initialise all modules within pygame

win = p.display.set_mode((WIDTH, HEIGHT)) #dimensions for background
p.display.set_caption('Crossy Road')
clock = p.time.Clock() # timer

run = True
while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False # end game if quit is entered

        win.fill((0, 255, 0))#bright green colour
        p.display.update()#user can see the changes going on

p.quit() #prevents an endless loop

