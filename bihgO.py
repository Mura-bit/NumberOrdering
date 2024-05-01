# int sum(int n) {
#     if n <= 0 {
#         return 0
#     }
#     return n + sum(n-1)
# }


# int pairSumSequence(int n) {
#     int sum = 0
#     for (int i=0; i<n ; i ++) {
#         sum += pairSum(i, i + 1) 
#     }
#     return sum
# }

# int pairSum(int a, int b) {
#     return a + b
# }

# student = 1
# while student > 3:
#     total = 0
#     for score in range(1,4):
#         score = int(input("Enter test score: "))
#         total += score
#     average = total/3
#     print("Student", student, "average: ", average)
#     student += 1

#/////////////////////////////////////////////////////////

# numOrdering = False

# for i in numOrdering:
#     num1 = input("Type here your first number: ")
#     if num1.isdigit() and int(num1) >= 0:
#         numOrdering = True
#     else:
#         print("It is not a valid number!")

# for i in numOrdering:
#     num2 = input("Type here your second number: ")
#     if num2.isdigit() and int(num2) >= 0:
#         numOrdering = True
#     else:
#         print("It is not a valid number!")

# for i in numOrdering:
#     num3 = input("Type here your first number: ")
#     if num3.isdigit() and int(num3) >= 0:
#         numOrdering = True
#     else:
#         print("It is not a valid number!")

# orderNum = False
# while not orderNum:
#     num3 = input("And the last number: ")
#     if num3.isdigit() and int(num3) >= 0:
#         orderNum = True
#     else:
#         print ("Error: because type here only number!")


# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)

# if num1 <= num2:
#     if num1 <= num3:
#         print(num1)
#         if num2 <= num3:
#             print(num2, num3)
#         else:
#             print(num3, num2)
#     else:
#         print(num3)
#         print(num1, num2)
# else:
#     if num2 <= num3:
#         print(num2)
#         if num1 <= num3:
#             print(num1, num3)
#         else:
#             print(num3,num1)
#     else:
#         print(num3)
#         print(num2, num1)#


#///////////////////////////////////////////////////////////

# while nums in range(3):
#     numOrdering = False
#     while not numOrdering:
#         num = input("Type here your number: ")
#         if num.isdigit() and int(num) >= 0:
#             numOrdering = True
#         else:
#             print("Error: because type here only number")

# num = int(num1)
# num = int(num2)
# num = int(num3)


# def correctNum(number):
#     if number.isdigit() and int(number) >= 0:
#         True
#     else:
#         False

# def getNumber():
#     while True:
#         num = input("Plese enter a number here: ")
#         if correctNum(num):
#             return int(num)
#         else:
#             print("Please enter a valid positive integer.")

# def main():
#     print("Enter three positive numbers:")

#     num1 = correctNum("Enter the first number: ")
#     num2 = correctNum("Enter the second number: ")
#     num3 = correctNum("Enter the third number: ")


#     if num1 <= num2:
#         if num2 <= num3:
#             print("Numbers in ascending order:", num1, num2, num3)
#         elif num1 <= num3:
#             print("Numbers in ascending order:", num1, num3, num2)
#         else:
#             print("Numbers in ascending order:", num3, num1, num2)
#     else:
#         if num1 <= num3:
#             print("Numbers in ascending order:", num2, num1, num3)
#         elif num2 <= num3:
#             print("Numbers in ascending order:", num2, num3, num1)
#         else:
#             print("Numbers in ascending order:", num3, num2, num1)

# if __name__ == "__main__":
#     main()
#////////////////////////////////////////////////////

# def print_Asterisk(numAsterisk):
#     for i in range(numAsterisk):
#         print("*", end="")
#     print()

# print_Asterisk(1)
# print_Asterisk(3)
# print_Asterisk(5)
# print_Asterisk(7)

#/////////////////////////////////

# import turtle
# import random

# turtle.speed(0)

# def drawStar(sideLen, color):
#     turtle.color(color)
#     for _ in range (5):
#         turtle.forward(sideLen)
#         turtle.right(144)

# turtle.pensize(5)
# len = 50 
# for color in ["black", "red", "yellow", "green", "purple"]:
#     drawStar(len, color)
#     len += 50

# turtle.done()


#/////////////////////////////////////////////////

# student = 1
# while student <= 3:
#     total = 0
#     for score in range(1, 4):
#         score = int(input("Enter test score: "))
#         total += score
#     average = total/3
#     print("Student", student, "average: ", average)
#     student += 1

#/////////////////////////////////////////////////////////

# nums = 3 
# resNumbers = [] 

# while nums > 0:
#     num = input("Type here your number: ")
#     if num.isdigit() and int(num) >= 0:
#         resNumbers.append(int(num)) 
#         nums = nums - 1
#     else:
#         print("Please type only positive integer or number!")

# resNumbers.sort()

# print("Numbers: ", resNumbers)

#/////////////////////////////////////////////////////////////

# nums = 3
# num1 = None
# num2 = None
# num3 = None

# while nums > 0:
#     num = input("Type here your number: ")
#     if num.isdigit() and int(num) >= 0:
#         num = int(num)
#         if num1 is None:
#             num1 = num
#         elif num2 is None:
#             num2 = num
#         elif num3 is None:
#             num3 = num
#         nums -= 1
#     else:
#         print("Error: Please type only numbers")

# smallest = num1
# middle = num1
# largest = num1

# if num2 is not None:
#     if num2 < smallest:
#         smallest = num2

# if num3 is not None:
#     if num3 < smallest:
#         smallest = num3

# if num2 is not None:
#     if num2 > smallest and num2 < num3 or num3 is None:
#         middle = num2

# if num3 is not None:
#     if num3 > smallest:
#         middle = num3

# if num2 is not None:
#     if num2 > middle:
#         largest = num2

# if num3 is not None:
#     if num3 > largest:
#         largest = num3

# print("Numbers in ascending order:", smallest, middle, largest)