import pygame, sys, os, random, time
from pygame.locals import *

pygame.init()

size = w, h = (1000,600)
display = pygame.display.set_mode(size)
fps = pygame.time.Clock()
name =  pygame.display.set_caption('Tung Tung Simulator')
gameState =  "Title Screen"
shopState = "Tylenol"
font= pygame.font.SysFont("Franklin Gothic", 70)

class Assets:
    titleBackground = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "tungtung.jpeg")).convert(), (1000, 600))
    gameBackground =  pygame.image.load(os.path.join("Assets", "gameBackground.jpg")).convert()
    logo = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "SimulatorLogo.jpg")).convert(), (400,400))
    playButton = pygame.image.load(os.path.join("Assets", "PlayButton.jpg")).convert()
    buttonRect = playButton.get_rect(topleft = (550,250))
    store = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "tungStore.png")).convert_alpha(), (300,300))
    storeRect = store.get_rect(topleft = (50,75))
    catcherTung = pygame.image.load(os.path.join("Assets", "catcherTung.png")).convert_alpha() 
    catcherBackground = pygame.image.load(os.path.join("Assets", "catcherBackground.jpg")).convert() 
    eagle = pygame.image.load(os.path.join("Assets", "eagle.jpg")).convert() 
    angelTung = pygame.image.load(os.path.join("Assets", "angelTung.png")).convert_alpha() 
    storeBackground = pygame.image.load(os.path.join("Assets", "shopBackground.jpg")).convert()
    exitButton = pygame.image.load(os.path.join("Assets", "exitButton.jpg")).convert()
    exitRect = exitButton.get_rect(topleft = (900,30))
    tylenolPicture = pygame.image.load(os.path.join("Assets", "tungTylenol.png")).convert_alpha()
    buyButton = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "buyButton.jpg")).convert(), (200, 100))
    buyRect = buyButton.get_rect(topleft=(775,250))
    catcher = pygame.image.load(os.path.join("Assets", "catcher.png")).convert_alpha()
    rightArrow = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "rightArrow.jpg")).convert(), (70,70))
    leftArrow = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "leftArrow.jpg")).convert(), (70,70))
    leftRect = leftArrow.get_rect(topleft = (132,490))
    rightRect = rightArrow.get_rect(topleft = (800,490))

cost = 0
catcherActive = "No"

    

class Player:
   sprite = pygame.image.load(os.path.join("Assets", "BuffTung.png")).convert_alpha()
   liftingSprite = pygame.image.load(os.path.join("Assets", "buffLift.png")).convert_alpha()
   scaledSprite = pygame.transform.scale(sprite, (400,400))
   scaledLiftingSprite = pygame.transform.scale(liftingSprite, (400,400))
   midLiftingSprite = pygame.image.load(os.path.join("Assets", "midLift.png")).convert_alpha()
   isLifting = False
   liftTimer = 0
   liftDuration = 450
   strength = 0
   strengthMeter = font.render(f"Strength: {strength}", True, (0, 0, 0))
   tylenol = 0
   tylenolOwned = False
   angels = 0
   pass



