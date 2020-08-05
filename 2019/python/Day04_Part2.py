
def nondecreasing(my_number):
    number_string = str(my_number)
    test = 1
    for k in range(0,len(number_string)-1):
        test *= (number_string[k] <= number_string[k+1])
    return test

def only_two_adjacent(my_number):
    number_string = str(my_number)
    test        = 1
    count       = 0
    digits_ad   = []
    digits_more = []
    for k in range(0, len(number_string)-1):
        # first count the adjacent digits and store them:
        if number_string[k] == number_string[k+1]:
            count += 1
            digits_ad += [number_string[k]]
        if k <= len(number_string)-3:
            # now check if there are more than two adjacent:
            if number_string[k] == number_string[k+1] == number_string[k+2]:
                digits_more += [number_string[k]]
    # now check if there are digits in both sets
    if list(set(digits_ad)-set(digits_more)):
        test *= (count >= 1)
    else:
        test = 0
    return test

def counting_passworts(a,b):
    number_of_passworts = 0
    while a <= b:
        number_of_passworts += 1*nondecreasing(a)*only_two_adjacent(a)
        a += 1
    return number_of_passworts

a = 307237
b = 769058
nr = counting_passworts(a,b)

print("the number of different passworts is:", nr)