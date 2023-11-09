import random 
from termcolor import colored


class RoomGeneration(): 
    """Class for generating dirty rooms for the virtual robot to clean."""
    def __init__(self): 
        self.width, self.height = 5, 5 #random.randint(3, 10), random.randint(3, 10)
        self.x, self.y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)

        self.obstacles = ['#', '*'] #solid, trash


    def startingPosition(self):  
        return self.x, self.y

    
    def getRoom(self): 
        """Returns a 2D list to represent the room"""
        room = []

        for _ in range(self.width): 
            row = []
            for _ in range(self.height): 
                row += f'{random.choice(self.obstacles)}'
            room.append(row)
        
        #define where the robot begins cleaning
        x, y = self.startingPosition()
        room[y][x] = colored('>', 'red', attrs=['blink'])

        return room
    





            
        




            


    


    
    
    

    

    










