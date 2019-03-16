import random
import time
'''
def generator_number():
    for x in range(1,14):
        yield x

        
def generator_type():
    yield 'Diamonds'
    yield 'Hearts'
    yield 'Spades'
    yield 'Clubs'
'''

class playGround():
    def __init__ (self,players=list(),pile=list()):
        self.players = players
        self.pile = pile
    def cardsPile(self,pile):
        for x in pile:
            self.pile.append(x)
    def play_obo(self,players):
        for _ in range(5):
            for x in self.players:
                x.drawCard()
    def play_5pp(self,players):
        for x in self.players:
            for _ in range(5):
                x.drawCard()

class Card():
    cardsNumber = int()
    number = int()
    _type = str()
    image= []
    def __init__(self,number=0,_type='',cardsNumber = 5,image = []):
        self.number = number
        self._type = _type
        self.cardsNumber = cardsNumber
        self.image = image
    def __str__(self):
        return str(self.number) + " " + self._type
    def __repr__(self):
        return str(self)
    def modifyValue(self,number):
        self.number = number
    def __iter__(self):
        return self

class Deck:
    def __init__(self):
        self.cards = list()
    def __str__(self):
        self.printdeck()
        return " " 
    def createDeck(self,x,y,z,img):
        self.cards.append(Card(x,y,z,img))
    def printdeck(self):
        print(self.cards)
    def shuffle(self):
        random.shuffle(self.cards)
    def get_firstCard(self):
        if len(self.cards) is 1:
            x = self.cards[0]
            self.cards.pop(0)
        else:
            self.cards.pop(0)
        return x 
    def specialCard(self,special):
        for x in self.cards:
            if x.number is special:
                x.modifyValue(0)
    def __iter__(self):
        return iter(self.cards)

            
class Player (Deck,playGround):
    hand = list()
    cards = Card()
    score = int()
    def __init__ (self,hand=list(),cards=Card(),score = 0):
        self.hand = hand
        self.cards = cards
        self.score = score
    def get_Score(self):
        return self.score
    def set_Score(self,score):
        self.score+=score
    def drawCard(self,hand):
        if len(self.hand) is 5:
            return "Not possible"
        else:
            self.hand.append(super().get_firstCard())
    def playCard(self,play,possition):
        if len(set(play)) is len(play):
            super().cardsPile(play)
            self.removeCard(possition)
    def removeCard(self,possition):
        for x in possition:
            self.hand[x].pop()
    def __str__(self):
        return self.hand + self.cards +self.score
