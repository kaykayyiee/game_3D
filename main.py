from direct.showbase.ShowBase import ShowBase
from map_manager import MapManager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self) #membuat basenya
        self.land = MapManager() #membuat objek mapmanager yg terdiri dari porperti model, teksture, warna
        x,y = self.land.loadLand("land.txt") #membuat banyak blok
        self.hero = Hero((x//2,y//2,2), self.land)
        base.camLens.setFov(90)
        
game = Game()
game.run()