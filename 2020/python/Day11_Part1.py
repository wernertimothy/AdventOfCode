import copy

def main():
    model = Model(ReadPuzzleInput("PuzzleInput_Day11.txt"))
    model.predict()
    print('The number of occupied seats is', model.occupiedSeats())

class Model:
    def __init__(self, map):
        self.map = map
        self.i = len(map)-1
        self.j = len(map[0])-1
        self.old_map = []

    def occupiedSeats(self):
        char = ''.join(map(str, self.map))
        return char.count('#')

    def predict(self):
        while self.map != self.old_map:
            self.predicted_map = copy.deepcopy(self.map)
            for i in range(self.i+1):
                for j in range(self.j+1):
                    self.applyRules(i, j)
            self.old_map = copy.deepcopy(self.map)
            self.map = copy.deepcopy(self.predicted_map)

    def applyRules(self, i, j):
        adjacent = self.getAdjacents(i,j)
        # If a seat is empty (L) and there are no occupied seats adjacent
        def noOccupied(adjacent) : return True if '#' not in adjacent else False
        # If a seat is occupied (#) and four or more seats adjacent are occupied
        def fourOrMoreOccupied(adjacent) : return True if adjacent.count('#') >= 4 else False

        if self.map[i][j] == 'L':
            if noOccupied(adjacent):
                self.predicted_map[i][j] = '#'
        elif self.map[i][j] == '#':
            if fourOrMoreOccupied(adjacent):
                self.predicted_map[i][j] = 'L'
        
    def getAdjacents(self, i, j):
        adjacent = []

        if i == 0 : irange = [0,1]
        elif i == self.i : irange = [-1,0]
        else : irange = [-1,0,1]

        if j == 0 : jrange = [0,1]
        elif j == self.j : jrange = [-1,0]
        else : jrange = [-1,0,1]

        for k in irange:
            for l in jrange:
                if k == l == 0: continue
                else : adjacent.append(self.map[i+k][j+l])

        return adjacent

def ReadPuzzleInput(my_file):
    def split(word): return list(word)
    with open(my_file, 'r') as f:
        return[split(line.rstrip()) for line in f] 

if __name__ == "__main__":
    main()