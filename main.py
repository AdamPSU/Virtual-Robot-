import os
import keyboard

from utils.robot import Robot

os.system('cls' if os.name == 'nt' else 'clear')

class Game():
    def __init__(self):
        self.roomba = Robot()
        self.play()

    def round(self, e):
        key = e.name
        if key == 'right':
            self.roomba.cleanRight()
        elif key == 'left':
            self.roomba.cleanLeft()
        elif key == 'up':
            self.roomba.cleanUp()
        elif key == 'down':
            self.roomba.cleanDown()

    def play(self):
        responses = ['yes', 'yea', 'sure', 'of course', 'why not', 'indubitably']
        gameQuery = input(f"Would you like to clean the room?\n> ").lower()
        
        condition = self.roomba.isClean()

        if gameQuery in responses:
            print("Use arrow keys to move the robot.")

            keyboard.on_release(self.round)  # Register the key listener
        
        while not condition: 
            #currently just an infinite loop as the condition is sometimes impossible to reach
            pass


if __name__ == "__main__":
    game = Game()
