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

Shuffle = pygame.image.load(r'asset\button\select.png')

colorSelected = pygame.image.load(r'asset\button\colorSelected.png')

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

leftArrowB =  Button(300,230, leftArrow)
rightArrowB = Button(700,230, rightArrow)
leftTopArrowB = Button(250,170, leftArrow)
leftBotArrowB = Button(250,290, leftArrow)
rightTopArrowB = Button(800,170, rightArrow)
rightBotArrowB = Button(800,290, rightArrow)

redSelectB = Button(410,475, redSelect)
orangeSelectB = Button(435,475, orangeSelect)
yellowSelectB = Button(460,475, yellowSelect)
greenSelectB = Button(485,475, greenSelect)
blueSelectB = Button(510,475, blueSelect)
purpleSelectB = Button(535,475, purpleSelect)
pinkSelectB = Button(560,475, pinkSelect)
brownSelectB= Button(585,475, brownSelect)
blackSelectB = Button(610,475, blackSelect)
graySelectB = Button(635,475, graySelect)

blackCatSelectB = Button(400,200, blackCatSelect)
brownCatSelectB = Button(510,200, brownCatSelect)
calicoCatSelectB = Button(620,200, calicoCatSelect)
orangeCatSelectB = Button(455,310, orangeCatSelect)
whiteCatSelectB = Button(565,310, whiteCatSelect)

ShuffleB = Button(300,430, Shuffle)

shirtPickerRedB = Button(100,520, shirtPickerRed)
shirtPickerPurpleB = Button(200,520, shirtPickerPurple)

class Start:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        screen.fill('#ffa7ad')
        if startButton.draw():
            self.gameStateManager.setState('Color')

class drawColorSelect:
    def __init__(self, display, color, x):
        self.display = display
        self.color = color
        self.x = x
    def colorSelect(self):
        if redSelectB.draw():
            self.color = 0
            self.x = 407
        if orangeSelectB.draw():
            self.color = 1
            self.x = 432
        if yellowSelectB.draw():
            self.color = 2
            self.x = 457
        if greenSelectB.draw():
            self.color = 3
            self.x = 482
        if blueSelectB.draw():
            self.color = 4
            self.x = 507
        if purpleSelectB.draw():
            self.color = 5
            self.x = 532
        if pinkSelectB.draw():
            self.color = 6
            self.x = 557
        if brownSelectB.draw():
            self.color = 7
            self.x = 582
        if blackSelectB.draw():
            self.color = 8
            self.x = 607
        if graySelectB.draw():
            self.color = 9   
            self.x = 632
        self.display.blit(colorSelected, (self.x,472))

class Universal:
    def __init__(self, gameStateManager, color, shirts, pants, sweater, accessories, shoes1, shoes2):
        self.gameStateManager = gameStateManager
        self.color = color
        self.shirts = [r'asset\empty.png', r'asset/Shirts/shortdress/'+str(self.color)+'.png',  r'asset\Shirts\longsleve/'+str(self.color)+'.png', r'asset\Shirts\plane/'+str(self.color)+'.png', r'asset\Shirts\tanktop/'+str(self.color)+'.png', r'asset\Shirts\tshirt/'+str(self.color)+'.png']
        self.pants = [r'asset\empty.png', r'asset\Pants\Jeans/'+str(self.color)+'.png', r'asset\Pants\jeanShorts/'+str(self.color)+'.png', r'asset\Pants\BasketballShorts/'+str(self.color)+'.png', r'asset\Pants\cargoPants/'+str(self.color)+'.png', r'asset\Pants\loosePants/'+str(self.color)+'.png', r'asset\Pants\shortSkirt/'+str(self.color)+'.png', r'asset\Pants\LongSkirt/'+str(self.color)+'.png']
        self.sweater = [r'asset\empty.png', r'asset\Sweater\Blue/'+str(self.color)+'.png', r'asset\Sweater\Cardigan/'+str(self.color)+'.png', r'asset\Sweater\Jacket/'+str(self.color)+'.png', r'asset\Sweater\Sweater/'+str(self.color)+'.png', r'asset\Sweater\Purple/'+str(self.color)+'.png', r'asset\Sweater\SweaterVest/'+str(self.color)+'.png', r'asset\Sweater\crewneck/'+str(self.color)+'.png']
        self.accessories = [r'asset\empty.png', r'asset\accessories\tie/'+str(self.color)+'.png', r'asset\accessories\scarf/'+str(self.color)+'.png', r'asset\accessories\hat/'+str(self.color)+'.png', r'asset\accessories\ingles/'+str(self.color)+'.png', r'asset\accessories\bigHat/'+str(self.color)+'.png', r'asset\accessories\watch/'+str(self.color)+'.png', r'asset\accessories\bow/'+str(self.color)+'.png', r'asset\accessories\necklace/'+str(self.color)+'.png', r'asset\accessories\purse/'+str(self.color)+'.png']
        self.shoes2 = [r'asset\empty.png', r'asset\shoe\shoe\converse/'+str(self.color)+'.png', r'asset\shoe\shoe\loaf/'+str(self.color)+'.png', r'asset\shoe\shoe\mj/'+str(self.color)+'.png', r'asset\shoe\shoe\sneek/'+str(self.color)+'.png']
        self.shoes1 = [r'asset\empty.png', r'asset\shoe\sock\shortSock/'+str(self.color)+'.png', r'asset\shoe\sock\tallSock/'+str(self.color)+'.png', r'asset\shoe\sock\tights/'+str(self.color)+'.png', r'asset\shoe\sock\legging/'+str(self.color)+'.png']
    def restart(self):
        if shirtPickerRedB.draw():
            self.gameStateManager.setState('start')
            self.gameStateManager.setCharacterDraw(pygame.image.load(r'asset/character/black.png'))
            self.gameStateManager.setShirtDraw(pygame.image.load(r'asset\empty.png'))
            self.gameStateManager.setPantsDraw(pygame.image.load(r'asset\empty.png'))
            self.gameStateManager.setSweaterDraw(pygame.image.load(r'asset\empty.png'))
            self.gameStateManager.setAccessories1Draw(pygame.image.load(r'asset\empty.png'))
            self.gameStateManager.setAccessories2Draw(pygame.image.load(r'asset\empty.png'))
            self.gameStateManager.setShoes1Draw(pygame.image.load(r'asset\empty.png'))
            self.gameStateManager.setShoes2Draw(pygame.image.load(r'asset\empty.png'))
    def fullShuffle(self):
        if shirtPickerPurpleB.draw():
            self.furindex = random.randrange(0,(len(self.furcolor)))
            self.gameStateManager.setCharacterDraw(pygame.image.load(r'asset/character/'+str(self.furcolor[self.furindex])+'.png'))
            self.randomColor1 = random.randint(0,9)
            self.shirtPaths1 = [path.replace(str(self.color), str(self.randomColor1)) for path in self.shirts]
            self.random1 = random.randint(0,len(self.shirts)-1)
            self.gameStateManager.setShirtDraw(pygame.image.load(self.shirtPaths1[self.random1]))
            self.randomColor2 = random.randint(0,9)
            self.pantsPaths2 = [path.replace(str(self.color), str(self.randomColor2)) for path in self.pants]
            self.random2 = random.randint(0,len(self.pants)-1)
            self.gameStateManager.setPantsDraw(pygame.image.load(self.pantsPaths2[self.random2]))
            print(self.gameStateManager.getPantsDraw())
            self.randomColor3 = random.randint(0,9)
            self.sweaterPaths3 = [path.replace(str(self.color), str(self.randomColor3)) for path in self.sweater]
            self.random3 = random.randint(0,len(self.sweater)-1)
            self.gameStateManager.setSweaterDraw(pygame.image.load(self.sweaterPaths3[self.random3]))
            self.randomColor4 = random.randint(0,9)
            self.accessoriesPaths4 = [path.replace(str(self.color), str(self.randomColor4)) for path in self.accessories]
            self.random4 = random.randint(0,len(self.accessories)-1)
            self.gameStateManager.setAccessories1Draw(pygame.image.load(self.accessoriesPaths4[self.random4]))
            self.randomColor5 = random.randint(0,9)
            self.accessoriesPaths5 = [path.replace(str(self.color), str(self.randomColor5)) for path in self.accessories]
            self.random5 = random.randint(0,len(self.accessories)-1)
            self.gameStateManager.setAccessories2Draw(pygame.image.load(self.accessoriesPaths5[self.random5]))
            self.randomColor6 = random.randint(0,9)
            self.shoesPaths6 = [path.replace(str(self.color), str(self.randomColor6)) for path in self.shoes1]
            self.random6 = random.randint(0,len(self.shoes1)-1)
            self.gameStateManager.setShoes1Draw(pygame.image.load(self.shoesPaths6[self.random6]))
            self.randomColor7 = random.randint(0,9)
            self.shoesPaths7 = [path.replace(str(self.color), str(self.randomColor7)) for path in self.shoes2]
            self.random7 = random.randint(0,len(self.shoes2)-1)
            self.gameStateManager.setShoes2Draw(pygame.image.load(self.shoesPaths7[self.random7]))
    def draw(self):
        self.display.blit((pygame.transform.scale_by(self.gameStateManager.getCharacterDraw(), 2)), (40, 150)) 
        self.display.blit((pygame.transform.scale_by(self.gameStateManager.getShoes1Draw(), 2)), (40, 150)) 
        self.display.blit((pygame.transform.scale_by(self.gameStateManager.getPantsDraw(), 2)), (40, 150)) 
        self.display.blit((pygame.transform.scale_by(self.gameStateManager.getShirtDraw(), 2)), (40, 150)) 
        self.display.blit((pygame.transform.scale_by(self.gameStateManager.getSweaterDraw(), 2)), (40, 150)) 
        self.display.blit((pygame.transform.scale_by(self.gameStateManager.getAccessories1Draw(), 2)), (40, 150)) 
        self.display.blit((pygame.transform.scale_by(self.gameStateManager.getAccessories2Draw(), 2)), (40, 150)) 
        self.display.blit((pygame.transform.scale_by(self.gameStateManager.getShoes2Draw(), 2)), (40, 150))

