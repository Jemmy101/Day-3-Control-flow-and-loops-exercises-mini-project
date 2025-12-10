# 3. Reverse a number using while loop
number = int(input("Enter a number"))
digit = number
reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print(f"The reverse of number is {reverse}")