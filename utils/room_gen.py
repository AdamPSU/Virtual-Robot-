import random 

class RoomGeneration(): 
    """Class for generating dirty rooms for the virtual room to clean."""
    def __init__(self): 
        self.height = random.randint(2, 5)
        self.width = random.randint(2, 5) 
        self.obstacles = ['#', '~', 'T'] #solid, clean, trash
    
    def getRoom(self): 
        """Returns a 2D list to represent the random map"""
        for _ in range(self.rows): 
            height = ''
            for _ in range(self.cols): 
                height += f'{random.choice(self.obstacles)}  '
            print(height)


    


    
    
    

    

    










