
def main():
    game = Game(ReadPuzzleInput("PuzzleInput_Day15.txt"))
    print('The number spoken is', game.play())

class Game:
    def __init__(self, numbers):
        self.number_counter   = 1
        self.spoken_numbers   = {}
        self.spoken_first_time = []
        for k, num in enumerate(numbers):
            self.spoken_numbers[str(num)] = k+1
            self.spoken_first_time.append(num)
            self.number_counter += 1
            self.last_spoken = num
        
    def play(self):
        while self.number_counter <= 2020:
            if self.last_spoken in self.spoken_first_time:
                speak = 0
                self.spoken_numbers[str(self.last_spoken)] = self.number_counter -1
            else:
                speak = self.number_counter - self.spoken_numbers[str(self.last_spoken)] - 1
                self.spoken_numbers[str(self.last_spoken)] = self.number_counter -1

            if speak in self.spoken_first_time:
                self.spoken_first_time.remove(speak)
            else:
                if str(speak) not in self.spoken_numbers:
                    self.spoken_first_time.append(speak)

            self.last_spoken = speak
            self.number_counter += 1
        return speak

def ReadPuzzleInput(my_file):
    with open(my_file, 'r') as f:
        for line in f:
            l = line.split(',')
            return [int(char) for char in l]

if __name__ == "__main__":
    main()