try:
    import pygame #requires pip install *
    importTest = pygame.image.load(r'asset\button\start.png')
except:
    print('please pip install pygame with the terminal command: python3 -m pip install -U pygame --user')
    print('if issues occur, please visit https://www.pygame.org/wiki/GettingStarted')