
'''
not optimal. I had to manipulate the firste few lines in the PuzzleInput for it to work
'''

def main():
    ranges, my_ticket, nearby_tickets = ReadPuzzleInput('PuzzleInput_Day16.txt')
    error_rate = BruteSearchTickets(ranges, nearby_tickets)
    print('The error rate is', error_rate)

def BruteSearchTickets(ranges, tickets):
    error_rate = 0
    for ticket in tickets:
        for value in ticket:
            in_no_range = True
            for the_range in ranges:
                if value in the_range:
                    in_no_range = False
                    break
            if in_no_range: 
                error_rate += value
    return error_rate 

def ReadPuzzleInput(my_file):
    counter = 0
    valid_ranges = []
    near_tickets = []
    with open(my_file, 'r') as f:
        for line in f:
            if line.rstrip():
                if counter == 0:
                    note = line.rstrip().split(' ')
                    ranges = [note[1], note[3]]
                    for the_range in ranges:
                        nums = the_range.split('-')
                        valid_ranges.append( range( int(nums[0]), int(nums[1]) + 1 ) )
                elif counter == 1:
                    if line.rstrip() == 'your ticket:':
                        continue
                    else:
                        note = line.rstrip().split(',')
                        my_ticket = [int(num) for num in note]
                elif counter == 2:
                    if line.rstrip() == 'nearby tickets:':
                        continue
                    else:
                        note = line.rstrip().split(',')
                        ticket = [int(num) for num in note]
                        near_tickets.append(ticket)
            else:
                counter += 1
    return valid_ranges, my_ticket, near_tickets

if __name__ == "__main__":
    main()