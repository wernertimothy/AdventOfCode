import matplotlib.pyplot as plt

def read_input(my_file):
    # only works for one line !!!
    PuzzleInput = open(my_file, "r")
    for line in PuzzleInput:
        the_picture = [ int(digit) for digit in line ]
    return the_picture

def encode_picture(the_picture, the_width, the_hight):
    Layers = [the_picture[i:i+(the_width*the_hight)] for i in range(0, len(the_picture), the_width*the_hight) ]
    return rearange_Layers(Layers, the_width, the_hight)
    
def rearange_Layers(Layers, the_width, the_hight):
    return [ [Layer[i:i+the_width] for i in range(0, len(Layer), the_width)] for Layer in Layers]

def render(the_picture):
    rendered_picture = the_picture[0]

    for j, row in enumerate(rendered_picture):
        for k, pixel in enumerate(row):
            i = 1
            while row[k] == 2:
                row[k] = the_picture[i][j][k]
                i += 1

    return rendered_picture


if __name__ == "__main__":
    picture = read_input("PuzzleInput_Day08.txt")

    pic = encode_picture(picture, 25, 6)
    pic = render(pic)

    plt.imshow(pic)
    plt.show()
