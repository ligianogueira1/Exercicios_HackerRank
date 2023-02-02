#The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
#1.The first line contains the sum of the two numbers.
#2.The second line contains the difference of the two numbers (first - second).
#3.The third line contains the product of the two numbers.

#Input Format
#The first line contains the first integer, a. 
#The second line contains the second integer, b.

# Constraints
#1 <= a <= 10**10
#1 <= b <= 10**10

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The sum of the numbers is: {num1 + num2}")
print(f"The difference of the numbers is: {num1 - num2}")
print(f"The product of the numbers is: {num1 * num2}")
