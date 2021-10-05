
def read_input(my_file):
    # only works for one line !!!
    PuzzleInput = open(my_file, "r")
    for line in PuzzleInput:
        the_picture = [ int(digit) for digit in line ]
    return the_picture

def encode_picture(the_picture, the_width, the_hight):
    Layers = [the_picture[i:i+(the_width*the_hight)] for i in range(0, len(the_picture), the_width*the_hight) ]
    return Layers

def find_Layer_with_fewest_zero_digits(the_picture):
    fewest = float('inf')
    for k, Layer in enumerate(the_picture):
        number_of_zeros = sum( digit == 0 for digit in Layer )
        if number_of_zeros < fewest:
            the_layer = k
            fewest = number_of_zeros
    return the_layer

def test_layer(the_layer, a, b):
    number_of = lambda x: sum( digit == x for digit in the_layer)
    return number_of(a) * number_of(b)



if __name__ == "__main__":
    picture = read_input("PuzzleInput_Day08.txt")

    pic   = encode_picture(picture, 25, 6)
    layer = find_Layer_with_fewest_zero_digits(pic)
    test  = test_layer(pic[layer], 1, 2)

    print("the answer is", test)
