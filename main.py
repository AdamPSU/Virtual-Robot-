import os

from utils.robot import Robot
os.system('cls' if os.name == 'nt' else 'clear')

class Game():
    def __init__(self):
        """Initialize the game by creating a Robot instance and starting the game loop."""
        self.roomba = Robot()
        self.play()

    def play(self):
        """Start the game loop, prompting the user for preferences and initiating the cleaning process."""
        
        responses = ['yes', 'yea', 'sure', 'of course', 'why not', 'indubitably']
        query = input(f'Would you like to clean the room?\n>').lower()

        # Continue prompting until a valid response is given
        while True:
            if query in responses:
                break

            query = input(f"I didn't quite get that... say it again.\n>").lower()

        mode = input(f'Would you like to clean randomly, manually, or with DFS? (random/manual/dfs)\n>').lower()

        # Continue prompting until a valid cleaning mode is selected
        while True:
            if mode == 'random':
                self.roomba.cleanRandom()
                break
            elif mode == 'dfs':
                self.roomba.cleanDFS()
                break
            elif mode == 'manual':
                self.roomba.cleanManual()
                break
            else:
                mode = input(f"Invalid input. Please enter 'random', 'dfs', or 'manual'.\n>").lower()


if __name__ == "__main__":
    # Start the cleaning process
    game = Game()

