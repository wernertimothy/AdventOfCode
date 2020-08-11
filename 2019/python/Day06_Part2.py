from collections import deque

def read_map(my_map):
    # first lets build a graph from the input
    the_map = {} # initialize empty graph
    # now fill the graph with the map instructions
    with open(my_map, 'r') as file:
        lines = (line.strip() for line in file if line)
        for line in lines:
            objects = line.split(")")
            # now this graph needs to be undirected!!!
            if objects[0] in the_map:
                the_map[objects[0]].append(objects[1])
            else:
                the_map[objects[0]] = [objects[1]]
            if objects[1] in the_map:
                the_map[objects[1]].append(objects[0])
            else:
                the_map[objects[1]] = [objects[0]]
    return the_map

def FindSanta(my_map):
    transfers        = 0              # init first transfers
    already_searched = ['YOU']        # init list of searched objects
    this_orbit       = deque()        # init searching queue for current orbit
    next_orbit       = deque()        # init searching queue for next orbit
    this_orbit      += my_map['YOU']  # start with me
    while this_orbit:
        the_object = this_orbit.popleft()
        if not the_object in already_searched:
            already_searched.append(the_object)
            if the_object == 'SAN':
                return transfers - 1 # i have no idea why -1 but it worked
            else:
                next_orbit += my_map[the_object]
        if not this_orbit:
            this_orbit = next_orbit
            next_orbit = deque()
            transfers += 1
    return 0
    
def main():
    MAP = read_map("PuzzleInput_Day06.txt")
    Orbital_transfers = FindSanta(MAP)
    print(Orbital_transfers)

if __name__ == "__main__":
    main()