class Color(Universal):
    def __init__(self, display, gameStateManager, color, furcolor, furindex, shirts, pants, sweater, accessories, shoes1, shoes2):
        super().__init__(gameStateManager, color, shirts, pants, sweater, accessories, shoes1, shoes2)
        self.display = display
        self.furcolor = furcolor
        self.furcolor = ['black', 'brown', 'calico', 'orange', 'white']
        self.furindex = furindex
    def navBar(self):
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
    def select(self):
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
    def singleShuffle(self): #working but decided not to use
        if ShuffleB.draw():
            self.furindex = random.randrange(0,(len(self.furcolor)))
            self.gameStateManager.setCharacterDraw(pygame.image.load(r'asset/character/'+str(self.furcolor[self.furindex])+'.png'))
    def run(self):
        Universal.restart(self)
        Universal.fullShuffle(self)
        Color.navBar(self)
        Color.select(self)
        Universal.draw(self)

class Shirt(Color):
    def __init__(self, display, gameStateManager, color, shirts, shirtSelect, shirtIndex1, shirtIndex2, shirtIndex3, shirtIndex4, furcolor, furindex, pants, sweater, accessories, shoes1, shoes2):
        super().__init__(display, gameStateManager, furcolor, furindex, shirts, pants, sweater, accessories, shoes1, shoes2, color)        
        self.x = 632
        self.color = 9
        self.shirtIndex1 = shirtIndex1
        self.shirtIndex1 = 0
        self.shirtIndex2 = shirtIndex2
        self.shirtIndex2 = 2
        self.shirtIndex3 = shirtIndex3
        self.shirtIndex3 = 1
        self.shirtIndex4 = shirtIndex4
        self.shirtIndex4 = 3
        self.shirts = [r'asset\empty.png', r'asset/Shirts/shortdress/'+str(self.color)+'.png', r'asset/Shirts/longsleve/'+str(self.color)+'.png', r'asset\Shirts\plane/'+str(self.color)+'.png', r'asset\Shirts\tanktop/'+str(self.color)+'.png', r'asset\Shirts\tshirt/'+str(self.color)+'.png']
        self.shirtSelect = [r'asset\button\no.png', r'asset/Shirts/shortdress/'+str(self.color)+'.png', r'asset/Shirts/longsleve/'+str(self.color)+'.png', r'asset\Shirts\plane/'+str(self.color)+'.png', r'asset\Shirts\tanktop/'+str(self.color)+'.png', r'asset\Shirts\tshirt/'+str(self.color)+'.png']
    def navBar(self):
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
    def arrowButtons(self):
        self.shirts = [r'asset\empty.png', r'asset/Shirts/shortdress/'+str(self.color)+'.png', r'asset\Shirts\longsleve/'+str(self.color)+'.png', r'asset\Shirts\plane/'+str(self.color)+'.png', r'asset\Shirts\tanktop/'+str(self.color)+'.png', r'asset\Shirts\tshirt/'+str(self.color)+'.png']
        self.shirtSelect = [r'asset\button\no.png', r'asset/Shirts/shortdress/'+str(self.color)+'.png', r'asset/Shirts/longsleve/'+str(self.color)+'.png', r'asset\Shirts\plane/'+str(self.color)+'.png', r'asset\Shirts\tanktop/'+str(self.color)+'.png', r'asset\Shirts\tshirt/'+str(self.color)+'.png']
        if rightArrowB.draw():
            if self.shirtIndex1 < len(self.shirts) - 3:
                self.shirtIndex1 += 2
            else:
                self.shirtIndex1 = 0
            if self.shirtIndex2 < len(self.shirts) - 3:
                self.shirtIndex2 += 2
            else:
                self.shirtIndex2 = 0
            if self.shirtIndex3 < len(self.shirts) - 2:
                self.shirtIndex3 += 2
            else:
                self.shirtIndex3 = 1
            if self.shirtIndex4 < len(self.shirts) - 2:
                self.shirtIndex4 += 2
            else:
                self.shirtIndex4 = 1
        if leftArrowB.draw():
            if self.shirtIndex1 >= 2:
                self.shirtIndex1 -= 2
            else:
                self.shirtIndex1 = len(self.shirts) - 2
            if self.shirtIndex2 >= 2:
                self.shirtIndex2 -= 2
            else:
                self.shirtIndex2 = len(self.shirts) - 2
            if self.shirtIndex3 >= 3:
                self.shirtIndex3 -= 2
            else:
                self.shirtIndex3 = len(self.shirts) - 1
            if self.shirtIndex4 >= 3:
                self.shirtIndex4 -= 2
            else:
                self.shirtIndex4 = len(self.shirts) - 1
        shirtBlit1 = pygame.image.load(self.shirtSelect[self.shirtIndex1])
        shirtBlit2 = pygame.image.load(self.shirtSelect[self.shirtIndex2])
        shirtBlit3 = pygame.image.load(self.shirtSelect[self.shirtIndex3])
        shirtBlit4 = pygame.image.load(self.shirtSelect[self.shirtIndex4])
        shirtBlit1B = Button(445,175, shirtBlit1)
        shirtBlit2B = Button(555,175, shirtBlit2)
        shirtBlit3B = Button(445,285, shirtBlit3)
        shirtBlit4B = Button(555,285, shirtBlit4)
        if shirtBlit1B.draw():
            self.gameStateManager.setShirtDraw(pygame.image.load(self.shirts[self.shirtIndex1]))
        if shirtBlit2B.draw():
            self.gameStateManager.setShirtDraw(pygame.image.load(self.shirts[self.shirtIndex2]))
        if shirtBlit3B.draw():
            self.gameStateManager.setShirtDraw(pygame.image.load(self.shirts[self.shirtIndex3]))
        if shirtBlit4B.draw():
            self.gameStateManager.setShirtDraw(pygame.image.load(self.shirts[self.shirtIndex4]))
    def singleShuffle(self):
        if ShuffleB.draw():
            self.randomColor = random.randint(0,9)
            self.shirtPaths = [path.replace(str(self.color), str(self.randomColor)) for path in self.shirts]
            self.random = random.randint(1,len(self.shirts)-1)
            self.gameStateManager.setShirtDraw(pygame.image.load(self.shirtPaths[self.random]))
    def run(self): 
        Universal.restart(self)
        Universal.fullShuffle(self)
        Shirt.navBar(self)
        Shirt.arrowButtons(self)
        drawColorSelect.colorSelect(self)
        Shirt.arrowButtons(self)
        Shirt.singleShuffle(self)
        Universal.draw(self)

