
def read_map(my_map):
    # first lets build a graph from the input
    the_map = {} # initialize empty graph
    # now fill the graph with the map instructions
    with open(my_map, 'r') as file:
        lines = (line.strip() for line in file if line)
        for line in lines:
            objects = line.split(")")
            if objects[0] in the_map:
                the_map[objects[0]].append(objects[1])
            else:
                the_map[objects[0]] = [objects[1]]
            if not objects[1] in the_map:
                the_map[objects[1]] = []
    return the_map

def OrbitCountChecksum(my_map):
    # immediatley get direct orbits
    direct_orbits   = len(my_map)-1
    indirect_orbits = 0

    current_degree       = 1
    nodes_in_degree      = my_map["COM"]
    nodes_in_next_degree = []

    check = direct_orbits - len(nodes_in_degree)

    while check > 0:
        for node in nodes_in_degree:
            nodes_in_next_degree += my_map[node]
            check -= 1
        indirect_orbits += current_degree*len(nodes_in_next_degree)

        # step up on degree
        current_degree += 1
        nodes_in_degree = nodes_in_next_degree
        nodes_in_next_degree = []

    the_number = direct_orbits + indirect_orbits

    return the_number

def main():
    MAP = read_map("PuzzleInput_Day06.txt")
    checksum = OrbitCountChecksum(MAP)
    print("the cheksum is:", checksum)

if __name__ == "__main__":
    main()