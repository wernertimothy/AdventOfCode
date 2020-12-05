import re

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
        has_keys = True
        for key in keys:
            has_keys *= key in passport
        if has_keys:
            is_valid = True
            for key in passport:
                if not is_valid: break
                is_valid *= CheckValueValidity(key, passport[key])
            if is_valid: count += 1; valid_Passports.append(passport) 
    return count, valid_Passports

def CheckValueValidity(key, value):
    if key == 'byr':
        return True if len(str(value)) == 4 and int(value) >= 1920 and int(value) <= 2002 else False
    elif key == 'iyr':
        return True if len(str(value)) == 4 and int(value) >= 2010 and int(value) <= 2020 else False
    elif key == 'eyr':
        return True if len(str(value)) == 4 and int(value) >= 2020 and int(value) <= 2030 else False
    elif key == 'hgt':
        match = re.match(r"([0-9]+)([a-z]+)", str(value), re.I)
        if match:
            items = match.groups()
            if items[1] == 'cm':
                return 150 <= int(items[0]) <= 193
            else:
                return 59 <= int(items[0]) <= 76
        else:
            return False
    elif key == 'hcl':
        if len(str(value)) == 7 and str(value)[0] == '#':
            test = True
            for char in str(value)[1:]:
                if not test: break
                if char.isdigit():
                    test *= ( 0 <= int(char) <= 9 )
                else:
                    test *= char in ['a', 'b', 'c', 'd', 'e', 'f']
            return test
        else: return False
    elif key == 'ecl':
        return True if str(value) in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] else False
    elif key == 'pid':
        return True if len(str(value)) == 9 else False
    elif key == 'cid':
        return True

if __name__ == "__main__":
    main()