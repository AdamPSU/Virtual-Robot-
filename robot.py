from utils.room_gen import RoomGeneration


class Robot(): 
    def __init__(self, posX: int, posY: int, direction: str): 
        self.posX = posX
        self.posY = posY 
        self.direction = direction
    
    def getCoordinates(self): 
        return (self.posX, self.posY) 