class Pants(Shirt):
    def __init__(self, display, gameStateManager, color, shirts, shirtSelect, shirtIndex1, shirtIndex2, shirtIndex3, shirtIndex4, furcolor, furindex, pants, pantsSelect, pantsIndex1, pantsIndex2, pantsIndex3, pantsIndex4, sweater, accessories, shoes1, shoes2):
        super().__init__(display, gameStateManager, color, shirts, shirtSelect, shirtIndex1, shirtIndex2, shirtIndex3, shirtIndex4, furcolor, furindex, pants, sweater, accessories, shoes1, shoes2)
        self.pantsIndex1 = pantsIndex1
        self.pantsIndex1 = 0
        self.pantsIndex2 = pantsIndex2
        self.pantsIndex2 = 2
        self.pantsIndex3 = pantsIndex3
        self.pantsIndex3 = 1
        self.pantsIndex4 = pantsIndex4
        self.pantsIndex4 = 3
        self.pants = [r'asset\empty.png', r'asset/Pants/Jeans/'+str(self.color)+'.png', r'asset/Pants/jeanShorts/'+str(self.color)+'.png', r'asset/Pants/BasketballShorts/'+str(self.color)+'.png', r'asset/Pants/cargoPants/'+str(self.color)+'.png', r'asset/Pants/loosePants/'+str(self.color)+'.png', r'asset/Pants/shortSkirt/'+str(self.color)+'.png', r'asset/Pants/LongSkirt/'+str(self.color)+'.png']
        self.pantsSelect = [r'asset\button\no.png', r'asset/Pants/Jeans/'+str(self.color)+'.png', r'asset/Pants/jeanShorts/'+str(self.color)+'.png', r'asset/Pants/BasketballShorts/'+str(self.color)+'.png', r'asset/Pants/cargoPants/'+str(self.color)+'.png', r'asset/Pants/loosePants/'+str(self.color)+'.png', r'asset/Pants/shortSkirt/'+str(self.color)+'.png', r'asset/Pants/LongSkirt/'+str(self.color)+'.png']
    def navBar(self):
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
    def arrowButtons(self):
        self.pants = [r'asset\empty.png', r'asset/Pants/Jeans/'+str(self.color)+'.png', r'asset/Pants/jeanShorts/'+str(self.color)+'.png', r'asset/Pants/BasketballShorts/'+str(self.color)+'.png', r'asset/Pants/cargoPants/'+str(self.color)+'.png', r'asset/Pants/loosePants/'+str(self.color)+'.png', r'asset/Pants/shortSkirt/'+str(self.color)+'.png', r'asset/Pants/LongSkirt/'+str(self.color)+'.png']
        self.pantsSelect = [r'asset\button\no.png', r'asset/Pants/Jeans/'+str(self.color)+'.png', r'asset/Pants/jeanShorts/'+str(self.color)+'.png', r'asset/Pants/BasketballShorts/'+str(self.color)+'.png', r'asset/Pants/cargoPants/'+str(self.color)+'.png', r'asset/Pants/loosePants/'+str(self.color)+'.png', r'asset/Pants/shortSkirt/'+str(self.color)+'.png', r'asset/Pants/LongSkirt/'+str(self.color)+'.png']
        if rightArrowB.draw():
            if self.pantsIndex1 < len(self.pants) - 3:
                self.pantsIndex1 += 2
            else:
                self.pantsIndex1 = 0
            if self.pantsIndex2 < len(self.pants) - 3:
                self.pantsIndex2 += 2
            else:
                self.pantsIndex2 = 0
            if self.pantsIndex3 < len(self.pants) - 2:
                self.pantsIndex3 += 2
            else:
                self.pantsIndex3 = 1
            if self.pantsIndex4 < len(self.pants) - 2:
                self.pantsIndex4 += 2
            else:
                self.pantsIndex4 = 1
        if leftArrowB.draw():
            if self.pantsIndex1 >= 2:
                self.pantsIndex1 -= 2
            else:
                self.pantsIndex1 = len(self.pants) - 2
            if self.pantsIndex2 >= 2:
                self.pantsIndex2 -= 2
            else:
                self.pantsIndex2 = len(self.pants) - 2
            if self.pantsIndex3 >= 3:
                self.pantsIndex3 -= 2
            else:
                self.pantsIndex3 = len(self.pants) - 1
            if self.pantsIndex4 >= 3:
                self.pantsIndex4 -= 2
            else:
                self.pantsIndex4 = len(self.pants) - 1
        pantsBlit1 = pygame.image.load(self.pantsSelect[self.pantsIndex1])
        pantsBlit2 = pygame.image.load(self.pantsSelect[self.pantsIndex2])
        pantsBlit3 = pygame.image.load(self.pantsSelect[self.pantsIndex3])
        pantsBlit4 = pygame.image.load(self.pantsSelect[self.pantsIndex4])
        pantsBlit1B = Button(445,175, pantsBlit1)
        pantsBlit2B = Button(555,175, pantsBlit2)
        pantsBlit3B = Button(445,285, pantsBlit3)
        pantsBlit4B = Button(555,285, pantsBlit4)
        if pantsBlit1B.draw():
            self.gameStateManager.setPantsDraw(pygame.image.load(self.pants[self.pantsIndex1]))
        if pantsBlit2B.draw():
            self.gameStateManager.setPantsDraw(pygame.image.load(self.pants[self.pantsIndex2]))
        if pantsBlit3B.draw():
            self.gameStateManager.setPantsDraw(pygame.image.load(self.pants[self.pantsIndex3]))
        if pantsBlit4B.draw():
            self.gameStateManager.setPantsDraw(pygame.image.load(self.pants[self.pantsIndex4]))
    def singleShuffle(self):
        if ShuffleB.draw():
            self.randomColor = random.randint(0,9)
            self.pantsPaths = [path.replace(str(self.color), str(self.randomColor)) for path in self.pants]
            self.random = random.randint(1,len(self.pants)-1)
            self.gameStateManager.setPantsDraw(pygame.image.load(self.pantsPaths[self.random]))
    def run(self):
        Universal.restart(self)
        Universal.fullShuffle(self)
        Pants.navBar(self)
        drawColorSelect.colorSelect(self)
        Pants.arrowButtons(self)
        Pants.singleShuffle(self)
        Universal.draw(self)

