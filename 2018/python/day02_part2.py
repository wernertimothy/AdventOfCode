import itertools

def main():
    ID_list = []
    with open ('PuzzleInput02.txt','r') as file:
        for ID in file:
            ID_list.append(ID.strip())

    the_IDs = []
    last_counter = 0
    for ID_a, ID_b in itertools.combinations(ID_list, 2):
        counter = 0
        pair = zip(ID_a, ID_b)
        for letter_a, letter_b in pair:
            if letter_a == letter_b:
                counter += 1
        if counter > last_counter:
            the_IDs = [ID_a, ID_b]
            last_counter = counter
    
    the_ID = ''
    for letter_a, letter_b in zip(the_IDs[0], the_IDs[1]):
        if letter_a == letter_b:
            the_ID += letter_a

    print(the_ID)

if __name__ == '__main__':
    main()