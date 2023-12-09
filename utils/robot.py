import os
import random
import time
from termcolor import colored

from utils.room_gen import RoomGeneration

class Robot():
    def __init__(self, initial_battery=100):
        """Initialize the Robot with the provided initial battery level."""
        self.room_gen = RoomGeneration()
        self.room = self.room_gen.getRoom(30)
        self.width, self.height = len(self.room[0]), len(self.room)

        self.charging_station_position = self.room_gen.chargingStationPosition()
        self.x, self.y = self.room_gen.startingPosition()
        self.prev_x, self.prev_y = None, None
        self.marked = [[False for _ in range(self.width)] for _ in range(self.height)]

        self.battery = initial_battery
        self.length = 0

        print(self)

    def __str__(self):
        """String representation of the room and robot's position."""
        room_str = "\n".join(["  ".join(row) for row in self.room])
        return room_str

    def isClean(self):
        """Verifies whether the room is clean/needs more work."""
        if all('*' not in row for row in self.room):
            print('The room is clean!')
            return True
        return False

    def isValid(self, x, y):
        """A move is invalid if it is out of bounds or if it tries to access a solid ('#') block or 'C' block."""
        return (
            (0 <= x < self.width)
            and (0 <= y < self.height)
            and not (self.marked[y][x])
            and (self.room[y][x] not in ['#', 'C'])
        )

    def increaseLength(self, amount):
        """Increase the cleaning path length."""
        self.length += amount

    def reduceBattery(self, amount):
        """Reduce the battery level by the specified amount."""
        self.battery -= amount

    def chargeBattery(self):
        """Simulate charging the battery."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Charging...")
        time.sleep(2)  # Simulating charging time
        self.battery = 100  # Fully charged
        print("Charged!")

    def isLowBattery(self):
        """Check if the battery falls below 20%."""
        return self.battery < 20

    def goHome(self):
        """Go to the charging station if the battery is low."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Low battery! Returning to charging station...")
        time.sleep(1.5)

        self.room[self.y][self.x] = colored('~', 'green', attrs=['blink'])
        self.x, self.y = self.charging_station_position
        self.room[self.y][self.x] = colored('>', 'red', attrs=['blink'])
        self.chargeBattery()
        print(self)
        time.sleep(0.5)

    def move(self, dx, dy, symbol):
        """Move the robot in the specified direction."""
        new_x, new_y = self.x + dx, self.y + dy
        if (
            0 <= new_x < self.width
            and 0 <= new_y < self.height
            and self.room[new_y][new_x] != "#"
        ):
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
            self.room[self.y][self.x] = colored("~", "green", attrs=["blink"])
            self.room[new_y][new_x] = colored(symbol, "red", attrs=["blink"])
            self.x, self.y = new_x, new_y
            print(self)
            self.reduceBattery(1)
            self.increaseLength(1)
            print(f"Path length: {self.length}, Remaining Battery: {self.battery}%")
            if self.isLowBattery():
                self.goHome()

    def cleanLeft(self):
        """Clean to the left."""
        self.move(-1, 0, '<')

    def cleanRight(self):
        """Clean to the right."""
        self.move(1, 0, '>')

    def cleanDown(self):
        """Clean downward."""
        self.move(0, 1, 'v')

    def cleanUp(self):
        """Clean upward."""
        self.move(0, -1, '^')

    def cleanManual(self):
        """Manual room-cleaning using W, A, S, D keys."""
        print('Move with W, A, S, D keys')
        while not self.isClean():
            key = input().lower()
            if key == 'w':
                self.cleanUp()
            elif key == 'a':
                self.cleanLeft()
            elif key == 's':
                self.cleanDown()
            elif key == 'd':
                self.cleanRight()

    def cleanRandom(self):
        """Randomized room-cleaning. Can go up, down, left, or right."""
        while not self.isClean():
            if self.battery > 0:
                choices = [self.cleanLeft, self.cleanRight, self.cleanUp, self.cleanDown]
                chosen_method = random.choice(choices)
                time.sleep(0.2)
                chosen_method()
                if self.isLowBattery():
                    self.goHome()

    def cleanDFS(self):
        """Start DFS from the current position."""
        self.marked = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.dfs(self.x, self.y)

    def dfs(self, x, y):
        """Depth-first search for cleaning the room."""
        if not self.isValid(x, y) or self.marked[y][x]:
            return

        # Mark the current position with "@"
        time.sleep(0.2)
        self.room[y][x] = colored("@", "red", attrs=["blink"])

        # If there was a previous position, turn it back to a cleaned spot
        if self.prev_x is not None and self.prev_y is not None:
            self.room[self.prev_y][self.prev_x] = colored("~", "green", attrs=["blink"])

        # Update the previous position
        self.prev_x, self.prev_y = x, y

        # Clean the current position
        self.marked[y][x] = True
        self.reduceBattery(1)
        self.increaseLength(1)

        if self.isLowBattery():
            self.goHome()

        # Display the current state
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
        print(self)
        print(f"Path length: {self.length}, Remaining Battery: {self.battery}%")

        # Explore in all possible directions (left, right, up, down)
        self.dfs(x - 1, y)
        self.dfs(x + 1, y)
        self.dfs(x, y - 1)
        self.dfs(x, y + 1)
