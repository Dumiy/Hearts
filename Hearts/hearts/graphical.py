import pygame
import gameplay as d
import os
import threading
import time
import queue
timenow = time.time()
q = queue.Queue()
x1=1000
y1=600
class myThread(threading.Thread):
    def __init__(self,func,*args):
        self.__func=func
        self.__args=args
        threading.Thread.__init__(self)
    def run(self):
        q.put(self.__func(*self.__args))

pygame.init()
gameDisplay = pygame.display.set_mode((x1,y1))
pygame.display.set_caption("Hearts <3")
clock = pygame.time.Clock()
#background_image = pygame.image.load("C:/Users/ASDERTY/IdeaProjects/Hearts/Ricardo/Ricardo.jpg").convert()
gameDisplay.blit(background_image,[0,0])
def degree(x):
    if x is 1:
        return 0
    if x is 2:
        return 90
    if x is 3:
        return 180
    if x is 4:
        return 270
class Player():
    px = int()
    py = int()
    number = int()
    border = list(list())
    def __init__(self,px=0,py=0,number = 1,player = d.Player):
        self.px = px
        self.py = py
        self.number = number
        self.gameplayer = player
    def __str__(self):
        return self.px + self.py
    def degree(self,x):
        if x is 1:
            return 0
        if x is 2:
            return 90
        if x is 3:
            return 180
        if x is 4:
            return 270
    def __repr__(self):
        return str(self)
    def setPlayer(self):
        i= 0
        p = self.setPosition()
        for x in self.gameplayer.hand:
            y=p[i]
            temp = pygame.transform.rotate(x.image,degree(self.number))
            print(y[0]," ",y[1])
            gameDisplay.blit(temp,(y[0],y[1]))
            pygame.display.update()
            i+=1
    def setPosition(self):
        coord = list()
        border = list()
        if self.number is 1:
            coord.append(self.px)
            coord.append(self.py)
            var1 = -160
            for _ in range(5):
                temp = list()
                t1 = (coord[0]//2)+var1
                t2 = coord[1]-70
                temp.append(t1)
                temp.append(t2)
                border.append(temp)
                var1 = var1 + 70
        if self.number is 2:
            coord.append(self.px)
            coord.append(self.py)
            var = int(-160)
            for _ in range(5):
                temp = list()
                t1 = 0
                t2 = (coord[1]//2)+var
                temp.append(t1)
                temp.append(t2)
                border.append(temp)
                var+=70
        if self.number is 3:
            coord.append(self.px)
            coord.append(self.py)
            var = int(-160)
            for _ in range(5):
                temp = list()
                t1 = (coord[0]//2)+var
                t2 = 0
                temp.append(t1)
                temp.append(t2)
                border.append(temp)
                var+=70
        if self.number is 4:
            coord.append(self.px)
            coord.append(self.py)
            var = int(-160)
            for _ in range(5):
                temp = list()
                t1 = coord[0]-70
                t2 = (coord[1]//2)+var
                temp.append(t1)
                temp.append(t2)
                border.append(temp)
                var+=70
        return border


def  loadingGame():
    playingDeck = d.Deck()
    for root,dirs,files in os.walk("C:/Users/ASDERTY/IdeaProjects/Hearts/cards/",topdown=True):
        for x in files:
            str1 = str()
            y = os.path.join(root,x)
            image = pygame.image.load(y)
            image = pygame.transform.scale(image,(70,70))
            str1 = x[0:x.find('.')]
            if len(str1) is 3:
                var = int(str1[0:2])
                playingDeck.createDeck(var,var,var,image)
            else:
                var = int(str1[0])
                playingDeck.createDeck(var,var,var,image)
    return playingDeck

playingDeck = myThread(loadingGame)
playingDeck.start()
playingDeck.join()
playingDeck = q.get()
playingDeck.shuffle()
Player1 = myThread(d.Player,list(),0,playingDeck)
Player2 = myThread(d.Player,list(),0,playingDeck)
Player3 = myThread(d.Player,list(),0,playingDeck)
Player4 = myThread(d.Player,list(),0,playingDeck)

Player1.start()
Player2.start()
Player3.start()
Player4.start()

Player1.join()
Player2.join()
Player3.join()
Player4.join()

Player1 = q.get()
Player2 = q.get()
Player3 = q.get()
Player4 = q.get()

#Player1 = d.Player(list(),0,playingDeck)
#Player2 = d.Player(list(),0,playingDeck)
#Player3 = d.Player(list(),0,playingDeck)
#Player4 = d.Player(list(),0,playingDeck)
for _ in range(5):
    Player1.drawCard()
    Player2.drawCard()
    Player3.drawCard()
    Player4.drawCard()
first = Player(x1,y1,1,Player1)
second =Player(x1,y1,2,Player2)
third =Player(x1,y1,3,Player3)
fourth =Player(x1,y1,4,Player4)

first.setPlayer()
second.setPlayer()
third.setPlayer()
fourth.setPlayer()
print("---%s seconds----",(time.time()-timenow))
crashed  = False
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()