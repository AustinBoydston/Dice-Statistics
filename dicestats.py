import random


SampleSizeString = ""
SampleSize = 0
acceptInputSample = False

NumberOfDiceString = ""
NumberOfDice = 2
acceptInputNumberOfDice = False

NumberOfFacesString = ""
NumberOfFaces = 6
acceptInputNumberOfFaces = False


DiceThrows = []



def SumArray(dataArray):
    sum = 0
    for a in dataArray:
        sum = sum + a
    return sum

#get the sample size from the user.
while(True):
    try:
        print("Enter a sample size. It must be an integer. (>=10000 recomended)")
        SampleSizeString = input()
        SampleSize = int(SampleSizeString)
        acceptInputSample = True
    except TypeError:
        print("You did not enter an integer, try again.")
    if acceptInputSample:
        if SampleSize <= 0:
            print("You entered a non-posative value, re-run the code and enter a posative integer.")
            exit()
        elif SampleSize < 1000:
            print("This is a small sample, larger samples are more statistically accurate")
        break

#Get the number of dice from the user.
while(True):
    try:
        print("Enter the amount of dice. This must be greater than zero.")
        NumberOfDiceString = input()
        NumberOfDice = int(NumberOfDiceString)
        acceptInputNumberOfDice = True
    except TypeError:
        print("You did no enter an integer, try again")
    if acceptInputNumberOfDice:
        if NumberOfDice <= 0:
            print("You entered a non-posative value, re-run the code and enter a posative integer.")
            exit()
        break


#Get the number of dice faces from the user.
while(True):
    try:
        print("Enter the number of faces on each dice. This must be 2 or greater.")
        NumberOfFacesString = input()
        NumberOfFaces = int(NumberOfFacesString)
        acceptInputNumberOfFaces = True
    except TypeError:
        print("You did no enter an integer, try again")
    if acceptInputNumberOfFaces:
        if NumberOfFaces < 2:
            print("You entered a number less than 2, re-run the code and enter a posative integer greater than or equal to 2.")
            exit()
        break




#declare our variables
data = []


#initialize counts for the given amount of possible a value outcomes on each dice
counts = []
ResultsInitCounter = 0
while(ResultsInitCounter <= (NumberOfFaces * NumberOfDice)):
    counts.append(0)
    ResultsInitCounter = ResultsInitCounter + 1


counter = 0
diceSum = 0

#throw the dice SampleSize amount of times
while(counter < SampleSize):
    Dice = []    
    diceSum = 0
    makeDiceCounter = 0
    
    while(makeDiceCounter < NumberOfDice):
        Dice.append(random.randint(1, NumberOfFaces))
        DiceThrows.append(Dice[makeDiceCounter])
        makeDiceCounter = makeDiceCounter + 1
    
    
    
    diceSum = SumArray(Dice)
    counts[diceSum] = counts[diceSum] + 1
    
    
    
     
    
    counter = counter + 1
    


# output section
printCounter = 0
while(printCounter <= NumberOfDice * NumberOfFaces):
    print("The probability of ", printCounter, " being thrown is: ", counts[printCounter] / SampleSize)
    printCounter = printCounter + 1
print("The average throw is: ", SumArray(DiceThrows) / SampleSize)

