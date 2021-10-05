import re
from collections import deque

def main():
    Bags    = ReadPuzzleInput("PuzzleInput_Day07.txt")
    options = SearchCombinations(Bags)
    print("The number of options is", options)

def ReadPuzzleInput(my_file):
    with open(my_file, 'r') as f:
        return GraphifyRules( GetBagRules( [line.split(' ') for line in [line.rstrip() for line in f]] ) )

def GetBagRules(Rules):
    Bags = []
    for rule in Rules:
        bag = [rule[0] + ' ' + rule[1]]
        if rule[4] == 'no':
            Bags.append(bag)
        else:
            for k, word in enumerate(rule):
                try:
                    int(word)
                    bag.append( word + ' ' + rule[k+1] + ' ' + rule[k+2] )
                except:
                    continue
            Bags.append(bag)
    return Bags

def GraphifyRules(Rules):
    graph = {}
    for rule in Rules:
        graph[rule[0]] = [rule[i] for i in range(1, len(rule))]
    return graph

def SearchCombinations(Bags):
    options       = []
    search_queue  = deque()
    search_queue += ['shiny gold']
    while search_queue:
        color = search_queue.popleft()
        for bag in Bags:
            if color in Bags[bag]:
                if bag not in options:
                    options.append(bag)
                    search_queue += [bag]
    return len(options)

if __name__ == "__main__":
    main()
