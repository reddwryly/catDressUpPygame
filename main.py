import pygame #requires pip install *
'''
copy paste in terminal to install: python3 -m pip install -U pygame --user
copy paste in terminal to check if working: python3 -m pygame.examples.aliens
if problems occur visit: https://www.pygame.org/wiki/GettingStarted
'''
import sys 
import random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 60

#load images
start = pygame.transform.scale_by(pygame.image.load(r'asset\button\start.png'), 2)

ColorTabSelected = pygame.image.load(r'asset\tabs\selectedColor.png')
ColorTabUnselected = pygame.image.load(r'asset\tabs\unselectedColor.png')
ShirtTabSelected = pygame.image.load(r'asset\tabs\selectedShirt.png')
ShirtTabUnselected = pygame.image.load(r'asset\tabs\unselectedShirt.png')
PantsTabSelected = pygame.image.load(r'asset\tabs\selectedPants.png')
PantsTabUnselected = pygame.image.load(r'asset\tabs\unselectedPants.png')
SweaterTabSelected = pygame.image.load(r'asset\tabs\selectedSweater.png')
SweaterTabUnselected = pygame.image.load(r'asset\tabs\unselectedSweater.png')
AccessoriesTabSelected = pygame.image.load(r'asset\tabs\selectedAccessories.png')
AccessoriesTabUnselected = pygame.image.load(r'asset\tabs\unselectedAccessories.png')
ShoesTabSelected = pygame.image.load(r'asset\tabs\selectedShoes.png')
ShoesTabUnselected = pygame.image.load(r'asset\tabs\unselectedShoes.png')

leftArrow = pygame.image.load(r'asset\button\left.png')
rightArrow = pygame.image.load(r'asset\button\right.png')

#temp color selectors 
redSelect = pygame.image.load(r'asset\button\red.png')
orangeSelect = pygame.image.load(r'asset\button\orange.png')
yellowSelect = pygame.image.load(r'asset\button\yellow.png')
greenSelect = pygame.image.load(r'asset\button\green.png')
blueSelect = pygame.image.load(r'asset\button\blue.png')
purpleSelect = pygame.image.load(r'asset\button\purple.png')
pinkSelect = pygame.image.load(r'asset\button\pink.png')
brownSelect = pygame.image.load(r'asset\button\brown.png')
blackSelect = pygame.image.load(r'asset\button\black.png')
graySelect = pygame.image.load(r'asset\button\gray.png')

blackCat = pygame.image.load(r'asset/character/black.png')
brownCat = pygame.image.load(r'asset/character/brown.png')
calicoCat = pygame.image.load(r'asset/character/calico.png')
orangeCat = pygame.image.load(r'asset/character/orange.png')
whiteCat = pygame.image.load(r'asset/character/white.png')

blackCatSelect = pygame.image.load(r'asset/furColorSelect/black.png')
brownCatSelect = pygame.image.load(r'asset/furColorSelect/brown.png')
calicoCatSelect = pygame.image.load(r'asset/furColorSelect/calico.png')
orangeCatSelect = pygame.image.load(r'asset/furColorSelect/orange.png')
whiteCatSelect = pygame.image.load(r'asset/furColorSelect/white.png')

#temp
shirtPickerGreen = pygame.image.load(r'asset\hats\0.png')
shirtPickerPurple = pygame.image.load(r'asset\hats\1.png')
shirtPickerRed = pygame.image.load(r'asset\hats\2.png')
shirtNone = pygame.image.load(r'asset\button\no.png')

characterGreen = pygame.image.load(r'asset/character/0.png')
characterPurple = pygame.image.load(r'asset/character/1.png')
characterRed = pygame.image.load(r'asset/character/2.png')

class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

#creating buttons     
startButton = Button(350, 170, start)
ColorTabSelectedB = Button(0,0, ColorTabSelected)
ColorTabUnselectedB = Button(0,0, ColorTabUnselected)
ShirtTabSelectedB = Button(150,0, ShirtTabSelected)
ShirtTabUnselectedB = Button(150,0, ShirtTabUnselected)
PantsTabSelectedB = Button(300,0, PantsTabSelected)
PantsTabUnselectedB = Button(300,0, PantsTabUnselected)
SweaterTabSelectedB = Button(450,0, SweaterTabSelected)
SweaterTabUnselectedB = Button(450,0, SweaterTabUnselected)
AccessoriesTabSelectedB = Button(600,0, AccessoriesTabSelected)
AccessoriesTabUnselectedB = Button(600,0, AccessoriesTabUnselected)
ShoesTabSelectedB = Button(750,0, ShoesTabSelected)
ShoesTabUnselectedB = Button(750,0, ShoesTabUnselected)

leftArrowB =  Button(250,200, leftArrow)
rightArrowB = Button(750,200, rightArrow)

