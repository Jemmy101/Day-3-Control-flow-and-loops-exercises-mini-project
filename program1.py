# 1. Write a program to check if a number is positive, negative, or zero
number = int(input("Enter the number you want to check"))
if (number>0):
    print(f"The number {number} is positive")
elif(number<0):
    print(f"The number {number} is negative")
else:
    print(f"The number {number} is zero")