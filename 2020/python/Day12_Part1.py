
def main():
    ship = Ship(ReadPuzzleInput("PuzzleInput_Day12.txt"))
    print("The Manhatten distance is", ship.followInstructions())

class Ship:
    def __init__(self, instructions):
        self.instructions = instructions
        self.directions = {0 : 'N', 90 : 'E', 180 : 'S', 270 : 'W'}
        # states:
        self.heading = 90
        self.x = 0
        self.y = 0

    def followInstructions(self):
        for inst in self.instructions:
            if inst[0] == 'F':
                # move in heading direction
                self.readInstruction(self.directions[self.heading], inst[1])
            elif inst[0] == 'R':
                # rotate ship right
                self.heading = (self.heading+inst[1])%360
            elif inst[0] == 'L':
                # rotate ship left
                self.heading = (self.heading-inst[1])%360
            else:
                # move in instructed direction
                self.readInstruction(inst[0], inst[1])
        
        return abs(self.x) + abs(self.y)

    def readInstruction(self, direction, amount):
        if   direction == 'N': self.y += amount
        elif direction == 'E': self.x += amount
        elif direction == 'S': self.y -= amount
        elif direction == 'W': self.x -= amount

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