class Sweater(Pants):
    def __init__(self, display, gameStateManager, color, shirts, shirtSelect, shirtIndex1, shirtIndex2, shirtIndex3, shirtIndex4, furcolor, furindex, pants, pantsSelect, pantsIndex1, pantsIndex2, pantsIndex3, pantsIndex4, sweater, sweaterSelect, sweaterIndex1, sweaterIndex2, sweaterIndex3, sweaterIndex4, accessories, shoes1, shoes2):
        super().__init__(display, gameStateManager, color, shirts, shirtSelect, shirtIndex1, shirtIndex2, shirtIndex3, shirtIndex4, furcolor, furindex, pants, pantsSelect, pantsIndex1, pantsIndex2, pantsIndex3, pantsIndex4, sweater, accessories, shoes1, shoes2)
        self.sweater = [r'asset\empty.png', r'asset\Sweater\Blue/'+str(self.color)+'.png', r'asset\Sweater\Cardigan/'+str(self.color)+'.png', r'asset\Sweater\Jacket/'+str(self.color)+'.png', r'asset\Sweater\Sweater/'+str(self.color)+'.png', r'asset\Sweater\Purple/'+str(self.color)+'.png', r'asset\Sweater\SweaterVest/'+str(self.color)+'.png', r'asset\Sweater\crewneck/'+str(self.color)+'.png']
        self.sweaterSelect = [r'asset\button\no.png', r'asset\Sweater\Blue/'+str(self.color)+'.png', r'asset\Sweater\Cardigan/'+str(self.color)+'.png', r'asset\Sweater\Jacket/'+str(self.color)+'.png', r'asset\Sweater\Sweater/'+str(self.color)+'.png', r'asset\Sweater\Purple/'+str(self.color)+'.png', r'asset\Sweater\SweaterVest/'+str(self.color)+'.png', r'asset\Sweater\crewneck/'+str(self.color)+'.png']
        self.sweaterIndex1 = sweaterIndex1
        self.sweaterIndex1 = 0
        self.sweaterIndex2 = sweaterIndex2
        self.sweaterIndex2 = 2
        self.sweaterIndex3 = sweaterIndex3
        self.sweaterIndex3 = 1
        self.sweaterIndex4 = sweaterIndex4
        self.sweaterIndex4 = 3
    def navBar(self):
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
    def arrowButtons(self):
        self.sweater = [r'asset\empty.png', r'asset\Sweater\Blue/'+str(self.color)+'.png', r'asset\Sweater\Cardigan/'+str(self.color)+'.png', r'asset\Sweater\Jacket/'+str(self.color)+'.png', r'asset\Sweater\Sweater/'+str(self.color)+'.png', r'asset\Sweater\Purple/'+str(self.color)+'.png', r'asset\Sweater\SweaterVest/'+str(self.color)+'.png', r'asset\Sweater\crewneck/'+str(self.color)+'.png']
        self.sweaterSelect = [r'asset\button\no.png', r'asset\Sweater\Blue/'+str(self.color)+'.png', r'asset\Sweater\Cardigan/'+str(self.color)+'.png', r'asset\Sweater\Jacket/'+str(self.color)+'.png', r'asset\Sweater\Sweater/'+str(self.color)+'.png', r'asset\Sweater\Purple/'+str(self.color)+'.png', r'asset\Sweater\SweaterVest/'+str(self.color)+'.png', r'asset\Sweater\crewneck/'+str(self.color)+'.png']
        if rightArrowB.draw():
            if self.sweaterIndex1 < len(self.sweater) - 3:
                self.sweaterIndex1 += 2
            else:
                self.sweaterIndex1 = 0
            if self.sweaterIndex2 < len(self.sweater) - 3:
                self.sweaterIndex2 += 2
            else:
                self.sweaterIndex2 = 0
            if self.sweaterIndex3 < len(self.sweater) - 2:
                self.sweaterIndex3 += 2
            else:
                self.sweaterIndex3 = 1
            if self.sweaterIndex4 < len(self.sweater) - 2:
                self.sweaterIndex4 += 2
            else:
                self.sweaterIndex4 = 1
        if leftArrowB.draw():
            if self.sweaterIndex1 >= 2:
                self.sweaterIndex1 -= 2
            else:
                self.sweaterIndex1 = len(self.sweater) - 2
            if self.sweaterIndex2 >= 2:
                self.sweaterIndex2 -= 2
            else:
                self.sweaterIndex2 = len(self.sweater) - 2
            if self.sweaterIndex3 >= 3:
                self.sweaterIndex3 -= 2
            else:
                self.sweaterIndex3 = len(self.sweater) - 1
            if self.sweaterIndex4 >= 3:
                self.sweaterIndex4 -= 2
            else:
                self.sweaterIndex4 = len(self.sweater) - 1
        sweaterBlit1 = pygame.image.load(self.sweaterSelect[self.sweaterIndex1])
        sweaterBlit2 = pygame.image.load(self.sweaterSelect[self.sweaterIndex2])
        sweaterBlit3 = pygame.image.load(self.sweaterSelect[self.sweaterIndex3])
        sweaterBlit4 = pygame.image.load(self.sweaterSelect[self.sweaterIndex4])
        sweaterBlit1B = Button(445,175, sweaterBlit1)
        sweaterBlit2B = Button(555,175, sweaterBlit2)
        sweaterBlit3B = Button(445,285, sweaterBlit3)
        sweaterBlit4B = Button(555,285, sweaterBlit4)
        if sweaterBlit1B.draw():
            self.gameStateManager.setSweaterDraw(pygame.image.load(self.sweater[self.sweaterIndex1]))
        if sweaterBlit2B.draw():
            self.gameStateManager.setSweaterDraw(pygame.image.load(self.sweater[self.sweaterIndex2]))
        if sweaterBlit3B.draw():
            self.gameStateManager.setSweaterDraw(pygame.image.load(self.sweater[self.sweaterIndex3]))
        if sweaterBlit4B.draw():
            self.gameStateManager.setSweaterDraw(pygame.image.load(self.sweater[self.sweaterIndex4]))
    def singleShuffle(self):
        if ShuffleB.draw():
            self.randomColor = random.randint(0,9)
            self.sweaterPaths = [path.replace(str(self.color), str(self.randomColor)) for path in self.sweater]
            self.random = random.randint(1,len(self.sweater)-1)
            self.gameStateManager.setSweaterDraw(pygame.image.load(self.sweaterPaths[self.random]))
    def run(self):
        Universal.restart(self)
        Universal.fullShuffle(self)
        Sweater.navBar(self)
        drawColorSelect.colorSelect(self)
        Sweater.arrowButtons(self)
        Sweater.singleShuffle(self)
        Universal.draw(self)

