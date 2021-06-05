
def main():
    freq = 0 # init frequenzy
    with open('PuzzleInput01.txt', 'r') as file:
        for change in file:
            freq = eval('freq' + change) 
    print(freq)
    
if __name__ == '__main__':
    main()