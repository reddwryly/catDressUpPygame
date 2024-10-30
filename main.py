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

shirtPickerGreen = pygame.image.load(r'asset\hats\0.png')
shirtPickerPurple = pygame.image.load(r'asset\hats\1.png')
shirtPickerRed = pygame.image.load(r'asset\hats\2.png')

characterGreen = pygame.image.load(r'asset/character/0.png')
characterPurple = pygame.image.load(r'asset/character/1.png')
characterRed = pygame.image.load(r'asset/character/2.png')

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

class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
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

shirtPickerGreenB = Button(450,200, shirtPickerGreen)
shirtPickerPurpleB = Button(550,200, shirtPickerPurple)
shirtPickerRedB = Button(650,200, shirtPickerRed)

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
            self.gameStateManager.set_state('Color')

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
        self.display.blit(self.gameStateManager.getShirtDraw(), (90, 120)) 

class Color(drawCharacter):
    def __init__(self, display, gameStateManager, characterDraw):
        super().__init__(display, characterDraw)
        self.gameStateManager = gameStateManager
        characterDraw = gameStateManager.getCharacterDraw()
    def run(self):
        ColorTabSelectedB.draw()
        if ShirtTabUnselectedB.draw():
            self.gameStateManager.set_state('Shirt')
        if PantsTabUnselectedB.draw():
            self.gameStateManager.set_state('Pants')
        if SweaterTabUnselectedB.draw():
            self.gameStateManager.set_state('Sweater')
        if AccessoriesTabUnselectedB.draw():
            self.gameStateManager.set_state('Accessories')
        if ShoesTabUnselectedB.draw():
            self.gameStateManager.set_state('Shoes')   
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

class Shirt(Color, drawShirt):
    def __init__(self, display, gameStateManager, shirtDraw):
        super().__init__(display, gameStateManager, shirtDraw)
        shirtDraw = gameStateManager.getCharacterDraw()
    def run(self): 
        ShirtTabSelectedB.draw()
        if ColorTabUnselectedB.draw():
            self.gameStateManager.set_state('Color')
        if PantsTabUnselectedB.draw():
            self.gameStateManager.set_state('Pants')
        if SweaterTabUnselectedB.draw():
            self.gameStateManager.set_state('Sweater')
        if AccessoriesTabUnselectedB.draw():
            self.gameStateManager.set_state('Accessories')
        if ShoesTabUnselectedB.draw():
            self.gameStateManager.set_state('Shoes')
        if shirtPickerGreenB.draw():
            self.gameStateManager.setShirtDraw(pygame.image.load(r'asset/hats/0.png'))
        if shirtPickerPurpleB.draw():
            self.gameStateManager.setShirtDraw(pygame.image.load(r'asset/hats/1.png'))
        if shirtPickerRedB.draw():
            self.gameStateManager.setShirtDraw(pygame.image.load(r'asset/hats/2.png'))
        drawCharacter.draw(self)
        drawShirt.draw(self)

class Pants(Shirt):
    def __init__(self, display, gameStateManager, shirtDraw):
        super().__init__(display, gameStateManager, shirtDraw)
        shirtDraw = gameStateManager.getShirtDraw()
    def run(self):
        PantsTabSelectedB.draw()
        if ColorTabUnselectedB.draw():
            self.gameStateManager.set_state('Color')
        if ShirtTabUnselectedB.draw():
            self.gameStateManager.set_state('Shirt')
        if SweaterTabUnselectedB.draw():
            self.gameStateManager.set_state('Sweater')
        if AccessoriesTabUnselectedB.draw():
            self.gameStateManager.set_state('Accessories')
        if ShoesTabUnselectedB.draw():
            self.gameStateManager.set_state('Shoes')
        drawCharacter.draw(self)
        drawShirt.draw(self)

class Sweater:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        SweaterTabSelectedB.draw()
        if ColorTabUnselectedB.draw():
            self.gameStateManager.set_state('Color')
        if ShirtTabUnselectedB.draw():
            self.gameStateManager.set_state('Shirt')
        if PantsTabUnselectedB.draw():
            self.gameStateManager.set_state('Pants')
        if AccessoriesTabUnselectedB.draw():
            self.gameStateManager.set_state('Accessories')
        if ShoesTabUnselectedB.draw():
            self.gameStateManager.set_state('Shoes')

class Accessories:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        AccessoriesTabSelectedB.draw()
        if ColorTabUnselectedB.draw():
            self.gameStateManager.set_state('Color')
        if ShirtTabUnselectedB.draw():
            self.gameStateManager.set_state('Shirt')
        if PantsTabUnselectedB.draw():
            self.gameStateManager.set_state('Pants')
        if SweaterTabUnselectedB.draw():
            self.gameStateManager.set_state('Sweater')
        if ShoesTabUnselectedB.draw():
            self.gameStateManager.set_state('Shoes')

class Shoes:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        ShoesTabSelectedB.draw()
        if ColorTabUnselectedB.draw():
            self.gameStateManager.set_state('Color')
        if ShirtTabUnselectedB.draw():
            self.gameStateManager.set_state('Shirt')
        if PantsTabUnselectedB.draw():
            self.gameStateManager.set_state('Pants')
        if SweaterTabUnselectedB.draw():
            self.gameStateManager.set_state('Sweater')
        if AccessoriesTabUnselectedB.draw():
            self.gameStateManager.set_state('Accessories')

class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
        self.characterDraw = pygame.image.load(r'asset/character/black.png')
        self.shirtDraw = pygame.image.load(r'asset/hats/0.png')

    def get_state(self):
        return self.currentState
    def set_state(self, state):
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
        self.gameStateManager = GameStateManager('start')

        self.start = Start(self.screen, self.gameStateManager)
        self.Color = Color(self.screen, self.gameStateManager, self.characterDraw)
        self.Shirt = Shirt(self.screen, self.gameStateManager, self.shirtDraw)
        self.Pants = Pants(self.screen, self.gameStateManager, self.shirtDraw)
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

            self.states[self.gameStateManager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()