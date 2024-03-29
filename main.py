def add(num1, num2):
    pass

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    pass


try:
    result1 = add(10, b)
    result2 = subtract(20, 7)
    result3 = multiply(3, 6)
    result4 = divide(15, 3)
    print(result1, result2, result3, result4)
except(NameError):
    print("Please enter only int")