redSelectB = Button(410,500, redSelect)
orangeSelectB = Button(435,500, orangeSelect)
yellowSelectB = Button(460,500, yellowSelect)
greenSelectB = Button(485,500, greenSelect)
blueSelectB = Button(510,500, blueSelect)
purpleSelectB = Button(535,500, purpleSelect)
pinkSelectB = Button(560,500, pinkSelect)
brownSelectB= Button(585,500, brownSelect)
blackSelectB = Button(610,500, blackSelect)
graySelectB = Button(635,500, graySelect)

blackCatSelectB = Button(400,200, blackCatSelect)
brownCatSelectB = Button(510,200, brownCatSelect)
calicoCatSelectB = Button(620,200, calicoCatSelect)
orangeCatSelectB = Button(455,310, orangeCatSelect)
whiteCatSelectB = Button(565,310, whiteCatSelect)

class Start:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        screen.fill('#ffa7ad')
        if startButton.draw():
            self.gameStateManager.setState('Color')

class drawCharacter:
    def __init__(self, display, characterDraw):
        self.display = display
        self.characterDraw = characterDraw
    def draw(self):
        self.display.blit((pygame.transform.scale_by(self.gameStateManager.getCharacterDraw(), 2)), (40, 150)) 

class drawShirt:
    def __init__(self, display, shirtDraw):
        self.display = display
        self.shirtDraw = shirtDraw
    def draw(self):
        self.display.blit((pygame.transform.scale_by(self.gameStateManager.getShirtDraw(), 2)), (40, 150)) 

class Color(drawCharacter):
    def __init__(self, display, gameStateManager, characterDraw):
        super().__init__(display, characterDraw)
        self.gameStateManager = gameStateManager
        characterDraw = gameStateManager.getCharacterDraw()
    def run(self):
        ColorTabSelectedB.draw()
        if ShirtTabUnselectedB.draw():
            self.gameStateManager.setState('Shirt')
        if PantsTabUnselectedB.draw():
            self.gameStateManager.setState('Pants')
        if SweaterTabUnselectedB.draw():
            self.gameStateManager.setState('Sweater')
        if AccessoriesTabUnselectedB.draw():
            self.gameStateManager.setState('Accessories')
        if ShoesTabUnselectedB.draw():
            self.gameStateManager.setState('Shoes')   
        if blackCatSelectB.draw():
            self.gameStateManager.setCharacterDraw(pygame.image.load(r'asset/character/black.png'))
        if brownCatSelectB.draw():
            self.gameStateManager.setCharacterDraw(pygame.image.load(r'asset/character/brown.png'))
        if calicoCatSelectB.draw():
            self.gameStateManager.setCharacterDraw(pygame.image.load(r'asset/character/calico.png'))
        if orangeCatSelectB.draw():
            self.gameStateManager.setCharacterDraw(pygame.image.load(r'asset/character/orange.png'))
        if whiteCatSelectB.draw():
            self.gameStateManager.setCharacterDraw(pygame.image.load(r'asset/character/white.png'))
        drawCharacter.draw(self)
        drawShirt.draw(self)


