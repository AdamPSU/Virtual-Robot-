import os 
from termcolor import colored

from utils.room_gen import RoomGeneration


class Robot(): 
    def __init__(self): 
        self.room_gen = RoomGeneration()

        self.room = self.room_gen.getRoom()
        self.x, self.y = self.room_gen.startingPosition()

        print(self)
    

    def isClean(self): 
        """Verifies whether the room is clean/needs more work"""
        room = self.room

        for row in room: 
            if '*' not in row: 
                return True 
            
        return False


    def cleanLeft(self): 
        os.system('cls' if os.name == 'nt' else 'clear')
        if (self.x > 0) and (self.room[self.y][self.x-1] != '#'):  

            self.room[self.y][self.x] = colored('~', 'green', attrs=['blink'])
            self.room[self.y][self.x-1] = colored('<', 'red', attrs=['blink'])
            self.x -= 1

        print(self)

    
    def cleanRight(self): 
        os.system('cls' if os.name == 'nt' else 'clear')
        if (self.x < len(self.room[0])-1) and (self.room[self.y][self.x+1] != '#'): 

            self.room[self.y][self.x] = colored('~', 'green', attrs=['blink'])
            self.room[self.y][self.x+1] = colored('>', 'red', attrs=['blink'])
            self.x += 1
        
        print(self)
    

    def cleanDown(self): 
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.y < len(self.room)-1 and self.room[self.y+1][self.x] != '#': 

            self.room[self.y][self.x] = colored('~', 'green', attrs=['blink'])
            self.room[self.y+1][self.x] = colored('v', 'red', attrs=['blink'])
            self.y += 1
        
        print(self)


    def cleanUp(self): 
        os.system('cls' if os.name == 'nt' else 'clear')
        if (self.y > 0) and (self.room[self.y-1][self.x] != '#'): 
        
            self.room[self.y][self.x] = colored('~', 'green', attrs=['blink'])
            self.room[self.y-1][self.x] = colored('^', 'red', attrs=['blink'])
            self.y -= 1 
        
        print(self)
    

    def __str__(self): 
        roomStr = ""

        for row in self.room:
            rowStr = "  ".join(row) 
            roomStr += rowStr + '\n'
        
        return roomStr

