
def opcode(my_list):
    k = 0
    instructions = 4
    halt = False
    while not halt:
        if my_list[k] == 1:
            # this is addition
            my_list[my_list[k+3]] =  my_list[my_list[k+1]]+my_list[my_list[k+2]]   
        elif my_list[k] == 2:
            # this is mulitplication
            my_list[my_list[k+3]]  = my_list[my_list[k+1]]*my_list[my_list[k+2]] 
        elif my_list[k] == 99:
            # this is halt
            halt = True
        
        k += instructions
        if k >= len(my_list):
            return my_list
    return my_list[0]


puzzle_input = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,99,2,14,0,0]
# puzzle_input = [1,90,74,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,99,2,14,0,0]

print(opcode(puzzle_input))