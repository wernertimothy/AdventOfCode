
def main():
    homework = ReadPuzzleInput('PuzzleInput_Day18.txt')
    accumulator = 0
    for expr in homework:
        accumulator += evaluate(expr.replace('*','a').replace('+','b').replace('a','+').replace('b','*'))
    print('The solution is', accumulator)

class number:
    def __init__(self, x):
        self.x = x
    def __add__(self, y):
        return number(self.x * y.x)
    def __mul__(self, y):
        return number(self.x + y.x)

def evaluate(expression):
    exp = ''
    for char in expression:
        if char in '0123456789':
            exp += 'number(' + char + ')'
        else:
            exp += char
    return(eval(exp).x) 

def ReadPuzzleInput(my_file):
    with open(my_file, 'r') as f:
        return [line.rstrip() for line in f]

if __name__ == "__main__":
    main()