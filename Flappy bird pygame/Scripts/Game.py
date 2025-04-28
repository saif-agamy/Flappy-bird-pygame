import pygame
import sys
from Player import Player
from AssetsLoader import LoadAsset
from Tiles import Tile
from Floor import Floor

pygame.init() #Call pygame modules

class Game :
    def __init__(self):
        self.screen = pygame.display.set_mode((720,480))#Make the main screen
        self.display = pygame.Surface((360, 240)) #make a smaller one to scale it to the bigger one
        
        #setting up camera
        self.CameraPosX = 0

        self.Font = pygame.font.SysFont(None, 48,True)#The font of the score Text
        self.Font2 = pygame.font.SysFont(None, 24,False)#The font of the score Text

        self.player = Player(self,(50,144-16),0.01)#The player 

        #Game Assets
        self.Assets = {
            "Player" : LoadAsset("Player.png",Rect=(0,0,16,16)),
            "Tile_Type_1" :  LoadAsset("Tiles.png",Rect=(0,0,32,80)),#green
            "Tile_Type_2" : LoadAsset("Tiles.png",Rect=(32,0,32,80)),#yellow
            "Tile_Type_3" : LoadAsset("Tiles.png",Rect=(64,0,32,80)),#red
            "Tile_Type_4" : LoadAsset("Tiles.png",Rect=(96,0,32,80)),#blue    
            "Background" : LoadAsset("Background.png"),
            "Floor" : LoadAsset("SimpleStyle1.png",Rect=(0,80,64,32)) 
        }

        self.lostScreen = pygame.Surface((self.display.get_width()/2,self.display.get_height()/2))

        self.floor = Floor(self,[0,210],6)

        #To control frame rate
        self.Clock = pygame.Clock()

        #The Tile which we give the beginig of them and the size of them
        self.Tile = Tile(self,(200 ,self.display.get_height()/2-50),[32,80])

    def run(self):
        while True :
            #set a color to the main screen
            self.display.blit(pygame.transform.scale(self.Assets["Background"],(self.display.get_width(),self.display.get_height())),(0,0)) 

            #moving camera
            if not self.player.playerLost :
                self.CameraPosX += 1 

            #player settings
            self.player.Update() # to upadte every frame the player status
            self.player.Render() # to render the player every frame 

            #Tiling
            self.Tile.update()#(adding / removing / moving) Tiles
            self.Tile.render()

            #print player Score
            Text = self.Font.render(str(self.player.playerScore),True,(255,255,0))
            if not self.player.playerLost :
                self.display.blit(Text,(self.display.get_width()/2-  Text.get_width()/2,10))

            #the floor 
            self.floor.update()
            self.floor.Render()

            LoseText = self.Font2.render("Your Lost!",True,(255,0,0))
            LastScoreText = self.Font2.render("Your Score is : " + str(self.player.LastScore),True,(0,255,0))

            if self.player.playerLost :

                self.lostScreen.fill((255,255,0))
                self.lostScreen.blit(LoseText,(self.lostScreen.get_width()/2 - LoseText.get_width()/2,(self.lostScreen.get_height()/2 - LoseText.get_height()/2)-25))
                self.lostScreen.blit(LastScoreText,(self.lostScreen.get_width()/2 - LastScoreText.get_width()/2,(self.lostScreen.get_height()/2 - LastScoreText.get_height()/2)+25))
                self.display.blit(self.lostScreen,(self.display.get_width()/2 - self.lostScreen.get_width()/2,self.display.get_height()/2 - self.lostScreen.get_height()/2))
                
      
            #Scale up the smaller screen to the main one
            self.screen.blit(pygame.transform.scale(self.display,(self.screen.get_width(),self.screen.get_height())),(0,0))
            self.screen.blit(pygame.transform.scale(self.display,(self.screen.get_width(),self.screen.get_height())),(0,0))

            #loop over all game events
            for event in pygame.event.get() :
                #Exist the game
                if event.type == pygame.QUIT :
                    pygame.quit() #stop pygame modules
                    sys.exit() #stop the code it self
                
                #Check space key for jumping
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_SPACE :
                        self.player.jump = True
                if event.type == pygame.KEYUP :
                    if event.key == pygame.K_SPACE :
                        self.player.jump = False 
            
            self.Clock.tick(60)#make the game 60 fps or lower
            pygame.display.update()#update the smaller display

game = Game()#game instance
game.run()#Running the game