class Shirt(Color, drawShirt):
    def __init__(self, display, gameStateManager, shirtDraw, color, shirts, shirtSelect, shirtIndex1, shirtIndex2, shirtIndex3, shirtIndex4):
        super().__init__(display, gameStateManager, shirtDraw)
        shirtDraw = gameStateManager.getCharacterDraw()
        self.color = color
        self.color = 9
        self.shirts = shirts
        # self.shirts = [r'asset\empty.png', r'asset/Shirts/shortdress/'+str(self.color)+'.png', r'asset/Shirts/longsleve/'+str(self.color)+'.png', r'asset\Shirts\plane/'+str(self.color)+'.png', r'asset\Shirts\tanktop/'+str(self.color)+'.png', r'asset\Shirts\tshirt/'+str(self.color)+'.png']
        self.shirtSelect = shirtSelect
        # self.shirtSelect = [r'asset\button\no.png', r'asset/Shirts/shortdress/'+str(self.color)+'.png', r'asset/Shirts/longsleve/'+str(self.color)+'.png', r'asset\Shirts\plane/'+str(self.color)+'.png', r'asset\Shirts\tanktop/'+str(self.color)+'.png', r'asset\Shirts\tshirt/'+str(self.color)+'.png']
        self.shirtIndex1 = shirtIndex1
        self.shirtIndex1 = 0
        self.shirtIndex2 = shirtIndex2
        self.shirtIndex2 = 1
        self.shirtIndex3 = shirtIndex3
        self.shirtIndex3 = 2
        self.shirtIndex4 = shirtIndex4
        self.shirtIndex4 = 3
    def run(self): 
        ShirtTabSelectedB.draw()
        if ColorTabUnselectedB.draw():
            self.gameStateManager.setState('Color')
        if PantsTabUnselectedB.draw():
            self.gameStateManager.setState('Pants')
        if SweaterTabUnselectedB.draw():
            self.gameStateManager.setState('Sweater')
        if AccessoriesTabUnselectedB.draw():
            self.gameStateManager.setState('Accessories')
        if ShoesTabUnselectedB.draw():
            self.gameStateManager.setState('Shoes')
        if redSelectB.draw():
            self.color = 0
        if orangeSelectB.draw():
            self.color = 1
        if yellowSelectB.draw():
            self.color = 2
        if greenSelectB.draw():
            self.color = 3
        if blueSelectB.draw():
            self.color = 4
        if purpleSelectB.draw():
            self.color = 5
        if pinkSelectB.draw():
            self.color = 6
        if brownSelectB.draw():
            self.color = 7
        if blackSelectB.draw():
            self.color = 8
        if graySelectB.draw():
            self.color = 9   
        self.shirts = [r'asset\empty.png', r'asset/Shirts/shortdress/'+str(self.color)+'.png', r'asset/Shirts/longsleve/'+str(self.color)+'.png', r'asset\Shirts\plane/'+str(self.color)+'.png', r'asset\Shirts\tanktop/'+str(self.color)+'.png', r'asset\Shirts\tshirt/'+str(self.color)+'.png']
        self.shirtSelect = [r'asset\button\no.png', r'asset/Shirts/shortdress/'+str(self.color)+'.png', r'asset/Shirts/longsleve/'+str(self.color)+'.png', r'asset\Shirts\plane/'+str(self.color)+'.png', r'asset\Shirts\tanktop/'+str(self.color)+'.png', r'asset\Shirts\tshirt/'+str(self.color)+'.png']
        if rightArrowB.draw():
            if self.shirtIndex1 < len(self.shirts) - 1:
                self.shirtIndex1 += 1
            else:
                self.shirtIndex1 = 0
            if self.shirtIndex2 < len(self.shirts) - 1:
                self.shirtIndex2 += 1
            else:
                self.shirtIndex2 = 0
            if self.shirtIndex3 < len(self.shirts) - 1:
                self.shirtIndex3 += 1
            else:
                self.shirtIndex3 = 0
            if self.shirtIndex4 < len(self.shirts) - 1:
                self.shirtIndex4 += 1
            else:
                self.shirtIndex4 = 0
        if leftArrowB.draw():
            if self.shirtIndex1 > 0:
                self.shirtIndex1 -= 1
            else:
                self.shirtIndex1 = len(self.shirts) - 1
            if self.shirtIndex2 > 0:
                self.shirtIndex2 -= 1
            else:
                self.shirtIndex2 = len(self.shirts) - 1
            if self.shirtIndex3 > 0:
                self.shirtIndex3 -= 1
            else:
                self.shirtIndex3 = len(self.shirts) - 1
            if self.shirtIndex4 > 0:
                self.shirtIndex4 -= 1
            else:
                self.shirtIndex4 = len(self.shirts) - 1
        shirtBlit1 = pygame.image.load(self.shirtSelect[self.shirtIndex1])
        shirtBlit2 = pygame.image.load(self.shirtSelect[self.shirtIndex2])
        shirtBlit3 = pygame.image.load(self.shirtSelect[self.shirtIndex3])
        shirtBlit4 = pygame.image.load(self.shirtSelect[self.shirtIndex4])
        shirtBlit1B = Button(350,175, shirtBlit1)
        shirtBlit2B = Button(450,175, shirtBlit2)
        shirtBlit3B = Button(550,175, shirtBlit3)
        shirtBlit4B = Button(650,175, shirtBlit4)
        if shirtBlit1B.draw():
            self.gameStateManager.setShirtDraw(pygame.image.load(self.shirts[self.shirtIndex1]))
        if shirtBlit2B.draw():
            self.gameStateManager.setShirtDraw(pygame.image.load(self.shirts[self.shirtIndex2]))
        if shirtBlit3B.draw():
            self.gameStateManager.setShirtDraw(pygame.image.load(self.shirts[self.shirtIndex3]))
        if shirtBlit4B.draw():
            self.gameStateManager.setShirtDraw(pygame.image.load(self.shirts[self.shirtIndex4]))
        drawCharacter.draw(self)
        drawShirt.draw(self)

