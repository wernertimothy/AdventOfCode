
def main():
    passwort_candidates = ReadPuzzleInput("PuzzleInput_Day02.txt")
    nr_valid_passworts = check_validity(passwort_candidates)
    print("the number of valid passworts is", nr_valid_passworts)

def check_validity(candidates):
    validty_count = 0
    for candidate in candidates:
        if candidate[3][candidate[0]-1] == candidate[2] and not candidate[3][candidate[1]-1] == candidate[2]:
            validty_count += 1
        elif candidate[3][candidate[1]-1] == candidate[2] and not candidate[3][candidate[0]-1] == candidate[2]:
            validty_count += 1
        else:
            continue
    return validty_count

def ReadPuzzleInput(my_file):
    candidates = []
    with open(my_file, 'r') as f:
        policies = [line.split() for line in f]
        for policy in policies:
            the_range = policy[0].split("-")
            candidates.append([
                int(the_range[0]),  # position a
                int(the_range[1]),  # position b
                policy[1][0],       # character
                policy[2]           # passwort
            ])
        return candidates

if __name__ == "__main__":
    main()