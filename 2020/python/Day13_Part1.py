import math

def main():
    notes = ReadPuzzleInput("PuzzleInput_Day13.txt")
    bus, wait = findEarliestBus(notes)
    print("The answer is", bus, '*', wait, '=', bus*wait)

def findEarliestBus(notes):
    schedule = getSchedule(notes)
    waitingTime = math.inf
    Bus = 0
    for k, stamps in enumerate(schedule):
        for stamp in stamps:
            wait = stamp - notes[0]
            if wait < waitingTime:
                waitingTime = wait
                Bus = notes[1][k]
    return Bus, waitingTime

def getSchedule(notes):
    earliest = notes[0]
    horizon = 10
    schedule = [[] for bus in notes[1]]
    for t in range(earliest, earliest+horizon+1):
        for k, bus in enumerate(notes[1]):
            if t%bus == 0: schedule[k].append(t)
    return schedule

def ReadPuzzleInput(my_file):
    notes = []
    with open(my_file, 'r') as f:
        for k, line in enumerate(f):
            if k == 0: notes.append(int(line.rstrip()))
            else:
                stamps = line.split(',')
                times = []
                for char in stamps:
                    try: times.append(int(char))
                    except: continue
                notes.append(times)
    return notes


if __name__ == "__main__":
    main()