
input = "PuzzleInput_Day22.txt"
data = open(input).read().strip().split("\n")
idx = data.index('')
player1 = [int(x) for x in data[1:idx]]
player2 = [int(x) for x in data[idx+2:]]

while player1 and player2:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if card1 > card2:
        player1.append(card1)
        player1.append(card2)
    else:
        player2.append(card2)
        player2.append(card1)

winner = player1 if player1 else player2

score=0
for worth, value in enumerate(reversed(winner), start=1):
    score += worth*value
print(f'score = {score}')
