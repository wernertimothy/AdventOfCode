
class Submarine:
    def __init__(self):
        self._horizontal_position = 0
        self._depth = 0
        self._aim = 0
    
    @property
    def horizontal_position(self):
        return self._horizontal_position

    @property
    def depth(self):
        return self._depth

    @property
    def solution(self):
        return self._depth * self._horizontal_position

    def move(self, direction : str, amount : int) -> None:
        if direction == 'forward':
            self._horizontal_position = self._horizontal_position + amount
            self._depth = self._depth + self._aim*amount
        elif direction == 'up':
            self._aim = self._aim - amount
        elif direction == 'down':
            self._aim = self._aim + amount
        else:
            raise Exception(f'unkown direction {direction}')

with open('PuzzleInput_day02.txt') as f:
    lines = f.readlines()
    course = [line.split() for line in lines]

sub = Submarine()

for command in course:
    sub.move(command[0], int(command[1]))

print(sub.horizontal_position, sub.depth)
print(sub.solution)