class Pants(Shirt):
    def __init__(self, display, gameStateManager, shirtDraw, color, shirts, shirtSelect, shirtIndex1, shirtIndex2, shirtIndex3, shirtIndex4):
        super().__init__(display, gameStateManager, shirtDraw, color, shirts, shirtSelect, shirtIndex1, shirtIndex2, shirtIndex3, shirtIndex4)
        shirtDraw = gameStateManager.getShirtDraw()
    def run(self):
        PantsTabSelectedB.draw()
        if ColorTabUnselectedB.draw():
            self.gameStateManager.setState('Color')
        if ShirtTabUnselectedB.draw():
            self.gameStateManager.setState('Shirt')
        if SweaterTabUnselectedB.draw():
            self.gameStateManager.setState('Sweater')
        if AccessoriesTabUnselectedB.draw():
            self.gameStateManager.setState('Accessories')
        if ShoesTabUnselectedB.draw():
            self.gameStateManager.setState('Shoes')
        if redSelectB.draw():
            self.color = 0
        if orangeSelectB.draw():
            self.color = 1
        if yellowSelectB.draw():
            self.color = 2
        if greenSelectB.draw():
            self.color = 3
        if blueSelectB.draw():
            self.color = 4
        if purpleSelectB.draw():
            self.color = 5
        if pinkSelectB.draw():
            self.color = 6
        if brownSelectB.draw():
            self.color = 7
        if blackSelectB.draw():
            self.color = 8
        if graySelectB.draw():
            self.color = 9   
        drawCharacter.draw(self)
        drawShirt.draw(self)

class Sweater:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        SweaterTabSelectedB.draw()
        if ColorTabUnselectedB.draw():
            self.gameStateManager.setState('Color')
        if ShirtTabUnselectedB.draw():
            self.gameStateManager.setState('Shirt')
        if PantsTabUnselectedB.draw():
            self.gameStateManager.setState('Pants')
        if AccessoriesTabUnselectedB.draw():
            self.gameStateManager.setState('Accessories')
        if ShoesTabUnselectedB.draw():
            self.gameStateManager.setState('Shoes')

class Accessories:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        AccessoriesTabSelectedB.draw()
        if ColorTabUnselectedB.draw():
            self.gameStateManager.setState('Color')
        if ShirtTabUnselectedB.draw():
            self.gameStateManager.setState('Shirt')
        if PantsTabUnselectedB.draw():
            self.gameStateManager.setState('Pants')
        if SweaterTabUnselectedB.draw():
            self.gameStateManager.setState('Sweater')
        if ShoesTabUnselectedB.draw():
            self.gameStateManager.setState('Shoes')

class Shoes:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        ShoesTabSelectedB.draw()
        if ColorTabUnselectedB.draw():
            self.gameStateManager.setState('Color')
        if ShirtTabUnselectedB.draw():
            self.gameStateManager.setState('Shirt')
        if PantsTabUnselectedB.draw():
            self.gameStateManager.setState('Pants')
        if SweaterTabUnselectedB.draw():
            self.gameStateManager.setState('Sweater')
        if AccessoriesTabUnselectedB.draw():
            self.gameStateManager.setState('Accessories')

class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
        self.characterDraw = pygame.image.load(r'asset/character/black.png')
        self.shirtDraw = pygame.image.load(r'asset\hats\empty.png')

    def getState(self):
        return self.currentState
    def setState(self, state):
        self.currentState = state
    def getCharacterDraw(self):
        return self.characterDraw
    def setCharacterDraw(self, character): 
        self.characterDraw = character
    def getShirtDraw(self):
        return self.shirtDraw
    def setShirtDraw(self, character): 
        self.shirtDraw = character

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Cat Dress Up")

        self.characterDraw = blackCat
        self.shirtDraw = shirtPickerGreen
        self.color = 9
        self.shirts = []
        self.shirtSelect = []
        self.shirtIndex1 = 0
        self.shirtIndex2 = 1
        self.shirtIndex3 = 2
        self.shirtIndex4 = 3
        self.gameStateManager = GameStateManager('start')

        self.start = Start(self.screen, self.gameStateManager)
        self.Color = Color(self.screen, self.gameStateManager, self.characterDraw)
        self.Shirt = Shirt(self.screen, self.gameStateManager, self.shirtDraw, self.color, self.shirts, self.shirtSelect, self.shirtIndex1, self.shirtIndex2, self.shirtIndex3, self.shirtIndex4)
        self.Pants = Pants(self.screen, self.gameStateManager, self.shirtDraw, self.color, self.shirts, self.shirtSelect, self.shirtIndex1, self.shirtIndex2, self.shirtIndex3, self.shirtIndex4)
        self.Sweater = Sweater(self.screen, self.gameStateManager)
        self.Accessories = Accessories(self.screen, self.gameStateManager)
        self.Shoes = Shoes(self.screen, self.gameStateManager)

        self.states = {'start':self.start, 'Color':self.Color, 'Shirt':self.Shirt, 'Pants':self.Pants, 
                        'Sweater':self.Sweater, 'Accessories':self.Accessories, 'Shoes':self.Shoes} #scenes or "tabs"
        
    def run(self):
        while True:

            screen.fill('#ffa7ad')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.states[self.gameStateManager.getState()].run()

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()