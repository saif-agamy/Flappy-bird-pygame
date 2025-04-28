import pygame 
import sys

class Player :
    def __init__(self,game,pos,speed=0): 
        self.game = game#the game if we want any attribute or methods such as assets dic
        self.pos = list(pos)#the player position
        self.speed = speed#main player speed
        self.jump = False#is player jumping or not
        self.velocity = [0,0]#the increase or reduce rate of the player speed
        self.playerScore = 0
        self.NextTileRects = []
        self.RestartInt = 0
        self.playerLost = False
        self.LastScore = 0
    
    #making the player collision
    def PlayerRect(self) :
        Rect = pygame.Rect(self.pos[0],self.pos[1],16,16)
        return Rect

    #Changing the player status every frame
    def Update(self) :
        #checking Tiles Rects
        PlayerRect = self.PlayerRect()

        #check the Next Tile 
        self.NextTileRects = self.game.Tile.TileRects(self.playerScore+1,self.game.CameraPosX)

        #if player collided with the Score Rect
        if PlayerRect.colliderect(self.NextTileRects[1]) :
            self.playerScore += 1
            self.RestartInt += 1
            self.LastScore = self.playerScore
        
        #If the player Collided with the Tile it self 
        if PlayerRect.colliderect(self.NextTileRects[0]) or PlayerRect.colliderect(self.NextTileRects[2]) :
            self.playerLost = True
            self.playerScore = 0#reset score

        if self.pos[1] > 210-16 :
            self.playerLost = True 


        self.velocity[1] += 0.1 #the gravity as a player pos increase rate in Y
        self.velocity[1] = min(5,self.velocity[1]) #Moving down in the speed lower than 5 or 5

        #if player is jumping
        if self.jump == True :
            self.velocity[1] = -2
            self.jump = False

        if self.playerLost :
            self.velocity[1] = 0

        self.pos[1] += self.velocity[1]

    #rendering the player
    def Render(self) :
        self.game.display.blit(self.game.Assets['Player'],self.pos)

