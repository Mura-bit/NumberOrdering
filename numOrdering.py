
nums = 3
num1 = None
num2 = None
num3 = None

while nums > 0:
    num = input("Type here your number: ")
    if num.isdigit() and int(num) >= 0:
        num = int(num)
        if num1 is None:
            num1 = num
        elif num2 is None:
            num2 = num
        elif num3 is None:
            num3 = num
        nums -= 1
    else:
        print("Please type only numbers")

smallest = num1
middle = num1
largest = num1

if num2 is not None:
    if num2 < smallest:
        smallest = num2

if num3 is not None:
    if num3 < smallest:
        smallest = num3

if num2 is not None:
    if num2 > smallest and num2 < num3 or num3 is None:
        middle = num2

if num3 is not None:
    if num3 > smallest:
        middle = num3

if num2 is not None:
    if num2 > middle:
        largest = num2

if num3 is not None:
    if num3 > largest:
        largest = num3

print("Numbers :", smallest, middle, largest)


#/////////////////////////////////////////////////////

# import random

# randomNum = random.randint(7,10)
# maxAttempts = 2
# attempts = 0

# sum = 0

# while True:
#     numStr = input("Guess the number between 7-10... --> ")
#     num = int(numStr)
    
#     if num == 0:
#         break 
#     if num == randomNum:
#         print("Congratulations! You guessed the correct number.")
#         break 
#     elif num < randomNum:
#         print("Your guess is lower than the correct number.")
#     else:
#         print("Your guess is higher than the correct number.")
    
#     for i in range(1):
#         if num == randomNum & maxAttempts == attempts:
#             print("Good job")
#         elif num == randomNum & maxAttempts > attempts:
#             print("You have 2 attemts left")
#         else:
#             print("You have no more attemts left")

#     sum += num

#     if attempts == maxAttempts:
#         print("Sorry, you've reached the maximum number of attempts.")
#         print("The correct number was:", randomNum)




