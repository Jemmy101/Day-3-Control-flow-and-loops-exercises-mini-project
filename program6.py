# Sum of first N natural numbers
sum =0
n = int(input("Enter the number"))

for i in range (1,n+1):
    sum = sum + i

print(f"The sum of first N natural number is {sum}")