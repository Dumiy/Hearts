import pygame
import gameplay as d
import os
class Player():
    gamePlayer = d.Player()
    px = int()
    py = int()
    def __init__(self,px=0,py=0):
        self.px = px
        self.py = py
    def __str__(self):
        return self.px + self.py
    def __repr__(self):
        return str(self)


x1=800
y1=600

playingDeck = d.Deck()
str1 = str()
img = list()
imageConver = list()
for root,dirs,files in os.walk("C:/Users/ASDERTY/IdeaProjects/Hearts/cards/",topdown=True):
    for x in files:
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
pygame.init()
gameDisplay = pygame.display.set_mode((x1,y1))
pygame.display.set_caption("Hearts <3")
clock = pygame.time.Clock()
i = 0
y = 20
playingDeck.shuffle()

gameDisplay.blit(playingDeck.cards[0].image,(0,y1/2))
crashed = False
i=0
y = 0
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()