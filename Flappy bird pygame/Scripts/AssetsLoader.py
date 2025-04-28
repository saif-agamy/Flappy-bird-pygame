import pygame 

def LoadAsset(FileName,Rect = None) :
    Asset = pygame.image.load("Game Assets\\" + FileName).convert()
    Asset.set_colorkey((0,0,0))

    if Rect == None :
        return Asset
    else :
        return Asset.subsurface(Rect)