import random


SampleSizeString = ""
SampleSize = 0
acceptInputSample = False

NumberOfDiceString = ""
NumberOfDice = 0
acceptInputNumberOfDice = False

NumberOfFacesString = ""
NumberOfFaces = 6
acceptInputNumberOfFaces = False

#get the sample size
while(True):
    try:
        print("Enter a sample size. It must be an integer. (>=10000 recomended)")
        SampleSizeString = input()
        SampleSize = int(SampleSizeString)
        acceptInputSample = True
    except TypeError:
        print("You did not enter an integer, try again")
    if acceptInputSample:
        if SampleSize <= 0:
            print("You entered a non-posative value, re-run the code and enter a posative integer.")
            exit()
        elif SampleSize < 5000:
            print("This is a small sample, larger samples are more statistically accurate")
        break

#Get the number of dice
while(True):
    try:
        print("Enter the amount of dice. This must be greater than zero.")
        NumberOfDiceString = input()
        SampleSize = int(SampleSizeString)
        acceptInput = True
    except TypeError:
        print("You did no enter an integer, try again")
    if acceptInput:
        if SampleSize <= 0:
            print("You entered a non-posative value, re-run the code and enter a posative integer.")
            exit()
        elif SampleSize < 5000:
            print("This is a small sample, larger samples are more statistically accurate")
        break

# Check if the input is a number

#declare our variables
data = []
datatemp = []


countOf53 = 0
countOf2 = 0
counter = 0
sum = 0

while(counter < SampleSize):
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)

    if(num1 + num2 == 12):
        countOf2 = countOf2 + 1

    if((num1 == 3 and num2 == 5) or (num1 == 5 and num2 == 3)):
        datatemptemp = []
        datatemptemp.append(num1)
        datatemptemp.append(num2)
        datatemp.append(datatemptemp)
        countOf53 = countOf53 + 1
    
    sum = sum + num1 + num2
    counter = counter + 1
    data.append(num1 + num2)
#print(data)
print(datatemp)
print("The average throw is: ", sum / SampleSize)
print("The chance of throwing doubles is: ",6 * countOf2/SampleSize)
print("The chance of throwing a 5 and a 3 is: ", countOf53/SampleSize)