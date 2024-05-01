import random

random.seed()
randomNum = random.randint(1,10)
maxAttempts = 3

while maxAttempts > 0:

    numGuess = input("Guess the number between 1-10... --> ")
    print("You have", maxAttempts - 1 , "attempts left")
    
    if not numGuess.isdigit():
        print("Error pleasse enter a valid number!")
        continue

    numGuess = int(numGuess)
    if numGuess > 10 or numGuess < 1:
        print("You are wrong! enter a number between 1 - 10!")
    elif numGuess == randomNum:
        print("You guessed the correct number, Congratulations")
        break
    elif numGuess < randomNum:
        print(numGuess, "<-- this guess is too small")
    elif numGuess < randomNum:
        print(numGuess, "I told you your guess is too small")
    else: 
        print(numGuess, "<-- Your guess is too high")
    maxAttempts = maxAttempts - 1


if maxAttempts == 0:
    print("Sorry, you've reached the maximum number of attempts.")
    print("The correct guessed number was:", randomNum)