def startGame():
    font = pygame.font.SysFont("Franklin Gothic", 70)
    Player.strengthMeter = font.render(f"Strength: {Player.strength}", True, (0, 0, 0))
    if Player.isLifting:
            scaledMid = pygame.transform.scale(Player.midLiftingSprite, (385,410))
            elapsed = pygame.time.get_ticks() - Player.liftTimer
            if elapsed < (Player.liftDuration)/3:
                Player.strengthMeter = font.render(f"Strength: {Player.strength}", True, (0, 0, 0))
                display.blit(Assets.gameBackground, (0,0))
                display.blit(scaledMid, (560,100))
                display.blit(Player.strengthMeter, (350,50))
                display.blit(Assets.store, (50,75))
                if Player.tylenolOwned == True:
                    scaledTylenol = pygame.transform.scale(Assets.tylenolPicture, (100,100))
                    display.blit(scaledTylenol, (520, 480))
                if Player.angels >= 1:
                    scaledAngel = pygame.transform.scale(Assets.angelTung, (100,150))
                    display.blit(scaledAngel, (530,340))
                pygame.display.update()
            elif elapsed > (Player.liftDuration)/3 and elapsed < 2*(Player.liftDuration)/3:
                display.blit(Assets.gameBackground, (0,0))
                display.blit(Player.scaledLiftingSprite, (550,100))
                display.blit(Player.strengthMeter, (350,50))
                display.blit(Assets.store, (50,75))
                if Player.tylenolOwned == True:
                    scaledTylenol = pygame.transform.scale(Assets.tylenolPicture, (100,100))
                    display.blit(scaledTylenol, (520, 480))
                if Player.angels >= 1:
                    scaledAngel = pygame.transform.scale(Assets.angelTung, (100,150))
                    display.blit(scaledAngel, (530,340))
                pygame.display.update()
            else:
                display.blit(Assets.gameBackground, (0,0))
                display.blit(Player.scaledSprite, (550,100))
                display.blit(Player.strengthMeter, (350,50))
                display.blit(Assets.store, (50,75))
                if Player.tylenolOwned == True:
                    scaledTylenol = pygame.transform.scale(Assets.tylenolPicture, (100,100))
                    display.blit(scaledTylenol, (520, 480))
                if Player.angels >= 1:
                    scaledAngel = pygame.transform.scale(Assets.angelTung, (100,150))
                    display.blit(scaledAngel, (530,340))
                pygame.display.update()
    else:
            display.blit(Assets.gameBackground, (0,0))
            display.blit(Player.scaledSprite, (550,100))
            display.blit(Player.strengthMeter, (350,50))
            display.blit(Assets.store, (50,75))
            if Player.tylenolOwned == True:
                scaledTylenol = pygame.transform.scale(Assets.tylenolPicture, (100,100))
                display.blit(scaledTylenol, (520, 480))
            if Player.angels >= 1:
                scaledAngel = pygame.transform.scale(Assets.angelTung, (100,150))
                display.blit(scaledAngel, (530,340))
            pygame.display.update()
    if Player.angels >= 1:
       scaledAngel = pygame.transform.scale(Assets.angelTung, (100,150))
       display.blit(scaledAngel, (530,340))
       Player.strength += int(1+ 0.5*Player.angels)
       pygame.time.wait(100)
    pygame.display.update()
    
def startShop():
    
    font = pygame.font.SysFont("Franklin Gothic", 40)
    strengthMeter = font.render(f"{Player.strength}", True, (255, 255, 255))
    display.fill((0,0,0))
    display.blit(Assets.storeBackground, (0,0)) 
    display.blit(strengthMeter, (90,47))
    display.blit(Assets.exitButton, (900,30))
    display.blit(Assets.buyButton, (775,250))
    display.blit(Assets.rightArrow, (800,490))
    display.blit(Assets.leftArrow, (132,490))
    if Player.angels >= 1:
       if catcherActive != "Yes":
        Player.strength += int(1 + 0.5*Player.angels)
        pygame.time.wait(100)
    if shopState == "Tylenol":
       cost = 5 + Player.tylenol*(Player.tylenol + 5)
       item = "Tylenol"
       scaledTylenol = pygame.transform.scale(Assets.tylenolPicture, (150,150))
       itemLabel = font.render(item, True, (0,0,0))
       itemAmount = font.render(f"Owned: {Player.tylenol}", True, (255,255,255))
       costMeter = font.render(f"Cost: {cost}", True, (255, 255, 255))
       
       display.blit(scaledTylenol, (425,150))
       display.blit(costMeter, (435,95)) 
       display.blit(itemLabel, (451,510))
       display.blit(itemAmount, (375,390))
    elif shopState == "Catcher":
       cost = 5000
       item = "Catcher in the Rye"
       scaledCatcher = pygame.transform.scale(Assets.catcher, (150,150))
       itemLabel = font.render(item, True, (0,0,0))
       itemAmount = font.render(f"Owned: {catcherActive}", True, (255, 255, 255))
       costMeter = font.render(f"Cost: {cost}", True, (255, 255, 255))
       
       display.blit(scaledCatcher, (425,150))
       display.blit(costMeter, (435,95)) 
       display.blit(itemLabel, (376,510))
       display.blit(itemAmount, (375,390))
    elif shopState == "Angel":
       cost = 100 + 100*Player.angels
       item = "Angel Sahur"
       scaledAngel = pygame.transform.scale(Assets.angelTung, (150,150))
       itemLabel = font.render(item, True, (0,0,0))
       itemAmount = font.render(f"Owned: {Player.angels}", True, (255, 255, 255))
       costMeter = font.render(f"Cost: {cost}", True, (255, 255, 255))
       
       display.blit(scaledAngel, (425,150))
       display.blit(costMeter, (435,95))
       display.blit(itemLabel, (414.5,510))
       display.blit(itemAmount, (375,390))
    if catcherActive == "Yes":
        Player.strength = 0
    pygame.display.update()

