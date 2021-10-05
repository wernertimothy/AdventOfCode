
def main():
    change_array = []
    with open('PuzzleInput01.txt', 'r') as file:
        for change in file:
            change_array.append( int(change) )
    
    freq_array = []
    freq       = 0

    not_found  = True

    while not_found:

        for change in change_array:

            freq_array.append(freq)
            freq += change

            if freq in freq_array:
                not_found = False
                print(freq)
                break   

if __name__ == '__main__':
    main()