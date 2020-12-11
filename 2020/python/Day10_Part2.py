
def main():
    adapters = Adapters(ReadPuzzleInput("PuzzleInput_Day10.txt"))
    combs = adapters.count()
    print('The number of possible combinations is', combs)
    
class Adapters:
    def __init__(self, adapters):
        self.adapters = {0: []}
        self.getNeighbours(0, adapters)
        for adapter in adapters:
            if adapter not in self.adapters:
                self.adapters[adapter] = []
                self.getNeighbours(adapter, adapters)

    def getNeighbours(self, the_adapter, adapters):
        for adapter in adapters:
            if 0 < (adapter - the_adapter) <= 3:
                self.adapters[the_adapter].append(adapter)
        if not self.adapters[the_adapter]: self.goal_adapter = the_adapter

    def count(self):
        visited = []
        self.counter = 0
        self.countCombinations(0, self.goal_adapter, visited)
        return self.counter

    def countCombinations(self, start_adapter, goal_adapter, visited):
        visited.append(start_adapter)
        if start_adapter == goal_adapter:
            self.counter += 1
        else:
            for adapter in self.adapters[start_adapter]:
                if adapter not in visited:
                    self.countCombinations(adapter, self.goal_adapter, visited)
        visited.remove(start_adapter)

def ReadPuzzleInput(my_file):
    with open(my_file, 'r') as f:
        return [int(line) for line in f]

if __name__ == "__main__":
    main()