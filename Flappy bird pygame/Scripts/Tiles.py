import pygame
import random

class Tile :
    def __init__(self,game,pos,TileSize) :
        self.game = game
        self.pos = pos
        self.TileSize = TileSize
        self.Tiles = {}#Tiles in Game already
        self.Tiles["Tile_1"] = {
                    "Type" : "Tile_Type_1", 
                    "poses" : [[self.pos[0],self.pos[1] - 65],[self.pos[0],self.pos[1] + 65]],
                    "SidePoses" : [[self.pos[0],self.pos[1]-self.TileSize[1]-65],[self.pos[0],self.pos[1] + self.TileSize[1] + 65]]
                    }
        self.ColorInt = 1#The color of the Tile
        self.oldHeight = 0
        

    #Return 3 main Tile rects Two for tiles them self and one for score Tile
    def TileRects(self,TileNum,CameraPosX) :
        if "Tile_" + str(TileNum) in self.Tiles :
        # if len(self.Tiles) >= TileNum : #تقريبا لبمشكلة هنااااااااا 
            Tile = self.Tiles["Tile_" + str(TileNum)]
            UpperTileRect = pygame.Rect(Tile["poses"][0][0] - CameraPosX,Tile["poses"][0][1],self.TileSize[0],self.TileSize[1])
            BetweenTileRect = pygame.Rect(Tile["poses"][1][0]+31 - CameraPosX,Tile["poses"][1][1] - 50,self.TileSize[0]-30,50)
            DownTileRect = pygame.Rect(Tile["poses"][1][0] - CameraPosX,Tile["poses"][1][1],self.TileSize[0],self.TileSize[1])
            return [UpperTileRect,BetweenTileRect,DownTileRect]
    
    def generateTile(self,TilesNum) :
        for TileNum in range(1,TilesNum) :
            #changing the Tiles color
            self.ColorInt += 1
            if self.ColorInt == 5 :
                self.ColorInt = 1

            #Setting the Random Height every time we add Tile
            NearHeight = True 
            while NearHeight :
                TileHeight = random.choice([5,20,35])
                TileHeightSign = random.choice([-1,1])#To make it negative or positive
                TileHeight = TileHeight*TileHeightSign
                if TileHeight != self.oldHeight :
                    NearHeight = False       
                    
            self.Tiles["Tile_"+str(int(list(self.Tiles.keys())[-1][5:]) + 1)] = {
                    "Type" : "Tile_Type_" + str(self.ColorInt),
                    "poses" : [[self.Tiles[list(self.Tiles.keys())[-1]]["poses"][0][0] + (3*self.TileSize[0]), self.Tiles[list(self.Tiles.keys())[0]]["poses"][0][1] + TileHeight],
                            [self.Tiles[list(self.Tiles.keys())[-1]]["poses"][1][0] + (3*self.TileSize[0]), self.Tiles[list(self.Tiles.keys())[0]]["poses"][1][1] + TileHeight]],
                    "SidePoses" : [[self.Tiles[list(self.Tiles.keys())[-1]]["SidePoses"][0][0] + (3*self.TileSize[0]),self.Tiles[list(self.Tiles.keys())[0]]["SidePoses"][0][1] + TileHeight],
                                   [self.Tiles[list(self.Tiles.keys())[-1]]["SidePoses"][1][0] + (3*self.TileSize[0]),self.Tiles[list(self.Tiles.keys())[0]]["SidePoses"][1][1] + TileHeight]]
                    }
            
            self.oldHeight = TileHeight

    #what happening every frame 
    def update(self) :
        if self.game.player.RestartInt == 5 or len(self.Tiles) < 10 :
            self.generateTile(10) 
            self.game.player.RestartInt = 0
        
    
    def render(self) :
        #if there are any Tiles -> loop over them 
        if len(self.Tiles) > 0 :
            for Tile in self.Tiles :
                #we print twice because every Tile consist 2 pieces
                self.game.display.blit(self.game.Assets[self.Tiles[Tile]["Type"]],(self.Tiles[Tile]["poses"][0][0] - self.game.CameraPosX,self.Tiles[Tile]["poses"][0][1]))
                self.game.display.blit(self.game.Assets[self.Tiles[Tile]["Type"]],(self.Tiles[Tile]["poses"][1][0] - self.game.CameraPosX,self.Tiles[Tile]["poses"][1][1]))
                self.game.display.blit(self.game.Assets[self.Tiles[Tile]["Type"]],(self.Tiles[Tile]["SidePoses"][0][0] - self.game.CameraPosX,self.Tiles[Tile]["SidePoses"][0][1]))
                self.game.display.blit(self.game.Assets[self.Tiles[Tile]["Type"]],(self.Tiles[Tile]["SidePoses"][1][0] - self.game.CameraPosX,self.Tiles[Tile]["SidePoses"][1][1]))