def startCatcher():
   scaledSadTung = pygame.transform.scale(Assets.catcherTung, (400,400))
   scaledCatcher = pygame.transform.scale(Assets.catcher,(300,300))
   display.fill((0,0,0))
   display.blit(Assets.catcherBackground, (0,0)) 
   display.blit(scaledSadTung, (550,100))
   display.blit(scaledCatcher, (50,75))
   pygame.display.update()

def draw_window(display, background):
    display.blit(Assets.titleBackground, (0,0)) 
    display.blit(Assets.logo, (100,100))
    display.blit(Assets.playButton, (550,250))
    pygame.display.update()

def lift():
    if gameState == "Start":
        Player.isLifting = True
        Player.liftTimer = pygame.time.get_ticks()
        x = 1 + Player.tylenol
        Player.strength += x

while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == MOUSEBUTTONDOWN:
        mousePos = event.pos
        if gameState == "Title Screen" and Assets.buttonRect.collidepoint(mousePos):
            print('Start Clicked')
            gameState = "Start"
            pass
        elif gameState == "Start" and Assets.storeRect.collidepoint(mousePos):
            print('Shop Clicked')
            gameState = "Shop"
        elif gameState == "Shop" and Assets.exitRect.collidepoint(mousePos):
            print('Exit Clicked')
            if catcherActive == "Yes":
                gameState = "Catcher"
            else:    
                gameState = "Start"
        elif gameState == "Shop" and Assets.buyRect.collidepoint(mousePos):
            if shopState == "Tylenol":
              if Player.strength >= 5 + Player.tylenol*(Player.tylenol + 5):
                    Player.strength -= 5 + Player.tylenol*(Player.tylenol + 5)
                    Player.tylenol += 1
                    Player.tylenolOwned = True
            elif shopState == "Catcher":
               if Player.strength >= 5000:
                    Player.strength -= 5000
                    catcherActive = "Yes"
            elif shopState == "Angel":
               if Player.strength >= 100 + 100*Player.angels:
                    Player.strength -= 100 + 100*Player.angels
                    Player.angels += 1
        elif gameState == "Shop" and Assets.rightRect.collidepoint(mousePos):
            if shopState == "Tylenol":
              shopState = "Angel"
            elif shopState == "Angel":
              shopState = "Catcher"
            elif shopState == "Catcher":
              shopState = "Tylenol"
        elif gameState == "Shop" and Assets.leftRect.collidepoint(mousePos):
            if shopState == "Catcher":
              shopState = "Angel"
            elif shopState == "Angel":
              shopState = "Tylenol"
            elif shopState == "Tylenol":
              shopState = "Catcher"
      elif event.type == KEYDOWN:
         if gameState == "Start" and event.key==pygame.K_SPACE:
            lift()
            pass
    if gameState == "Title Screen":
            draw_window(display, Assets.titleBackground)
    elif gameState == "Start":  
            startGame()
    elif gameState == "Shop":
            startShop()
    elif gameState == "Catcher":
            startCatcher()
    fps.tick(60)

