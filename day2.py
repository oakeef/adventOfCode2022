scoring = {
    "A": 1,
    "X": 1,
    "B": 2,
    "Y": 2,
    "C": 3,
    "Z": 3
}

win = 6
tie = 3

rockPaperScissorsRounds = []
totalScore = 0

with open('day2input.txt') as rounds:
    for round in rounds:
        rockPaperScissorsRounds.append(round.strip().split(" "))

for round in rockPaperScissorsRounds:
    opponentScore = scoring[round[0]]
    PlayerScore = scoring[round[1]]

    # P1 and P2 tie
    if opponentScore == PlayerScore:
        totalScore += PlayerScore + tie
 
    # P1 Rock vs P2 Paper = P2 Win
    elif opponentScore == 1 and PlayerScore == 2:
        totalScore += PlayerScore + win

    # P1 Paper vs P2 Scissors = P2 Win
    elif opponentScore == 2 and PlayerScore == 3: 
        totalScore += PlayerScore + win

    # P1 Scissors vs P2 Rock = P2 Win
    elif opponentScore == 3 and PlayerScore == 1:
        totalScore += PlayerScore + win

    # All other scenarios are P2 loss
    else:
        totalScore += PlayerScore
        

print(totalScore)

# Part 2
startegy = {
    "X": "loss",
    "Y": "tie",
    "Z": "win"
}

totalScoreReal = 0

def findUserScoreWin(oppMove):
    if oppMove == 1:
        return 2
    elif oppMove == 2:
        return 3
    else: 
        return 1

def findUserScoreLoss(oppMove):
    if oppMove == 1:
        return 3
    elif oppMove == 2:
        return 1
    else: 
        return 2

for round in rockPaperScissorsRounds:
    opponentScore = scoring[round[0]]
    playerStrat = startegy[round[1]]

    if playerStrat == "tie":
        totalScoreReal += opponentScore
        totalScoreReal += tie

    elif playerStrat == "win":
        totalScoreReal += findUserScoreWin(opponentScore)
        totalScoreReal += win
        
    else:
        totalScoreReal += findUserScoreLoss(opponentScore)

print(totalScoreReal)
        