class Accessories(Sweater):
    def __init__(self, display, gameStateManager, color, shirts, shirtSelect, shirtIndex1, shirtIndex2, shirtIndex3, shirtIndex4, furcolor, furindex, pants, pantsSelect, pantsIndex1, pantsIndex2, pantsIndex3, pantsIndex4, sweater, SweaterSelect, sweaterIndex1, sweaterIndex2, sweaterIndex3, sweaterIndex4, accessories, accessoriesSelect, accTIndex1, accTIndex2, accTIndex3, accBIndex1, accBIndex2, accBIndex3, shoes1, shoes2):
        super().__init__(display, gameStateManager, color, shirts, shirtSelect, shirtIndex1, shirtIndex2, shirtIndex3, shirtIndex4, furcolor, furindex, pants, pantsSelect, pantsIndex1, pantsIndex2, pantsIndex3, pantsIndex4, sweater, SweaterSelect, sweaterIndex1, sweaterIndex2, sweaterIndex3, sweaterIndex4, accessories, shoes1, shoes2)
        self.accTIndex1 = accTIndex1
        self.accTIndex1 = 0
        self.accTIndex2 = accTIndex2
        self.accTIndex2 = 1
        self.accTIndex3 = accTIndex3
        self.accTIndex3 = 2
        self.accBIndex1 = accBIndex1
        self.accBIndex1 = 0
        self.accBIndex2 = accBIndex2
        self.accBIndex2 = 1
        self.accBIndex3 = accBIndex3
        self.accBIndex3 = 2
        self.accessories = [r'asset\empty.png', r'asset\accessories\tie/'+str(self.color)+'.png', r'asset\accessories\scarf/'+str(self.color)+'.png', r'asset\accessories\hat/'+str(self.color)+'.png', r'asset\accessories\ingles/'+str(self.color)+'.png', r'asset\accessories\bigHat/'+str(self.color)+'.png', r'asset\accessories\watch/'+str(self.color)+'.png', r'asset\accessories\bow/'+str(self.color)+'.png', r'asset\accessories\necklace/'+str(self.color)+'.png', r'asset\accessories\purse/'+str(self.color)+'.png']
        self.accessoriesSelect = [r'asset\button\no.png', r'asset\accessories\tie/'+str(self.color)+'.png', r'asset\accessories\scarf/'+str(self.color)+'.png', r'asset\accessories\hat/'+str(self.color)+'.png', r'asset\accessories\ingles/'+str(self.color)+'.png', r'asset\accessories\bigHat/'+str(self.color)+'.png', r'asset\accessories\watch/'+str(self.color)+'.png', r'asset\accessories\bow/'+str(self.color)+'.png', r'asset\accessories\necklace/'+str(self.color)+'.png', r'asset\accessories\purse/'+str(self.color)+'.png']
    def navBar(self):
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
    def arrowButtons(self):
        self.accessories = [r'asset\empty.png', r'asset\accessories\tie/'+str(self.color)+'.png', r'asset\accessories\scarf/'+str(self.color)+'.png', r'asset\accessories\hat/'+str(self.color)+'.png', r'asset\accessories\ingles/'+str(self.color)+'.png', r'asset\accessories\bigHat/'+str(self.color)+'.png', r'asset\accessories\watch/'+str(self.color)+'.png', r'asset\accessories\bow/'+str(self.color)+'.png', r'asset\accessories\necklace/'+str(self.color)+'.png', r'asset\accessories\purse/'+str(self.color)+'.png']
        self.accessoriesSelect = [r'asset\button\no.png', r'asset\accessories\tie/'+str(self.color)+'.png', r'asset\accessories\scarf/'+str(self.color)+'.png', r'asset\accessories\hat/'+str(self.color)+'.png', r'asset\accessories\ingles/'+str(self.color)+'.png', r'asset\accessories\bigHat/'+str(self.color)+'.png', r'asset\accessories\watch/'+str(self.color)+'.png', r'asset\accessories\bow/'+str(self.color)+'.png', r'asset\accessories\necklace/'+str(self.color)+'.png', r'asset\accessories\purse/'+str(self.color)+'.png']
        if rightTopArrowB.draw():
            if self.accTIndex1 < len(self.accessories) - 1:
                self.accTIndex1 += 1
            else:
                self.accTIndex1 = 0
            if self.accTIndex2 < len(self.accessories) - 1:
                self.accTIndex2 += 1
            else:
                self.accTIndex2 = 0
            if self.accTIndex3 < len(self.accessories) - 1:
                self.accTIndex3 += 1
            else:
                self.accTIndex3 = 0
        if leftTopArrowB.draw():
            if self.accTIndex1 > 0:
                self.accTIndex1 -= 1
            else:
                self.accTIndex1 = len(self.accessories) - 1
            if self.accTIndex2 > 0:
                self.accTIndex2 -= 1
            else:
                self.accTIndex2 = len(self.accessories) - 1
            if self.accTIndex3 > 0:
                self.accTIndex3 -= 1
            else:
                self.accTIndex3 = len(self.accessories) - 1
        if rightBotArrowB.draw():
            if self.accBIndex1 < len(self.accessories) - 1:
                self.accBIndex1 += 1
            else:
                self.accBIndex1 = 0
            if self.accBIndex2 < len(self.accessories) - 1:
                self.accBIndex2 += 1
            else:
                self.accBIndex2 = 0
            if self.accBIndex3 < len(self.accessories) - 1:
                self.accBIndex3 += 1
            else:
                self.accBIndex3 = 0
        if leftBotArrowB.draw():
            if self.accBIndex1 > 0:
                self.accBIndex1 -= 1
            else:
                self.accBIndex1 = len(self.accessories) - 1
            if self.accBIndex2 > 0:
                self.accBIndex2 -= 1
            else:
                self.accBIndex2 = len(self.accessories) - 1
            if self.accBIndex3 > 0:
                self.accBIndex3 -= 1
            else:
                self.accBIndex3 = len(self.accessories) - 1
        AccTBlit1 = pygame.image.load(self.accessoriesSelect[self.accTIndex1])
        AccTBlit2 = pygame.image.load(self.accessoriesSelect[self.accTIndex2])
        AccTBlit3 = pygame.image.load(self.accessoriesSelect[self.accTIndex3])
        AccBBlit1 = pygame.image.load(self.accessoriesSelect[self.accBIndex1])
        AccBBlit2 = pygame.image.load(self.accessoriesSelect[self.accBIndex2])
        AccBBlit3 = pygame.image.load(self.accessoriesSelect[self.accBIndex3])

        AccTBlit1B = Button(400,170, AccTBlit1)
        AccTBlit2B = Button(510,170, AccTBlit2)
        AccTBlit3B = Button(630,170, AccTBlit3)
        AccBBlit1B = Button(410,290, AccBBlit1)
        AccBBlit2B = Button(520,290, AccBBlit2)
        AccBBlit3B = Button(630,290, AccBBlit3)
        if AccTBlit1B.draw():
            self.gameStateManager.setAccessories1Draw(pygame.image.load(self.accessories[self.accTIndex1]))
        if AccTBlit2B.draw():
            self.gameStateManager.setAccessories1Draw(pygame.image.load(self.accessories[self.accTIndex2]))
        if AccTBlit3B.draw():
            self.gameStateManager.setAccessories1Draw(pygame.image.load(self.accessories[self.accTIndex3]))
        if AccBBlit1B.draw():
            self.gameStateManager.setAccessories2Draw(pygame.image.load(self.accessories[self.accBIndex1]))
        if AccBBlit2B.draw():
            self.gameStateManager.setAccessories2Draw(pygame.image.load(self.accessories[self.accBIndex2]))
        if AccBBlit3B.draw():
            self.gameStateManager.setAccessories2Draw(pygame.image.load(self.accessories[self.accBIndex3]))
    def singleShuffle(self):
        if ShuffleB.draw():
            self.randomColor1 = random.randint(0,9)
            self.accessoriesPaths1 = [path.replace(str(self.color), str(self.randomColor1)) for path in self.accessories]
            self.random1 = random.randint(0,len(self.accessories)-1)
            self.gameStateManager.setAccessories1Draw(pygame.image.load(self.accessoriesPaths1[self.random1]))
            self.randomColor2 = random.randint(0,9)
            self.accessoriesPaths2 = [path.replace(str(self.color), str(self.randomColor2)) for path in self.accessories]
            self.random2 = random.randint(0,len(self.accessories)-1)
            self.gameStateManager.setAccessories2Draw(pygame.image.load(self.accessoriesPaths2[self.random2]))
    def run(self):
        Universal.restart(self)
        Universal.fullShuffle(self)
        Accessories.navBar(self)
        drawColorSelect.colorSelect(self)
        Accessories.arrowButtons(self)
        Accessories.singleShuffle(self)
        Universal.draw(self)

