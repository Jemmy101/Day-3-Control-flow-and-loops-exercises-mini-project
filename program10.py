# 2. Calculate factorial of a number using a loop
fact =1 
n = int(input("Enter the number you want to get factorial for"))
for i in range (1,n+1):
    fact = fact * i
print(f"The factorial of {n} is {fact}")