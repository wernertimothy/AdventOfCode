import numpy as np

def main():
    ship = Ship(ReadPuzzleInput("PuzzleInput_Day12.txt"))
    print("The Manhatten distance is", ship.followInstructions())

class Ship:
    def __init__(self, instructions):
        self.instructions = instructions
        self.directions = {0 : 'N', 90 : 'E', 180 : 'S', 270 : 'W'}
        # states:
        self.x          = 0     # global coordinates
        self.y          = 0     # global coordinates
        self.waypoint_x = 10    # ship coordinates
        self.waypoint_y = 1     # ship coordinates

    def followInstructions(self):
        for inst in self.instructions:
            if inst[0] == 'F':
                # move ship
                self.move(inst[1])
            elif inst[0] == 'R' or inst[0] == 'L':
                # rotate waypoint
                self.rotateWaypoint(inst[0], inst[1])
            else:
                # move the waypoint
                self.readInstruction(inst[0], inst[1])
        
        return int(abs(self.x) + abs(self.y))

    def readInstruction(self, direction, amount):
        if   direction == 'N': self.waypoint_y += amount
        elif direction == 'E': self.waypoint_x += amount
        elif direction == 'S': self.waypoint_y -= amount
        elif direction == 'W': self.waypoint_x -= amount

    def rotateWaypoint(self, direction, amount):
        if   direction == 'L' : deg =  amount
        elif direction == 'R' : deg = -amount
        cos = np.cos(deg * np.pi / 180)
        sin = np.sin(deg * np.pi / 180)
        R = np.array([
            [cos, -sin],
            [sin,  cos]
        ])
        [self.waypoint_x, self.waypoint_y] = R@[self.waypoint_x, self.waypoint_y]

    def move(self, amount):
        self.x += amount*self.waypoint_x
        self.y += amount*self.waypoint_y

def ReadPuzzleInput(my_file):
    with open(my_file, 'r') as f:
        my_list = []
        for line in f:
            line = line.rstrip()
            my_list.append([
                line[0], int(line[1:])
            ])
        return my_list

if __name__ == "__main__":
    main()