class Shoes(Accessories):
    def __init__(self, display, gameStateManager, color, shirts, shirtSelect, shirtIndex1, shirtIndex2, shirtIndex3, shirtIndex4, furcolor, furindex, pants, pantsSelect, pantsIndex1, pantsIndex2, pantsIndex3, pantsIndex4, sweater, sweaterSelect, sweaterIndex1, sweaterIndex2, sweaterIndex3, sweaterIndex4, accessories, accessoriesSelect, accTIndex1, accTIndex2, accTIndex3, accBIndex1, accBIndex2, accBIndex3, shoes1, shoes2, shoeSelect1, shoeSelect2, shoesTIndex1, shoesTIndex2, shoesTIndex3, shoesBIndex1, shoesBIndex2, shoesBIndex3):
        super().__init__(display, gameStateManager, color, shirts, shirtSelect, shirtIndex1, shirtIndex2, shirtIndex3, shirtIndex4, furcolor, furindex, pants, pantsSelect, pantsIndex1, pantsIndex2, pantsIndex3, pantsIndex4, sweater, sweaterSelect, sweaterIndex1, sweaterIndex2, sweaterIndex3, sweaterIndex4, accessories, accessoriesSelect, accTIndex1, accTIndex2, accTIndex3, accBIndex1, accBIndex2, accBIndex3, shoes1, shoes2)
        self.shoesTIndex1 = shoesTIndex1
        self.shoesTIndex1 = 0
        self.shoesTIndex2 = shoesTIndex2
        self.shoesTIndex2 = 1
        self.shoesTIndex3 = shoesTIndex3
        self.shoesTIndex3 = 2
        self.shoesBIndex1 = shoesBIndex1
        self.shoesBIndex1 = 0
        self.shoesBIndex2 = shoesBIndex2
        self.shoesBIndex2 = 1
        self.shoesBIndex3 = shoesBIndex3
        self.shoesBIndex3 = 2
        self.shoes2 = [r'asset\empty.png', r'asset\shoe\shoe\converse/'+str(self.color)+'.png', r'asset\shoe\shoe\loaf/'+str(self.color)+'.png', r'asset\shoe\shoe\mj/'+str(self.color)+'.png', r'asset\shoe\shoe\sneek/'+str(self.color)+'.png']
        self.shoes1 = [r'asset\empty.png', r'asset\shoe\sock\shortSock/'+str(self.color)+'.png', r'asset\shoe\sock\tallSock/'+str(self.color)+'.png', r'asset\shoe\sock\tights/'+str(self.color)+'.png', r'asset\shoe\sock\legging/'+str(self.color)+'.png']
        self.shoeSelect2 = [r'asset\button\no.png', r'asset\shoe\shoe\converse/'+str(self.color)+'.png', r'asset\shoe\shoe\loaf/'+str(self.color)+'.png', r'asset\shoe\shoe\mj/'+str(self.color)+'.png', r'asset\shoe\shoe\sneek/'+str(self.color)+'.png']
        self.shoeSelect1 = [r'asset\button\no.png', r'asset\shoe\sock\shortSock/'+str(self.color)+'.png', r'asset\shoe\sock\tallSock/'+str(self.color)+'.png', r'asset\shoe\sock\tights/'+str(self.color)+'.png', r'asset\shoe\sock\legging/'+str(self.color)+'.png']
    def navBar(self):
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
    def arrowButtons(self):
        self.shoes2 = [r'asset\empty.png', r'asset\shoe\shoe\converse/'+str(self.color)+'.png', r'asset\shoe\shoe\loaf/'+str(self.color)+'.png', r'asset\shoe\shoe\mj/'+str(self.color)+'.png', r'asset\shoe\shoe\sneek/'+str(self.color)+'.png']
        self.shoes1 = [r'asset\empty.png', r'asset\shoe\sock\shortSock/'+str(self.color)+'.png', r'asset\shoe\sock\tallSock/'+str(self.color)+'.png', r'asset\shoe\sock\tights/'+str(self.color)+'.png', r'asset\shoe\sock\legging/'+str(self.color)+'.png']
        self.shoeSelect2 = [r'asset\button\no.png', r'asset\shoe\shoe\converse/'+str(self.color)+'.png', r'asset\shoe\shoe\loaf/'+str(self.color)+'.png', r'asset\shoe\shoe\mj/'+str(self.color)+'.png', r'asset\shoe\shoe\sneek/'+str(self.color)+'.png']
        self.shoeSelect1 = [r'asset\button\no.png', r'asset\shoe\sock\shortSock/'+str(self.color)+'.png', r'asset\shoe\sock\tallSock/'+str(self.color)+'.png', r'asset\shoe\sock\tights/'+str(self.color)+'.png', r'asset\shoe\sock\legging/'+str(self.color)+'.png']
        if rightTopArrowB.draw():
            if self.shoesTIndex1 < len(self.shoes1) - 1:
                self.shoesTIndex1 += 1
            else:
                self.shoesTIndex1 = 0
            if self.shoesTIndex2 < len(self.shoes1) - 1:
                self.shoesTIndex2 += 1
            else:
                self.shoesTIndex2 = 0
            if self.shoesTIndex3 < len(self.shoes1) - 1:
                self.shoesTIndex3 += 1
            else:
                self.shoesTIndex3 = 0
        if leftTopArrowB.draw():
            if self.shoesTIndex1 > 0:
                self.shoesTIndex1 -= 1
            else:
                self.shoesTIndex1 = len(self.shoes1) - 1
            if self.shoesTIndex2 > 0:
                self.shoesTIndex2 -= 1
            else:
                self.shoesTIndex2 = len(self.shoes1) - 1
            if self.shoesTIndex3 > 0:
                self.shoesTIndex3 -= 1
            else:
                self.shoesTIndex3 = len(self.shoes1) - 1
        if rightBotArrowB.draw():
            if self.shoesBIndex1 < len(self.shoes2) - 1:
                self.shoesBIndex1 += 1
            else:
                self.shoesBIndex1 = 0
            if self.shoesBIndex2 < len(self.shoes2) - 1:
                self.shoesBIndex2 += 1
            else:
                self.shoesBIndex2 = 0
            if self.shoesBIndex3 < len(self.shoes2) - 1:
                self.shoesBIndex3 += 1
            else:
                self.shoesBIndex3 = 0
        if leftBotArrowB.draw():
            if self.shoesBIndex1 > 0:
                self.shoesBIndex1 -= 1
            else:
                self.shoesBIndex1 = len(self.shoes2) - 1
            if self.shoesBIndex2 > 0:
                self.shoesBIndex2 -= 1
            else:
                self.shoesBIndex2 = len(self.shoes2) - 1
            if self.shoesBIndex3 > 0:
                self.shoesBIndex3 -= 1
            else:
                self.shoesBIndex3 = len(self.shoes2) - 1
        ShoesTBlit1 = pygame.image.load(self.shoeSelect1[self.shoesTIndex1])
        ShoesTBlit2 = pygame.image.load(self.shoeSelect1[self.shoesTIndex2])
        ShoesTBlit3 = pygame.image.load(self.shoeSelect1[self.shoesTIndex3])
        ShoesBBlit1 = pygame.image.load(self.shoeSelect2[self.shoesBIndex1])
        ShoesBBlit2 = pygame.image.load(self.shoeSelect2[self.shoesBIndex2])
        ShoesBBlit3 = pygame.image.load(self.shoeSelect2[self.shoesBIndex3])

        ShoesTBlit1B = Button(400,170, ShoesTBlit1)
        ShoesTBlit2B = Button(510,170, ShoesTBlit2)
        ShoesTBlit3B = Button(630,170, ShoesTBlit3)
        ShoesBBlit1B = Button(410,290, ShoesBBlit1)
        ShoesBBlit2B = Button(520,290, ShoesBBlit2)
        ShoesBBlit3B = Button(630,290, ShoesBBlit3)
        if ShoesTBlit1B.draw():
            self.gameStateManager.setShoes1Draw(pygame.image.load(self.shoes1[self.shoesTIndex1]))
        if ShoesTBlit2B.draw():
            self.gameStateManager.setShoes1Draw(pygame.image.load(self.shoes1[self.shoesTIndex2]))
        if ShoesTBlit3B.draw():
            self.gameStateManager.setShoes1Draw(pygame.image.load(self.shoes1[self.shoesTIndex3]))
        if ShoesBBlit1B.draw():
            self.gameStateManager.setShoes2Draw(pygame.image.load(self.shoes2[self.shoesBIndex1]))
        if ShoesBBlit2B.draw():
            self.gameStateManager.setShoes2Draw(pygame.image.load(self.shoes2[self.shoesBIndex2]))
        if ShoesBBlit3B.draw():
            self.gameStateManager.setShoes2Draw(pygame.image.load(self.shoes2[self.shoesBIndex3]))
    def singleShuffle(self):
        if ShuffleB.draw():
            self.randomColor1 = random.randint(0,9)
            self.shoesPaths1 = [path.replace(str(self.color), str(self.randomColor1)) for path in self.shoes1]
            self.random1 = random.randint(0,len(self.shoes1)-1)
            self.gameStateManager.setShoes1Draw(pygame.image.load(self.shoesPaths1[self.random1]))
            self.randomColor2 = random.randint(0,9)
            self.shoesPaths2 = [path.replace(str(self.color), str(self.randomColor2)) for path in self.shoes2]
            self.random2 = random.randint(0,len(self.shoes2)-1)
            self.gameStateManager.setShoes2Draw(pygame.image.load(self.shoesPaths2[self.random2]))
    def run(self):
        Universal.restart(self)
        Universal.fullShuffle(self)
        Shoes.navBar(self)
        drawColorSelect.colorSelect(self)
        Shoes.arrowButtons(self)
        Shoes.singleShuffle(self)
        Universal.draw(self)

