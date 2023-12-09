import random
from termcolor import colored

class RoomGeneration():
    """Class for generating dirty rooms for the virtual robot to clean."""

    def __init__(self):
        """Initialize the RoomGeneration object with default room dimensions and starting position."""
        self.width, self.height = 10, 10
        self.obstacles = ['#', '*']  # Solid, trash

        self.x, self.y = 0, 0
        self.cx, self.cy = random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    def startingPosition(self):
        """Get the starting position of the robot in the room."""

        return self.x, self.y

    def chargingStationPosition(self):
        """Get the position of the charging station in the room."""
        return self.cx, self.cy

    def getRoom(self, obstacles):
        """Returns a 2D list to represent the room with randomly placed obstacles."""
        
        # Set all elements to '*'
        room = [['*' for _ in range(self.height)] for _ in range(self.width)]

        # Place furniture (solid blocks) randomly in the room
        for _ in range(obstacles):
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            room[y][x] = '#'

        # Set the starting position of the robot in the room
        x, y = self.startingPosition()
        room[y][x] = colored('>', 'red', attrs=['blink']) # Robot = '>'

        # Set the charging station position and color it purple
        cx, cy = self.chargingStationPosition()
        room[cy][cx] = 'C'

        return room







            




                


        


        
        
        

    

    










