import numpy as np

class BingoBoard:
    def __init__(self, board : np.ndarray) -> None:
        '''
        Representation of a 5x5 bingo board.
        '''
        self._board = board
        self._marked = np.zeros_like(board, dtype=int)

    def mark(self, number : float):
        '''
        Marks the given number if present.
        '''
        if number in self._board:
            self._marked[np.where(self._board==number)] = 1

    def bingo(self) -> bool:
        '''
        Checks board for a BINGO.
        '''
        for row in self._marked:
            if not 0 in row: return True
        for col in self._marked.T:
            if not 0 in col: return True
        return False

    def score(self, number) -> int:
        return sum(self._board[self._marked==0])*number
    
# initialize bingo boards
with open('PuzzleInput_day04.txt') as f:
    data = f.readlines()
    drawing_numbers = [int(number) for number in data[0].strip().split(',')]
    bingo_boards = []
    data.pop(0)
    while data:
        data.pop(0)
        board = np.empty((5,5), dtype=int)
        for i in range(5):
            board[i,:] = [int(number) for number in data[0].split()]
            data.pop(0)
        bingo_boards.append(BingoBoard(board))

# draw numbers
for number in drawing_numbers:
    for k, board in enumerate(bingo_boards):
        board.mark(number)
        if board.bingo():
            break
    else:
        continue
    break

print(bingo_boards[k].score(number))