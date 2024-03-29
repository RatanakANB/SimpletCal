def add(num1, num2):
    pass

def subtract(num1, num2):
    if type(num1) == int and type(num2) == int:
        return num1 - num2
    else:
        return "Please enter only int"

def multiply(num1, num2):
    if type(num1) == int and type(num2) == int:
        return num1 * num2
    else:
        return "Please enter only int"

def divide(num1, num2):
    pass



result1 = add(10, 5)
result2 = subtract(20, 7)
result3 = multiply(3, "b")
result4 = divide(15, 3)

print(result1, result2, result3, result4)
