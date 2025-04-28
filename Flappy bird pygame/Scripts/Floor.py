import pygame 

class Floor :
    def __init__(self,game,pos,TilesNum) :
        self.game = game 
        self.pos = pos
        self.floorTiles = {

        }
        self.TilesNum = TilesNum

    def update(self) :
        if len(self.floorTiles) < self.TilesNum :
            for Tile in range(1,self.TilesNum + 1) : 
                self.floorTiles["Floor_" + str(Tile)] = {
                    "AssetName" : "Floor",
                    "pos" : [(Tile * (self.pos[0] + 64))-64,self.pos[1]]
                }

    def Render(self) : 
        if len(self.floorTiles) > 0 :
            for floor in self.floorTiles :
                self.game.display.blit(self.game.Assets[self.floorTiles[floor]["AssetName"]],self.floorTiles[floor]["pos"]) 