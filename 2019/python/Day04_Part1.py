
def nondecreasing(my_number):
    number_string = str(my_number)
    test = 1
    for k in range(0,len(number_string)-1):
        test *= (number_string[k] <= number_string[k+1])
    return test

def two_adjacent(my_number):
    number_string = str(my_number)
    test = 1
    count = 0
    # first count the adjacent integers:
    for k in range(0, len(number_string)-1):
        if number_string[k] == number_string [k+1]:
            count += 1
    # now check if there is at least one:
    test *= (count >= 1) 
    return test

def counting_passworts(a,b):
    number_of_passworts = 0
    while a <= b:
        number_of_passworts += 1*nondecreasing(a)*two_adjacent(a)
        a += 1
    return number_of_passworts

a = 307237
b = 769058
nr = counting_passworts(a,b)

print("the number of different passworts is:", nr)