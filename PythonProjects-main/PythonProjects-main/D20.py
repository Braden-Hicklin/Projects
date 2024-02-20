import random

def Roll(rollCount, dice):
    total = 0
    critF = 0
    critS = 0
    for i in range(rollCount):
        roll = random.randint(1, dice)
        total += roll
        if roll == 1:
            critF += 1
        elif roll == 20:
            critS += 1
    avg = total / rollCount
    print("Your final value is: ", avg, ". You rolled a nat 1:", critF, "times, and you rolled a nat 20:", critS, "times.")
    
    return 0

def main():
    diceVal = input("What type of die would you like to roll?: ")
    print("How many d", diceVal, " would you like to roll?: ")
    diceNum = input()
    Roll(int(diceNum), int(diceVal))
    endWait = input()
    return 0

if __name__=="__main__":
    main()