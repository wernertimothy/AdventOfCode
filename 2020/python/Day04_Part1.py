
def main():
    Passports = ReadPuzzleInput("PuzzleInput_Day04.txt")
    nr_valid_passports, Passports = CheckPassports(Passports)
    print("the number of valid passports is", nr_valid_passports)

def ReadPuzzleInput(my_file):
    # patch_file needs two empty lines at the end for this to work
    batch_file = []
    with open(my_file, 'r') as f:
        passport = []
        for line in f:
            if line == '\n':
                batch_file.append(passport)
                passport = []
            else:
                passport.append(line)
    return Sortify(batch_file)

def Sortify(batch_file):
    Passports = [{} for passport in batch_file]
    for i, passport in enumerate(batch_file):
        for entry in passport:
            tmp = entry.split()
            for field in tmp:
                tmp2 = field.split(':')
                Passports[i][tmp2[0]] = tmp2[1]
    return Passports

def CheckPassports(Passports):
    valid_Passports = []
    count = 0
    keys = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        #'cid'
    ]
    for passport in Passports:
        is_valid = True
        for key in keys:
            is_valid *= key in passport
        if is_valid: count += 1; valid_Passports.append(passport) 
    return count, valid_Passports

if __name__ == "__main__":
    main()