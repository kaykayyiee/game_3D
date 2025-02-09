import pickle
class MapManager():
    def __init__(self):
        self.model = 'block'
        self.texture = 'block.png'
        self.colors = [
            (0.2, 0.2, 0.35, 1),
            (0.2, 0.5, 0.2, 1),
            (0.7, 0.2, 0.2, 1),
            (0.5, 0.3, 0.0, 1)
            ]
        self.startNew()
        #self.addBlock((0,10,0)) 

    def startNew(self):
        self.land= render.attachNewNode("land")
    def getColor(self, z):
        if z < len(self.colors): #menentukan warna color bedqasarkan ketinggian
            return self.colors[z]
        else:
            return self.colors[len(self.colors)-1]
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getColor(int(position[2]))
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
    def  clear(self):
        "" "resets the map" ""
        self.land.removeNode()
        self.startNew()
    def loadLand(self, filename):
        "" "creates a land map from a text file, return its dimensions" ""
        self.clear()
        with open(filename) as file:
            y = 0 
            for line in file :
                x = 0 
                line = line.split(' ')
                for z in line:
                    for zO in range(int(z)+1):
                        block = self.addBlock((x, y, zO))
                    x += 1
                y += 1
        return x,y
    def findBlocks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))
    def isEmpty(self, pos):
        blocks =self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True
    def findHighestEmpty(self, pos):
        x, y, z = pos
        z = 1
        while not self.isEmpty((x,y,z)):
             z += 1
        return (x,y,z)
    def buildBlock(self, pos):
        x, y, z = pos
        new = self.findHighestEmpty(pos)
        if new[2] <= z + 1:
            self.addBlock(new)
    def delBlock(self, position):
        blocks = self.findBlocks(position)
        for block in blocks:
            block.removeNode()
    def delBlockFrom(self, position):
        x, y, z = self.findHighestEmpty(position)
        pos = x,y,z - 1
        for block in self.findBlocks(pos):
            block.removeNode()
    def saveMap(self):
        blocks = self.land.getChildren()
        with open('my_map.dat', 'wb') as fout:
            pickle.dump(len(blocks), fout)
            for block in blocks:
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, fout)
    def loadMap(self):
        self.clear()
        with open('my_map.dat', 'rb') as fin:
            legth = pickle.load(fin)
            for i in range(legth):
                pos = pickle.load(fin)
                self.addBlock(pos)
