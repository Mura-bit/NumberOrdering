


orderNum = False

while not orderNum:
    num1 = input("Type here your first number: ")
    if num1.isdigit() and int(num1) >= 0:
        orderNum = True
    else:
        print("It is not a valid number!")


orderNum = False
while not orderNum:
    num2 = input ("Type here your second number: ")
    if num2.isdigit() and int(num2) >= 0:
        orderNum = True
    else:
        print ("Error: type here only valid number!")
orderNum = False
while not orderNum:
    num3 = input("And the last number: ")
    if num3.isdigit() and int(num3) >= 0:
        orderNum = True
    else:
        print ("Error: because type here only number!")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 <= num2:
    if num1 <= num3: 
        print (num1, end="")
        if num2 <= num3:
            print (num2, num3) 
        else:
            print (num3, num2)
    else:
        print (num3, end="") 
        print (num1, num2)
else:
    if num2 <= num3:
        print (num2, end="") 
        if num1 <= num3:
            print (num1, num3)
        else:
            print (num3, num1)
    else:
        print (num3, end="")
        print (num2, num1)





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

