import matplotlib.pyplot as plt
  
def follow_instructions(directions,steps):
    # total = len(directions) # just for printing

    if len(directions) != len(steps):
        return -1
    trajx = []
    trajy = []
    for k in range(0,len(directions)):
        if directions[k] == 'R':
            # go right
            if not trajx and not trajy:
                trajx += [[0, steps[k]]]
                trajy += [[0, 0]]
            else:
                trajx += [[trajx[-1][1], trajx[-1][1] + steps[k]]]
                trajy += [[trajy[-1][1], trajy[-1][1]]]
        elif directions[k] == 'L':
            # go left
            if not trajx and not trajy:
                trajx += [[0, -steps[k]]]
                trajy += [[0, 0]]
            else:
                trajx += [[trajx[-1][1], trajx[-1][1] - steps[k]]]
                trajy += [[trajy[-1][1], trajy[-1][1]]]
        elif directions[k] == 'U':
            # go up
            if not trajx and not trajy:
                trajx += [[0, 0]]
                trajy += [[0, steps[k]]]
            else:
                trajx += [[trajx[-1][1], trajx[-1][1]]]
                trajy += [[trajy[-1][1], trajy[-1][1] + steps[k]]]
        elif directions[k] == 'D':
            # go down
            if not trajx and not trajy:
                trajx += [[0, 0]]
                trajy += [[0, -steps[k]]]
            else:
                trajx += [[trajx[-1][1], trajx[-1][1]]]
                trajy += [[trajy[-1][1], trajy[-1][1] - steps[k]]]
                
        # print('followed',k+1, 'of', total, 'instructions')
    return [trajx, trajy]

def convert_instructions(my_input):
    with open(my_input, 'r') as file:
        lines = (line.strip() for line in file if line)
        puzzle_input = [line for line in lines]
        Wires = [wire.split(',') for wire in puzzle_input]
        Directions = [[edge[0] for edge in wire] for wire in Wires]

        Steps = []
        for wire in Wires:
            steps = []
            for edge in wire:
                step_string = str()
                for k in range(1,len(edge)):
                    step_string = step_string + edge[k]
                steps = steps + [int(step_string)]
            Steps = Steps + [steps]
    return Directions, Steps

def sign(x):
    return (x>=0) - (x<0)

def is_between(a,b,c):
    # want to know if a between b and c
    # (1) order b and c:
    sorted = sort(b,c)
    if sorted[0] <= a <= sorted[1]:
        return True
    else:
        return False

def sort(a,b):
    if a <= b:
        return [a,b]
    else:
        return [b,a]

def crossing_points(wire1,wire2):
    Points = []
    for k in range(0,len(wire1[0])):
        line1 = [line[k] for line in wire1]

        for l in range(0,len(wire2[0])):
            line2 = [line[l] for line in wire2]

            # line driections:
            a1 = line1[0][1] - line1[0][0] # x direction line 1
            a2 = line1[1][1] - line1[1][0] # y direction line 1
            b1 = line2[0][1] - line2[0][0] # x direction line 2
            b2 = line2[1][1] - line2[1][0] # y direction line 2

            # denote parallel to x-axis x||
            # denote parallel to y-axis y||

            # 1. lines are not parallel:
            if (a1*b1 + a2*b2) == 0:
                # crossing possible
                if a1 == 0 and b2 == 0:
                    # 1.1 line 1 is y|| and line 2 is x||
                    steady_x = line1[0][0] # x1 (or x2) od line 1
                    steady_y = line2[1][0] # y2 (or y2) of line 2
                    if is_between(steady_x,line2[0][0],line2[0][1])  and is_between(steady_y,line1[1][0],line1[1][1]):
                        # lines do cross
                        Points += [[steady_x, steady_y]]
                else:
                    # 1.2 line 1 is x|| and line 2 is y||
                    steady_x = line2[0][0] # x1 (or x2) of line 2
                    steady_y = line1[1][0] # y1 (or y2) of line 1
                    if  is_between(steady_x,line1[0][0],line1[0][1]) and is_between(steady_y,line2[1][0],line2[1][1]):
                        # lines do cross
                        Points += [[steady_x, steady_y]]
                    
            else:
                continue
                # 2. lines are both y|| (no crossing) ???
                # 3. lines are both x|| (no crossing) ???
                # step to next line2
    if Points[0] == [0,0]:
        Points.pop(0) # get rid of the origin
    return Points

def Manhatten_distance(x,y):
    return abs( x[0] - y[0] ) + abs( x[1] - y[1] )

def closest_intersec(points):
    closest = float('inf')
    for k in range(0,len(points)):
        distance = Manhatten_distance([0,0],points[k])
        if distance < closest:
            closest = distance
            closest_point = points[k]
    return closest_point, closest
   
def main():
    print('converting instructions...')
    # directions, steps = convert_instructions('test_day3.txt')
    directions, steps = convert_instructions('PuzzleInput_Day03.txt')

    print('following instructions...')
    my_wires = [follow_instructions(directions[inst],steps[inst]) for inst in range(0,len(directions))]

    # the following only works for two wires:
    print('calculating intersections...')
    Crossings = crossing_points(my_wires[0],my_wires[1])
    print('searching for the closest...')
    intersec, man_distance = closest_intersec(Crossings)

    # plot wires
    for k in range(0,len(my_wires)):
        if k == 0:
            color = 'b'
        elif k == 1:
            color = 'g'
        current_wire = my_wires[k]
        for l in range(0,len(current_wire[0])):
            plt.plot(current_wire[0][l],current_wire[1][l],color)
    
    # plot origin
    plt.plot(0,0,'sk') 
    # plot crossings
    for point in Crossings:
        plt.plot(point[0],point[1],'ko')

    # plot intersec
    plt.plot(intersec[0],intersec[1],'rx')
    print('The Manhatten Distance to the closest intersection is',man_distance)
    plt.show()

if __name__ == '__main__':
    main()