class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
        self.characterDraw = pygame.image.load(r'asset/character/black.png')
        self.shirtDraw = pygame.image.load(r'asset\empty.png')
        self.pantsDraw = pygame.image.load(r'asset\empty.png')
        self.sweaterDraw = pygame.image.load(r'asset\empty.png')
        self.accessories1Draw = pygame.image.load(r'asset\empty.png')
        self.accessories2Draw = pygame.image.load(r'asset\empty.png')
        self.shoes1Draw = pygame.image.load(r'asset\empty.png')
        self.shoes2Draw = pygame.image.load(r'asset\empty.png')
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
    def setShirtDraw(self, shirt): 
        self.shirtDraw = shirt
    def getPantsDraw(self):
        return self.pantsDraw
    def setPantsDraw(self, pants):
        self.pantsDraw = pants
    def getSweaterDraw(self):
        return self.sweaterDraw
    def setSweaterDraw(self, sweater):
        self.sweaterDraw = sweater
    def getAccessories1Draw(self):
        return self.accessories1Draw
    def setAccessories1Draw(self, accessories1):
        self.accessories1Draw = accessories1
    def getAccessories2Draw(self):
        return self.accessories2Draw
    def setAccessories2Draw(self, accessories2):
        self.accessories2Draw = accessories2
    def getShoes1Draw(self):
        return self.shoes1Draw
    def setShoes1Draw(self, shoes1):
        self.shoes1Draw = shoes1
    def getShoes2Draw(self):
        return self.shoes2Draw
    def setShoes2Draw(self, shoes2):
        self.shoes2Draw = shoes2

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Cat Dress Up")

        self.gameStateManager = GameStateManager('start')
        self.furcolor = []
        self.furindex = []
        self.color = 9
        self.shirts = []
        self.shirtSelect = []
        self.shirtIndex1 = 0
        self.shirtIndex2 = 2
        self.shirtIndex3 = 1
        self.shirtIndex4 = 3
        self.x = 632
        self.pants = []
        self.pantsSelect = []
        self.pantsIndex1 = 0
        self.pantsIndex2 = 2
        self.pantsIndex3 = 1
        self.pantsIndex4 = 3
        self.sweater = []
        self.sweaterSelect = []
        self.sweaterIndex1 = 0
        self.sweaterIndex2 = 2
        self.sweaterIndex3 = 1
        self.sweaterIndex4 = 3
        self.accTIndex1 = 0
        self.accTIndex2 = 1
        self.accTIndex3 = 2
        self.accBIndex1 = 0
        self.accBIndex2 = 1
        self.accBIndex3 = 2
        self.shoesTIndex1 = 0
        self.shoesTIndex2 = 1
        self.shoesTIndex3 = 2
        self.shoesBIndex1 = 0
        self.shoesBIndex2 = 1
        self.shoesBIndex3 = 2
        self.accessories = []
        self.accessoriesSelect = []
        self.shoes1 = []
        self.shoes2 = []
        self.shoeSelect1 = []
        self.shoeSelect2 = []

        self.start = Start(self.screen, self.gameStateManager)
        self.Color = Color(self.screen, self.gameStateManager, self.furcolor, self.furindex, self.shirts, self.pants, self.sweater, self.accessories, self.shoes1, self.shoes2, self.color)
        self.Shirt = Shirt(self.screen, self.gameStateManager, self.color, self.shirtIndex1, self.shirtIndex2, self.shirtIndex3, self.shirtIndex4, self.furcolor, self.furindex, self.shirts, self.shirtSelect, self.pants, self.sweater, self.accessories, self.shoes1, self.shoes2)
        self.Pants = Pants(self.screen, self.gameStateManager, self.color, self.shirtIndex1, self.shirtIndex2, self.shirtIndex3, self.shirtIndex4, self.furcolor, self.furindex, self.pantsIndex1, self.pantsIndex2, self.pantsIndex3, self.pantsIndex4, self.shirts, self.shirtSelect, self.pants, self.pantsSelect, self.sweater, self.accessories, self.shoes1, self.shoes2)
        self.Sweater = Sweater(self.screen, self.gameStateManager, self.color, self.shirtIndex1, self.shirtIndex2, self.shirtIndex3, self.shirtIndex4, self.furcolor, self.furindex, self.pantsIndex1, self.pantsIndex2, self.pantsIndex3, self.pantsIndex4, self.sweaterIndex1, self.sweaterIndex2, self.sweaterIndex3, self.sweaterIndex4, self.shirts, self.shirtSelect, self.pants, self.pantsSelect, self.sweater, self.sweaterSelect, self.accessories, self.shoes1, self.shoes2)
        self.Accessories = Accessories(self.screen, self.gameStateManager, self.color, self.shirtIndex1, self.shirtIndex2, self.shirtIndex3, self.shirtIndex4, self.furcolor, self.furindex, self.pantsIndex1, self.pantsIndex2, self.pantsIndex3, self.pantsIndex4, self.sweaterIndex1, self.sweaterIndex2, self.sweaterIndex3, self.sweaterIndex4, self.accTIndex1, self.accTIndex2, self.accTIndex3, self.accBIndex1, self.accBIndex2, self.accBIndex3, self.shirts, self.shirtSelect, self.pants, self.pantsSelect, self.sweater, self.sweaterSelect, self.accessories, self.accessoriesSelect, self.shoes1, self.shoes2)
        self.Shoes = Shoes(self.screen, self.gameStateManager, self.color, self.shirtIndex1, self.shirtIndex2, self.shirtIndex3, self.shirtIndex4, self.furcolor, self.furindex, self.pantsIndex1, self.pantsIndex2, self.pantsIndex3, self.pantsIndex4, self.sweaterIndex1, self.sweaterIndex2, self.sweaterIndex3, self.sweaterIndex4, self.accTIndex1, self.accTIndex2, self.accTIndex3, self.accBIndex1, self.accBIndex2, self.accBIndex3, self.shoesTIndex1, self.shoesTIndex2, self.shoesTIndex3, self.shoesBIndex1, self.shoesBIndex2, self.shoesBIndex3,  self.shirts, self.shirtSelect, self.pants, self.pantsSelect, self.sweater, self.sweaterSelect, self.accessories, self.accessoriesSelect, self.shoes1, self.shoes2, self.shoeSelect1, self.shoeSelect2)

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