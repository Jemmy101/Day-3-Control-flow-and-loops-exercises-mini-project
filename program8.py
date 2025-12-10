# Print multiplication table of a number
mul = 1
n = int(input("Enter the number"))

for i in range (1,11):
    mul = n *i
    print(f"{i} X {n} = {mul}")
