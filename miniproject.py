# Mini-project: 
# • Combine control flow + loops into menu-driven program 
# • Options: 
# 1. Check even/odd 
# 2. Factorial calculator 
# 3. Multiplication table 
# 4. Print number pattern

while True:
    choice = int(input("1. Check even/odd 2. Factorial calculator 3. Multiplication table  4. Print number pattern 5. Exit"))
    if (choice == 1):
        # 2. Program to check if a number is even or odd
        number = int(input("Enter the number you want to check"))

        if(number%2==0):
            print(f"The number {number} is even")
        else:
            print(f"The number {number} is odd")
    
    elif(choice == 2):
        # 2. Calculate factorial of a number using a loop
        fact =1 
        n = int(input("Enter the number you want to get factorial for"))
        for i in range (1,n+1):
            fact = fact * i
        print(f"The factorial of {n} is {fact}")
                    
    elif(choice ==3):
        # Print multiplication table of a number
        mul = 1
        n = int(input("Enter the number"))

        for i in range (1,11):
            mul = n *i
            print(f"{i} X {n} = {mul}")
    elif(choice == 4):
        # 4. Print a pattern: 
        # * 
        # * * 
        # * * * 
        # * * * *

        for i in range (1, 5):
            print("*" * i)
    
    elif(choice == 5):
        break

    