def add(lst):
    return sum(lst)

def subtract(lst):
    result = lst[0]
    for num in lst[1:]:
        result -= num
    return result

def multiply(lst):
    result = 1    #we want to multiply all numbers
    for num in lst:
        result *= num
    return result

def divide(lst):
    result = lst[0]
    for num in lst[1:]:
        if num != 0:
            result /= num
        else:
            return "Error: Division by zero"
    return result
    