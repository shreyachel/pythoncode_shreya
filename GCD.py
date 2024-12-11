#Write a python program to find the GCD(Greatest Common Divisor) of two numbers.
def gcd(a, b):
    # Euclidean algorithm to find GCD
    while b:
        a, b = b, a % b
    return a

# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the GCD
result = gcd(num1, num2)

# Output the result
print(f"The GCD of {num1} and {num2} is: {result}")
