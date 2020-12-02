
def main():
    passwort_candidates = ReadPuzzleInput("PuzzleInput_Day02.txt")
    nr_valid_passworts = check_validity(passwort_candidates)
    print("the number of valid passworts is", nr_valid_passworts)

def check_validity(candidates):
    validty_count = 0
    for candidate in candidates:
        occurence = candidate[3].count(candidate[2])
        if (occurence >= candidate[0]) and (occurence <= candidate[1]): validty_count += 1
    return validty_count

def ReadPuzzleInput(my_file):
    candidates = []
    with open(my_file, 'r') as f:
        policies = [line.split() for line in f]
        for policy in policies:
            the_range = policy[0].split("-")
            candidates.append([
                int(the_range[0]),  # at least
                int(the_range[1]),  # the most
                policy[1][0],       # character
                policy[2]           # passwort
            ])
        return candidates

if __name__ == "__main__":
    main()