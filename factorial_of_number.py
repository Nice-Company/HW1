def factorial(num1):
    if num1 <= 1:
        return 1
    return factorial(num1 - 1) * num1

num1 = 5

fact = factorials(num1)

print("factorial of 5:", fact)