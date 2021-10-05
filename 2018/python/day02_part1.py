
def main():
    two_count   = 0
    three_count = 0

    with open('PuzzleInput02.txt','r') as file:

        for ID in file:
            letter_array = []
            two   = 0
            three = 0
            for letter in ID.strip():
            
                if letter not in letter_array:

                    letter_array.append(letter)
                    occurence = ID.count(letter)

                    if occurence == 2:
                        if two == 0:
                            two_count += 1
                            two += 1
                    elif occurence == 3:
                        if three == 0:
                            three_count += 1
                            three += 1
                    else:
                        continue

                
    print(two_count * three_count)

if __name__ == '__main__':
    main() 